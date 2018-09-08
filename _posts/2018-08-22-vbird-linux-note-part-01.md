---
layout: post
title:  "《鸟叔的Linux私房菜-基础学习篇（第三版）》学习笔记-Part01-Linux的规则与安装"
date:   2018-08-22 12:02:49 +0800
categories: jekyll update
---

=================================================================================
## 第1章 Linux是什么？

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