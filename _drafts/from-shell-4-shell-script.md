---
layout: post
title:  "从shell到shell script"
date:   2020-11-15 14:39:25 +0800
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - Linux
    - 技术
---

本质上是《鸟哥的Linux私房菜》第三部分的内容，以前小打小闹写过一些，但是这次想系统的学习下。契机是想写一个用于备份mysql的shell script。对我来说虽然用python来写可能编写的效率更高，但是服务器端往往是python2，总归就是麻烦。正好可以系统的学习下shell script也挺好。需要系统学习的朋友右拐去[鸟站](https://linux.vbird.org/linux_basic/centos7/0320bash.php)吧，我这就记录些精简的“干货”。

## 准备

| 文件 | 说明 
| - | - 
| /etc/shells | 记录了系统支持哪些shell
| /etc/passwd | 记录了登录后会取得的具体shell

bash shell的优势：
- 命令记忆`history`，上下方向键可以找到执行过的命令。注销时会写到`/.bash_history`中。注销前历史命令是保存在内存中的。
- 命令/文件补全`[tab]`。
- 命令别名功能`alias`，通过`alias lm='ls -al'`来设置。
- 作业控制、前台、后台控制。（GR：奇怪，这个不应该是操作系统提供的功能吗？）
- 程序脚本`shell scripts`。
- 通配符`wildcard *`。

type：bash shell的内建命令，可以通过type来找到一个命令的执行文件，也可以识别是否是bash shell的内建命令。

```bash shell
[root@Server-i-jwvdl9av3u ~]# type ls
ls 是 `ls --color=auto' 的别名
[root@Server-i-jwvdl9av3u ~]# type -t ls
alias
[root@Server-i-jwvdl9av3u ~]# type -a ls
ls 是 `ls --color=auto' 的别名
ls 是 /usr/bin/ls
[root@Server-i-jwvdl9av3u ~]# type -a type
type 是 shell 内建
type 是 /usr/bin/type
[root@Server-i-jwvdl9av3u ~]# type cd
cd 是 shell 内建
[root@Server-i-jwvdl9av3u ~]# type -a cd
cd 是 shell 内建
cd 是 /usr/bin/cd
```

## 变量

变量创建、修改、删除、升级环境变量（export）；""、''、``之间的区别，可以引用变量、内部是纯文本、会被优先执行。bash中的变量也有一定的命名规则。

```bash shell
[root@Server-i-jwvdl9av3u ~]# name=liutianyu
[root@Server-i-jwvdl9av3u ~]# echo $name
liutianyu
[root@Server-i-jwvdl9av3u ~]# echo ${name}
liutianyu
[root@Server-i-jwvdl9av3u ~]# echo $myname

[root@Server-i-jwvdl9av3u ~]# name=$name:xixixi
[root@Server-i-jwvdl9av3u ~]# echo $name
liutianyu:xixixi
[root@Server-i-jwvdl9av3u ~]# bash
[root@Server-i-jwvdl9av3u ~]# echo $name

[root@Server-i-jwvdl9av3u ~]# exit
exit
[root@Server-i-jwvdl9av3u ~]# export name
[root@Server-i-jwvdl9av3u ~]# bash
[root@Server-i-jwvdl9av3u ~]# echo $name
liutianyu:xixixi
[root@Server-i-jwvdl9av3u ~]# exit
exit
[root@Server-i-jwvdl9av3u ~]# unset name
[root@Server-i-jwvdl9av3u ~]# echo $name

[root@Server-i-jwvdl9av3u ~]# cd /lib/modules/`uname -r`/kernel
[root@Server-i-jwvdl9av3u kernel]# cd /lib/modules/$(uname -r)/kernel
[root@Server-i-jwvdl9av3u kernel]# name=liutianyu
[root@Server-i-jwvdl9av3u kernel]# myname="$name xixixi"
[root@Server-i-jwvdl9av3u kernel]# echo $myname
liutianyu xixixi
[root@Server-i-jwvdl9av3u kernel]# myname='$name xixixi'
[root@Server-i-jwvdl9av3u kernel]# echo $myname
$name xixixi
```

环境变量

```bash shell
[root@Server-i-jwvdl9av3u kernel]# env
HOME=/root
SHELL=/bin/bash
HISTSIZE=1000
MAIL=/var/spool/mail/root
LANG=zh_CN.UTF-8
...
[root@Server-i-jwvdl9av3u kernel]# env
myname='$name xixixi'
name=liutianyu
OSTYPE=linux-gnu
HOSTTYPE=x86_64
MACHTYPE=x86_64-redhat-linux-gnu
...
```


## 更新记录

- 2020年：初稿