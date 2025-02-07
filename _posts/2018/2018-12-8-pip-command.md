---
layout: post
title:  "Python-pip的常用命令"
date:   2018-12-08 22:44:25 +0800
subtitle:   ""
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - Python
    - 技术相关
---

pip是PyPA推荐的用于管理Python包的工具，现在Python的安装包中已经自带了该工具。[GitHub地址](https://github.com/pypa/pip)

## 常用命令

### pip --help

`pip --help`帮助。
![help]({{ site.url }}assets/2018/2018-12-8-pip-command/02.png)

### pip list

`pip list`列出安装好的包以及对应的版本。
![list]({{ site.url }}assets/2018/2018-12-8-pip-command/01.png)

### pip install flask

`pip install flask`安装flask包，安啥用啥。

### pip install -r requirements.txt

`pip install -r requirements.txt`安装文本文件中写好的需要安装的包名和版本号。

requirements.txt中的文本示例：
```
psutil==5.4.5
pywinauto==0.6.4
requests==2.18.4
```
后期结合bat或者sh文件，就可以方便准备项目所需的依赖包了。

### pip 导出离线安装包并安装

有时候linux的服务器不能连接外网，可以通过在别的机器上下载后并打成离线安装包，然后拷贝到不能连接外网的设备上进行安装。

但是，好像该方式只支持python的包。一些可以通过pip安装的应用类的并不能通过这个方式导出，比如uWSGI。这个待确认原理。

#### 1.导出所安装的包

`pip freeze > requirements.txt`

#### 2.导出安装包

~~pip install --download /root/packs -r requirements.txt~~

`pip download pymysql -d "D:\pipDownloadTest"`

不清楚为什么，原来记的这个命令不好用了，所以更新一波。具体原因再说吧，最近有点忙。另外注意一点，比如request包又依赖的别的几个包（如下），所以导出时要一起导出才行，不过简单暴力的方法就是本机中有啥包，直接全灌倒离线服务器上也行😂
```
certifi==2018.4.16
chardet==3.0.4
idna==2.6
urllib3==1.22
requests==2.18.4
```

#### 3.拷贝导出的安装包到需要安装的机器上

#### 4.安装导出的安装包

`pip install --no-index --find-links=/root/packs/ -r requirements.txt`
