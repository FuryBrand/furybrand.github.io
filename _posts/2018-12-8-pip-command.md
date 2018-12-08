---
layout: post
title:  "Python-pip的常用命令"
date:   2018-12-08 22:44:25 +0800
categories: jekyll update
---

pip是PyPA推荐的用于管理Python包的工具，现在Python的安装包中已经自带了该工具。[GitHub地址](https://github.com/pypa/pip)

- [常用命令](#%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4)
    - [pip --help](#pip---help)
    - [pip list](#pip-list)
    - [pip install flask](#pip-install-flask)
    - [pip install -r requirements.txt](#pip-install--r-requirementstxt)
    - [pip 导出离线安装包并安装](#pip-%E5%AF%BC%E5%87%BA%E7%A6%BB%E7%BA%BF%E5%AE%89%E8%A3%85%E5%8C%85%E5%B9%B6%E5%AE%89%E8%A3%85)
        - [1.导出所安装的包](#1%E5%AF%BC%E5%87%BA%E6%89%80%E5%AE%89%E8%A3%85%E7%9A%84%E5%8C%85)
        - [2.导出安装包](#2%E5%AF%BC%E5%87%BA%E5%AE%89%E8%A3%85%E5%8C%85)
        - [3.拷贝导出的安装包到需要安装的机器上](#3%E6%8B%B7%E8%B4%9D%E5%AF%BC%E5%87%BA%E7%9A%84%E5%AE%89%E8%A3%85%E5%8C%85%E5%88%B0%E9%9C%80%E8%A6%81%E5%AE%89%E8%A3%85%E7%9A%84%E6%9C%BA%E5%99%A8%E4%B8%8A)
        - [4.安装导出的安装包](#4%E5%AE%89%E8%A3%85%E5%AF%BC%E5%87%BA%E7%9A%84%E5%AE%89%E8%A3%85%E5%8C%85)

## 常用命令

### pip --help

`pip --help`帮助。
![help]({{ site.url }}assets/2018-12-8-pip-command/02.png)

### pip list

`pip list`列出安装好的包以及对应的版本。
![list]({{ site.url }}assets/2018-12-8-pip-command/01.png)

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

`pip install --download /root/packs -r requirements.txt`

#### 3.拷贝导出的安装包到需要安装的机器上

#### 4.安装导出的安装包

`pip install --no-index --find-links=/root/packs/ -r requirements.txt`