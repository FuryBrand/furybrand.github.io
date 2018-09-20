---
layout: post
title:  "《鸟叔的Linux私房菜-基础学习篇（第三版）》学习笔记-Part02-Linux文件、目录与磁盘格式"
date:   2018-09-15 20:25:49 +0800
categories: jekyll update
---
<!-- TOC -->

- [第6章 Linux的文件权限与目录配置](#6-linux)
    - [Keywords：](#keywords)
    - [1.2.5 Linux的内核版本](#125-linux)
    - [1.2.6 Linux distribution](#126-linux-distribution)
    - [1.3.3 关于授权](#133)
- [第2章 Linux如何学习](#2-linux)
    - [2.3.1 从头学习Linux基础](#231-linux)
- [第3章 主机规划与磁盘分区](#3)
    - [3.1 Linux与硬件的搭配](#31-linux)
    - [3.1.3 各硬件设备在Linux中的文件名](#313-linux)
    - [3.2.1 磁盘连接的方式与设备文件名的关系](#321)
    - [3.2.2 磁盘的组成复习](#322)
    - [3.2.3 磁盘分区表（partition table）](#323-partition-table)
    - [3.2.4 开机流程与主引导分区（MBR）](#324-mbr)
    - [3.2.5 Linux安装模式下，磁盘分区的选择（极重要）](#325-linux)
    - [3.3.2 主机的服务规划与硬件的关系](#332)
    - [主机硬盘的主要规划](#)

<!-- /TOC -->
## 第6章 Linux的文件权限与目录配置

### Keywords：

 - GUI：Graphical User Interface
 - FSF：Free Software Foundation
 - GNU：GNU is Not Unix
 - POSIX：Portable Operationg System Interface
 - [LSB](http://www.linuxbase.org)：Linux Standard Base
 - [FHS](http://www.pathname.com/fhs)：File system Hierarchy Standard

### 1.2.5 Linux的内核版本

Linux的内核版本号一般长成这个样子：2.6.18-92.e15
- 主版本.次版本.释出版本-修改版本

次版本为奇数：development； 次版本为偶数：stable

### 1.2.6 Linux distribution

定义：这个“Kernel+Softwares+Tools”的可完全安装的系统。

Distribution主要分为两类：
- 一种是用RPM方式安装软件的系统，包括Red Hat，Fedora，SuSE
- 另一种是使用Debian的dpkg方式安装软件的系统，Debian，Ubuntu，B2D

想了解更多的Linux Distribution的下载于使用信息，参考：http://distrowatch.com

### 1.3.3 关于授权

Open Source：
- GNU General Public License
- Berkeley Software Distribution(BSD)
- Apache License, Version 2.0 修改并重新发布后的软件必须依然定名为Apache

Close Source：
- 	Freeware，不同于Free Software，Freeware是“免费软件”而不是“自由软件”。
- 	Shareware，试用期软件

=================================================================================
## 第2章 Linux如何学习

[Netman 網中人的學習 Linux](http://www.study-area.org/menu1.htm)

[The Linux Documentation Project](http://www.tldp.org/)

### 2.3.1 从头学习Linux基础

学习路线：
- 计算机概论与硬件相关知识：做到听过，有概念即可
- 先从Linux的安装和命令学起：先装一套Linux再说
- Linux操作系统的基础技能：用户/用户组的概念，权限的观念，程序的定义等
- 务必学会vi文本编辑器：vi会被很多的软件调用，所有Unix like系统上面都有vi。
- Shell与Shell脚本的学习：会用Shell，包括“正则表达式”、“管道命令”、“数据流重定向”等
- 一定要会软件管理员：由于经常会遇到自己安装驱动或者额外软件的时候，尤其是嵌入式设备等，这个时候就要用Tarball/RPM/DPKG等软件管理员的安装方式就很重要。
- 网络基础的建立：IP，路由等概念。

=================================================================================
## 第3章 主机规划与磁盘分区

### 3.1 Linux与硬件的搭配

强调：各个组件或设备在Linux下面都是一个文件。

### 3.1.3 各硬件设备在Linux中的文件名

| 设备 | 设备在Linux内的文件名  
| - | - 
| IDE硬盘 | /dev/hd[a-d]，其中[]的意思是字母为a-d当中的任意一个
| SCSI/SATA/USB硬盘 | /dev/sd[a-p]
| U盘 | /dev/sd[a-p]，与SATA相同
| 软驱 | /dev/fd[0-1]
| 打印机 |25针：/dev/lp[0-2] <br> USB：/dev/usb/lp[0-15]
| 鼠标 | USB:/dev/usb/mouse[0-15] <br> PS2:/dev/psaux
| 当前CD ROM/DVD ROM | /dev/cdrom
| 当前鼠标 | /dev/mouse
| 磁带机 | IDE:/dev/ht0 <br> SCSI:/dev/st0

需要特别留意的是硬盘，每个磁盘驱动器的磁盘分区(partition)不同时，其磁盘文件名还会改变。
更多Linux内核支持的硬件设备与文件名，可以参考[这里](www.kernel.org/pub/linux/docs/device-list/devices.txt)

### 3.2.1 磁盘连接的方式与设备文件名的关系

以IDE接口来说，通常，主机提供两个IDE接口，一个IDE接口可以连接两个IDE设备。两个IDE接口一般称为IDE1（primary）和IDE2（secondary），而每条扁平电缆上面的IDE设备可以被区分为Master与Slave。其文件名如下：

| IDE\Jumper | Master | Slave
| - | - | -
| IDE1(Primary) | /dev/hda | /dev/hdb
| IDE2(Secondary) | /dev/hdc | /dev/hdd

由于SCSI/SATA/USB硬盘是使用SCSI模块驱动的，所以这些设备的文件名是/dev/sd[a-p]，但是与IDE接口不同的是，其命名顺序是按照Linux内核检测到磁盘的顺序决定的。

### 3.2.2 磁盘的组成复习

![磁盘截面图]({{ site.url }}assets/2018-08-22-vbird-linux-note-part-01/01.jpg)

盘片上细分出扇区（Sector）与柱面（Cylinder）两个单位，其中扇区每个为512bytes 。

整块儿磁盘的第一个扇区特别的重要，因为它记录了整块儿磁盘的重要信息。即：主引导分区（Master Boot Record，MBR）可以安装引导加载程序的地方，有446bytes；分区表（partition table）记录整块硬盘分区的状态，有64bytes。

### 3.2.3 磁盘分区表（partition table）

![磁盘分区表]({{ site.url }}assets/2018-08-22-vbird-linux-note-part-01/02.png)

在分区表所在的64bytes中，总共分为4组记录区，每组记录区记录了该区段的起始与结束的柱面号码。

所以假设硬盘设备的文件名为：/dev/hda，那么每个分区的文件名是：
- P1：/dev/hda1
- P2：/dev/hda2
- P3：/dev/hda3
- P4：/dev/hda4 

由于分区表只有64bytes，所以最多只能容纳4个分区，这4个分区被称为主(Primary)或者扩展(Extended)分区。

根据上面的说明，我们能总结几点重要的信息：
- 所谓的“分区”，只是针对那个64bytes的分区表进行设置而已。
- 硬盘默认的分区表仅能写入四组分区信息。
- 这四组分区信息我们称为主（Primary）或者扩展（Extended）。
- 分区的最小单位为柱面(cylinder)。
- 当系统要写入磁盘时，一定会参考磁盘分区表，才能针对某个分区进行数据的处理。

分区的必要性，即为什么要分区：
- 数据的安全性，将数据分门别类来管理。
- 系统的性能考虑：将数据集中保存，磁盘只会在相应的柱面范围进行检索，有助于提高系统的读取速度。

![图3-4_磁盘分区表的作用示意图]({{ site.url }}assets/2018-08-22-vbird-linux-note-part-01/03.png)
利用扩展分区的方式，可以将硬盘分成4个以上的分区。其中P1是主分区，P2是扩展分区。

扩展分区的目的是使用而外的扇区来记录分区信息，所以不能拿来格式化。

文件名：
- P1：/dev/hda1
- P2：/dev/hda2
- L1：/dev/hda5
- ...
  
主分区、扩展分区、逻辑分区的特性：
- 主分区与扩展分区最多可以有4个（硬盘的限制）。
- 扩展分区最多只能有一个（操作系统的限制）。
- 逻辑分区是由扩展分区持续切割出来的分区。
- 能够被格式化后作为数据访问的分区为主分区与逻辑分区。扩展分区无法格式化。
- 逻辑分区的数量，依操作系统的不同而不同，在Linux系统中，IDE硬盘最多有59个逻辑分区（5号-63号），SATA硬盘则有11个逻辑分区（5号-15号）。

### 3.2.4 开机流程与主引导分区（MBR）

BIOS：写入到主板上的一个程序。是计算机在开机后系统主动执行的第一个程序。<br>
CMOS：记录各项硬件参数且嵌入到主板上面的存储器。<br>
Boot Loader：引导加载程序是系统安装时提供的，所以它能识别硬盘内的文件系统格式，因此可以读取内核文件。
主要功能：1.提供开机选项菜单，实现多重引导。2.载入内核文件。3.转交其他Loader。

开机的步骤：
- a. BIOS分析计算机里面的存储设备，根据用户的设置去去的能够开机的硬盘。并到该硬盘里面去读取第一个扇区的MBR位置。
- b. MBR中存有的最基本的引导加载程序开始工作。
- c. 引导加载程序（Boot Loader）开始工作，目的是加载内核文件。
- d. 内核文件开始操作系统的功能。

双系统的实现原理：<br>
Boot Loader除了可以安装在MBR之外，还可以安装在每个分区的引导扇区（boot sector）。
![图04_引导加载程序的工作执行示意图]({{ site.url }}assets/2018-08-22-vbird-linux-note-part-01/04.jpg)

总结：
- 每个分区都拥有自己的启动扇区（boot sector）。
- 图中的系统分区为第一及第二分区。
- 实际可开机的内核文件时放置到各分区内的。
- loader只会认识自己的系统分区内的可开机内核文件，以及其他loader而已。
- Loader可直接指向，或者将管理权间接交给另一个管理程序。

为什么安装多重引导，最好先安装Windows，然后安装Linux？（spfdisk/spfdisk.sourceforge.net）

### 3.2.5 Linux安装模式下，磁盘分区的选择（极重要）

目录树结构（directory tree），根目录（root directory）是“/”。下图中方框为文件夹，波浪线方框为文件。
![图05_目录树相关性示意图]({{ site.url }}assets/2018-08-22-vbird-linux-note-part-01/05.gif)

文件系统与目录树的关系（挂载mount）,所谓的挂载就是利用一个目录当成进入点，将磁盘分区的数据放置在该目录下；也就是说，进入该目录就可以读取该分区的意思。
![图06_目录树与分区之间的相关性]({{ site.url }}assets/2018-08-22-vbird-linux-note-part-01/06.png)
假设我的硬盘分为两区，partition 1挂载到根目录，partition 2则挂载到/home这个目录。则/home下的数据是保存在partition 2中的。

初次接触Linux，只要分区“/”和“swap”即可。建议预留一个备用的剩余磁盘容量。

### 3.3.2 主机的服务规划与硬件的关系

由于主机的服务目的不同，所需要的硬件等级和配置也不同，下面是几种常见的主机服务：
- 打造Windows与Linux共存的环境
- NAT（达到路由器的功能）
- SAMBA（加入Windows网络上的邻居）
- /home可以考虑独立出来，并加大容量
- Mail(邮件服务器)
- /var可以考虑独立出来，并加大容量
- Web(WWW服务器)
- DHCP（提供客户端自动获取IP的功能）
- Proxy（代理服务器）
- FTP

### 主机硬盘的主要规划

硬盘的规划对于Linux初学者而言，那将是造成你“头疼”的主要凶手之一。因为硬盘的分区技巧需要对于Linux文件结构有相当程序的认知之后才能够做出比较完善的规划的。所以，目前只要有个基础认识就行。没有安装过十次以上的Linux系统，是学不会Linux与磁盘分区的。

基本硬盘的分区模式：
- 懒人分区法：至分出根目录与内容交换空间（ / & swap）即可。
- 稍微麻烦点的方式：/ + /usr + /home + /var + swap