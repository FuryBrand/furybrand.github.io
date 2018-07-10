---
layout: post
title:  "我的Linux常用命令（持续更新）"
date:   2018-07-08 11:46:49 +0800
categories: jekyll update
---
最近在通过《鸟哥的Linux私房菜》系统得学习linux。可是工作中还是要用Linux的，有些命令啥的就是现学现用，这个笔记就是记录这个的。

# 常用

| 命令 | 简介 | 备注 |
| - | - | - |
|pwd |显示当前路径 | |
|mv |重命名或移动 | |
|cp |复制 |-r 递归将子文件全部复制 |
|mkdir |创建文件夹 | |
|/sbin/ifconfig |获取ip地址 | |
|zip -r mydata.zip mydata |把当前目录下面的mydata目录压缩为mydata.zip| |
|unzip |解压zip文件。unzip xx.zip | |
|tar |将文件压缩成tar文件| |


|查看电脑和操作系统的信息：uname -a
查询内核版本：cat /proc/version
查询发行版本：cat /etc/issue
查询发行版本：lsb_release -a(适用于所有的linux，包括Redhat、SuSE、Debian等发行版，但是在debian下要安装lsb) |查询linux系统的版本 | |
