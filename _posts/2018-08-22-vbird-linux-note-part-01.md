---
layout: post
title:  "《鸟叔的Linux私房菜-基础学习篇（第三版）》学习笔记-Part01-Linux的规则与安装"
date:   2018-08-22 12:02:49 +0800
categories: jekyll update
---

# 第1章 Linux是什么？

## Keywords：

 - GUI：Graphical User Interface
 - FSF：Free Software Foundation
 - GNU：GNU is Not Unix
 - POSIX：Portable Operationg System Interface
 - [LSB](http://www.linuxbase.org)：Linux Standard Base
 - [FHS](http://www.pathname.com/fhs)：File system Hierarchy Standard

## 1.2.5 Linux的内核版本

Linux的内核版本号一般长成这个样子：2.6.18-92.e15
- 主版本.次版本.释出版本-修改版本

次版本为奇数：development； 次版本为偶数：stable

## 1.2.6 Linux distribution

定义：这个“Kernel+Softwares+Tools”的可完全安装的系统。

Distribution主要分为两类：
- 一种是用RPM方式安装软件的系统，包括Red Hat，Fedora，SuSE
- 另一种是使用Debian的dpkg方式安装软件的系统，Debian，Ubuntu，B2D

想了解更多的Linux Distribution的下载于使用信息，参考：http://distrowatch.com

## 1.3.3 关于授权

Open Source：
- GNU General Public License
- Berkeley Software Distribution(BSD)
- Apache License, Version 2.0 修改并重新发布后的软件必须依然定名为Apache

Close Source：
- 	Freeware，不同于Free Software，Freeware是“免费软件”而不是“自由软件”。
- 	Shareware，试用期软件

# 第2章 Linux如何学习