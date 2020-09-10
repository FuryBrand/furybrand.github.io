---
layout: post
title:  "Python-批量修改Linux服务器的密码"
date:   2018-09-06 20:02:49 +0800
subtitle:   ""
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - Python
    - 技术相关
---

### 背景

由于服务器安全问题，要将admin用户也都换成强密码。之前的密码一直是admin/admin，手动捂脸.........

可是无奈好几套测试环境服务器数量太多，共88台服务器。一个一个弄的话，简直要命。所以写了这个小工具来进行批量处理。

### paramiko是什么？

[paramiko](http://www.paramiko.org/)是领先的原生Python SSHv2协议库。它支持Python2.7和Python3.4+。由于实现了SSH2协议，所以可以用于与远程机器进行安全连接。也可以实现SFTP连接。

### 环境

- python(Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32)
- paramiko(Ver:2.4.1)

*paramiko只需要用`pip install paramiko`来安装即可。

### 实现

主要包含主脚本`changeServersPWD.py`和记录了服务器信息的`servers.txt`。

## changeServersPWD.py

```
import paramiko
import sys
import os

# 获取服务器配置文件的文件名
file_name = input("请输入文件名（包含后缀如'servers.txt'），若不输入则默认读取'servers.txt'中的服务器信息：")
if file_name == '':
    file_name = sys.path[0]+'\\servers.txt'
else:
    file_name = sys.path[0]+'\\'+file_name

# 判断文件是否存在
if os.path.exists(file_name):
    pass
else:
    input("当前目录下不存在该文件，回车后程序结束")
    exit()

# 打开文件
with open(file_name, 'r', encoding='utf-8') as f:

    for i in f:
        L = i.split()
        host_name = L[0]
        port = L[1]
        root = L[2]
        root_pwd = L[3]
        user_name = L[4]
        user_pwd = L[5]

        # 创建SSH对象
        ssh = paramiko.SSHClient()
        try:
            # 允许连接不在known_hosts文件上的主机
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # 连接服务器
            ssh.connect(hostname=host_name, port=port, username=root, password=root_pwd, timeout=5)
            # 执行命令
            stdin, stdout, stderr = ssh.exec_command('echo "%s" | passwd --stdin %s' % (user_pwd, user_name))
            # 获取结果
            result = stdout.read().decode()
            # 获取错误提示（stdout、stderr只会输出其中一个）
            err = stderr.read()
            # 关闭连接
            ssh.close()
            # 打印提示消息
            print(host_name,"KO! change <",user_name,">'s password successful!")
            print("执行结果：", stdin, result, err)
        except Exception as e:
            # 关闭连接
            ssh.close()
            # 打印错误消息
            print(host_name, str(e))

input("执行完毕，回车后关闭当前窗口")
```

## servers.txt

```
192.168.158.110 22 root testpwd110 admin admin@fuza1.
192.168.158.111 22 root testpwd111 admin admin@fuza1.
192.168.158.112 22 root testpwd112 admin admin@fuza1.
```
主要分了6个字段，`服务器ip地址`，`ssh端口`，`root`，`root的用户名`，`想要修改密码的用户`，`用户对应的密码`。每个字段用空格隔开。

## 写在最后

程序已经打包好了。[下载]({{ site.url }}assets/2018/2018-09-06-python-change-pwd-linux-server/python-change-pwdVer0.2.zip)

为了不瞎眼，必须要写个脚本来实现。主要收到这两篇博文的启发,谢谢！

[鸣谢1](https://www.cnblogs.com/rainowl-ymj/p/7247287.html)
[鸣谢2](http://blog.51cto.com/weixiaoxin/2063323)
