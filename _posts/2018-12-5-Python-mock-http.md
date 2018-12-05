---
layout: post
title:  "Python-mock一个提供http协议的服务"
date:   2018-12-5 21:00:25 +0800
categories: jekyll update
---

内部系统和外部系统在对接的过程常见的几种协议有：http/https，webservice，AS系列，ftp/sftp，外部系统API等。

这次对接的外部系统是采用了http协议，通过白名单的形式来保证安全。但是和往常不同，这次的外部系统是通过被调用后提供信息，也就是说内部系统定时轮询去调用外部系统。那么功能测试阶段只能mock一下来搞了，不然就没法测了。还好是http，实现起来也相对比较简单。

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
![01]({{ site.url }}assets/2019-12-5-Python-mock-http/01.png)

先发送请求来设置值。
![02]({{ site.url }}assets/2019-12-5-Python-mock-http/02.png)

然后用再次请求之后就可以获得到刚才设置的值了。
![03]({{ site.url }}assets/2019-12-5-Python-mock-http/03.png)

如果用浏览器来访问的话，就会提示我们给出的信息了。
![04]({{ site.url }}assets/2019-12-5-Python-mock-http/04.png)

终端中会记录请求的记录。
![05]({{ site.url }}assets/2019-12-5-Python-mock-http/05.png)

## 4. 部署到服务器上吧~

往往办公机的网络可能会和服务器不能直接连通，那么我们就将它部署到服务器上吧。
