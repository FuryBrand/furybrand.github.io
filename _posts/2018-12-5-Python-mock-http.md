---
layout: post
title:  "Python-mock一个提供http协议的服务"
date:   2018-12-05 21:00:25 +0800
categories: jekyll update
---

内部系统和外部系统在对接的过程常见的几种协议有：http/https，webservice，AS系列，ftp/sftp，外部系统API等。

这次对接的外部系统是采用了http协议，通过白名单的形式来保证安全。但是和往常不同，这次的外部系统是通过被调用后提供信息，也就是说内部系统定时轮询去调用外部系统。那么功能测试阶段只能mock一下来搞了，不然就没法测了。还好是http，实现起来也相对比较简单。

目录：
- [categories: jekyll update](#categories-jekyll-update)
- [1. 准备工作](#1-%E5%87%86%E5%A4%87%E5%B7%A5%E4%BD%9C)
- [2. demo.py](#2-demopy)
- [3. 试着用一下吧~](#3-%E8%AF%95%E7%9D%80%E7%94%A8%E4%B8%80%E4%B8%8B%E5%90%A7)
- [4. 部署到服务器上吧~](#4-%E9%83%A8%E7%BD%B2%E5%88%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A%E5%90%A7)
  - [4.1 安装uWSGI](#41-%E5%AE%89%E8%A3%85uwsgi)
  - [4.2 安装Nginx](#42-%E5%AE%89%E8%A3%85nginx)
  - [4.3 配置Nginx](#43-%E9%85%8D%E7%BD%AEnginx)
  - [4.4 启动uWSGI](#44-%E5%90%AF%E5%8A%A8uwsgi)
  - [4.5 验证结果](#45-%E9%AA%8C%E8%AF%81%E7%BB%93%E6%9E%9C)

## 1. 准备工作

通过`pip install -U Flask`来安装Flask。Flask是一个使用 Python 编写的轻量级 Web 应用框架。在[GitHub](https://github.com/pallets/flask/)上可以找到相当有用的信息，我这里就是一个小Demo吧。

## 2. demo.py

新建一个python文件，将下面的代码复制进去执行下就行。

主要实现了如下功能：
- 1.用Postman向`/setReturn`地址发送请求，同时传入参数来设置接下来的返回值。
- 2.用Postman向`/return`地址发送请求，即可得到上一步骤传入的值。

```python
from flask import Flask ,jsonify,request

# 1. 先准备一个设置设置成功的提示
set_success_msg = {
    "code" : 100,
    "msg" : "返回值设置成功"
}

# 2. 准备一个全局变量来保存设置的返回值
global msg

# 3. 将该文件初始化为一个Flask的服务
app = Flask(__name__)

# 4. 修改服务配置。
# 这个据说是为了应对中文乱码的问题，但是我实际使用并没有这个问题。详情：ttp://docs.jinkan.org/docs/flask/config.html
app.config['JSON_AS_ASCII'] = False

# 5. 通过装饰器为服务添加路由，从而决定url。methods中决定了支持的请求方式。
@app.route('/getReturn',methods=['POST','GET'])
def getReturn():
    if request.method != 'POST':
        return '我们只支持POST请求哦'
    else:
        global msg
        return msg

@app.route('/setReturn',methods=['POST','GET'])
def setReturn():
    global msg
    msg = request.values.get('value')
    return jsonify(set_success_msg)

# 6. 以debug的方式运行程序，可以看到请求。
if __name__=='__main__':
    app.run(debug=True)
```

## 3. 试着用一下吧~

本地调试的话，直接运行python文件就可以启动服务了。
![01]({{ site.url }}assets/2018-12-5-Python-mock-http/01.png)

先发送请求来设置值。
![02]({{ site.url }}assets/2018-12-5-Python-mock-http/02.png)

然后用再次请求之后就可以获得到刚才设置的值了。
![03]({{ site.url }}assets/2018-12-5-Python-mock-http/03.png)

如果用浏览器来访问的话，就会提示我们给出的信息了。
![04]({{ site.url }}assets/2018-12-5-Python-mock-http/04.png)

终端中会记录请求的记录。
![05]({{ site.url }}assets/2018-12-5-Python-mock-http/05.png)

## 4. 部署到服务器上吧~

往往办公机的网络可能会和服务器不能直接连通，那么我们就将它部署到服务器上吧~

部署到服务器的话，可能就需要Nginx和uWSGI来帮忙了。Nginx用于反向代理，即外部请求打到服务器的80端口上之后就会被Nginx获取到。随后Nginx将其交给uWSGI来处理。所以uWSGI就是Web容器，用于运行起我们的程序从而处理从Nginx传递过来的请求。对了我用的服务器是CentOS6.6。

### 4.1 安装uWSGI

- 首先下载[uWSGI](https://projects.unbit.it/downloads/uwsgi-latest.tar.gz)后传到服务器上。有网络的话，可以用`wget http://projects.unbit.it/downloads/uwsgi-latest.tar.gz`来下载。
- 然后`tar zxf uwsgi-latest.tar.gz`解压文件。
- 随后`cd uwsgi-2.0.17.1`进入文件内
- 执行`make`来编译并安装uWSGI。

P.S. 关于配置，这个[手册](https://uwsgi-docs-zh.readthedocs.io/zh_CN/latest/Nginx.html)给了我很大的帮助。

### 4.2 安装Nginx

我的服务器里有，所以先不多提了，稍后补充一波。

### 4.3 配置Nginx

安装目录稍有不同，但是配置文件都在`nginx.conf`这个文件里。添加配置文件：

```
server
        {
         listen                 80; #对外暴露的端口，默认就是80不用变。
         server_name            test_mock.com; #如果不想那个配置host的话就用服务器的ip地址也没有关系。
location / {
         include uwsgi_params; #自0.8.40版本起，Nginx本身就包含了对使用 uwsgi protocol 的上游服务器的的支持。通过这个会默认引入一些参数。
         uwsgi_pass 127.0.0.1:8888; #uWSGI服务器启动后使用的ip和端口。稍后启动uWSGI时会用到。
         }
}
```

记得重启Nginx。

### 4.4 启动uWSGI

由于我们的代码就一个demo.py。所以将文件传到服务器上即可。然后到`uwsgi-2.0.17.1`文件夹内使用如下命令来启动uWSGI。

`./uwsgi --socket 127.0.0.1:8888 --wsgi-file /root/demo.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191 --callable app`

注意:
- 命令中的`/root/demo.py`是demo.py的路径。
- `--callable app`中的app是代码中的Flask的服务的名字。因为不是用python来直接运行，所以代码中的第6步实际在这种方式的运行下就没有用了。uWSGI是通过Flask服务的名字来启动的。

### 4.5 验证结果

用之前的方式来验证就可以。

