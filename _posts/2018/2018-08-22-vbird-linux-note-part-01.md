---
layout: post
title:  "《鸟哥的Linux私房菜-基础学习篇（第三版）》学习笔记-Part01-Linux的规则与安装"
subtitle:   ""
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    false
tags:
    - Linux
    - 技术相关
---

##目录

第1章 Linux是什么？<br>
<a href="#Keywords">Keywords</a><br>
<a href="#1.2.5">1.2.5 Linux的内核版本</a><br>
<a href="#1.2.6">1.2.6 Linux distribution</a><br>
<a href="#1.3.3">1.3.3 关于授权</a><br>
第2章 Linux如何学习<br>
<a href="#2.3.1">2.3.1 从头学习Linux基础</a><br>
第3章 主机规划与磁盘分区<br>
<a href="#3.1">3.1 Linux与硬件的搭配</a><br>
<a href="#3.1.3">3.1.3 各硬件设备在Linux中的文件名</a><br>
<a href="#3.2.1">3.2.1 磁盘连接的方式与设备文件名的关系</a><br>
<a href="#3.2.2">3.2.2 磁盘的组成复习</a><br>
<a href="#3.2.3">3.2.3 磁盘分区表（partition table）</a><br>
<a href="#3.2.4">3.2.4 开机流程与主引导分区（MBR）</a><br>
<a href="#3.2.5">3.2.5 Linux安装模式下，磁盘分区的选择（极重要）</a><br>
<a href="#3.3.2">3.3.2 主机的服务规划与硬件的关系</a><br>
第4章 安装CentOS 5.x与多重引导小技巧<br>
略<br>
第5章 首次登陆与在线求助 man page<br>
<a href="#5.1.4">5.1.4 X Window与命令行模式的切换</a><br>
<a href="#5.1.5">5.1.5 在终端界面登录linux</a><br>
<a href="#5.2">5.2 在命令行模式下执行命令</a><br>
<a href="#5.2.1">5.2.1 开始执行命令</a><br>
<a href="#5.2.2">5.2.2 基本命令的操作</a><br>
<a href="#5.2.3">5.2.3 重要的热键[Tab], [Ctrl]-c, [Ctrl]-d</a><br>
<a href="#5.2.4">5.2.4 错误信息的查看</a><br>
<a href="#5.3">5.3 Linux系统的在线求助man page与info page</a><br>
<a href="#5.3.1">5.3.1 man page</a><br>
<a href="#5.3.2">5.3.2 info page</a><br>
<a href="#5.3.3">5.3.3 其他有用的文件（documents）</a><br>
<a href="#5.5">5.5 正确的关机方法</a><br>

=================================================================================
## 第1章 Linux是什么？

<h3 id="Keywords">Keywords</h3>

 - GUI：Graphical User Interface
 - FSF：Free Software Foundation
 - GNU：GNU is Not Unix
 - POSIX：Portable Operationg System Interface
 - [LSB](http://www.linuxbase.org)：Linux Standard Base
 - [FHS](http://www.pathname.com/fhs)：File system Hierarchy Standard

<h3 id="1.2.5">1.2.5 Linux的内核版本</h3>

Linux的内核版本号一般长成这个样子：2.6.18-92.e15
- 主版本.次版本.释出版本-修改版本

次版本为奇数：development； 次版本为偶数：stable

<h3 id="1.2.6">1.2.6 Linux distribution</h3>

定义：这个“Kernel+Softwares+Tools”的可完全安装的系统。

Distribution主要分为两类：
- 一种是用RPM方式安装软件的系统，包括Red Hat，Fedora，SuSE
- 另一种是使用Debian的dpkg方式安装软件的系统，Debian，Ubuntu，B2D

想了解更多的Linux Distribution的下载于使用信息，参考：http://distrowatch.com

<h3 id="1.3.3">1.3.3 关于授权</h3>

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

<h3 id="2.3.1">2.3.1 从头学习Linux基础</h3>

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

<h3 id="3.1">3.1 Linux与硬件的搭配</h3>

强调：各个组件或设备在Linux下面都是一个文件。

<h3 id="3.1.3">3.1.3 各硬件设备在Linux中的文件名</h3>

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

<h3 id="3.2.1">3.2.1 磁盘连接的方式与设备文件名的关系</h3>

以IDE接口来说，通常，主机提供两个IDE接口，一个IDE接口可以连接两个IDE设备。两个IDE接口一般称为IDE1（primary）和IDE2（secondary），而每条扁平电缆上面的IDE设备可以被区分为Master与Slave。其文件名如下：

| IDE\Jumper | Master | Slave
| - | - | -
| IDE1(Primary) | /dev/hda | /dev/hdb
| IDE2(Secondary) | /dev/hdc | /dev/hdd

由于SCSI/SATA/USB硬盘是使用SCSI模块驱动的，所以这些设备的文件名是/dev/sd[a-p]，但是与IDE接口不同的是，其命名顺序是按照Linux内核检测到磁盘的顺序决定的。

<h3 id="3.2.2">3.2.2 磁盘的组成复习</h3>

![磁盘截面图]({{ site.url }}assets/2018/2018-08-22-vbird-linux-note-part-01/01.jpg)

盘片上细分出扇区（Sector）与柱面（Cylinder）两个单位，其中扇区每个为512bytes 。

整块儿磁盘的第一个扇区特别的重要，因为它记录了整块儿磁盘的重要信息。即：主引导分区（Master Boot Record，MBR）可以安装引导加载程序的地方，有446bytes；分区表（partition table）记录整块硬盘分区的状态，有64bytes。

<h3 id="3.2.3">3.2.3 磁盘分区表（partition table）</h3>

![磁盘分区表]({{ site.url }}assets/2018/2018-08-22-vbird-linux-note-part-01/02.png)

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

![图3-4_磁盘分区表的作用示意图]({{ site.url }}assets/2018/2018-08-22-vbird-linux-note-part-01/03.png)
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

<h3 id="3.2.4">3.2.4 开机流程与主引导分区（MBR）</h3>

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
Boot Loader除了可以安装在MBR之外，还可以安装在每个分区的引导扇区（boot sector）。<br>
![图04_引导加载程序的工作执行示意图]({{ site.url }}assets/2018/2018-08-22-vbird-linux-note-part-01/04.jpg)

总结：
- 每个分区都拥有自己的启动扇区（boot sector）。
- 图中的系统分区为第一及第二分区。
- 实际可开机的内核文件时放置到各分区内的。
- loader只会认识自己的系统分区内的可开机内核文件，以及其他loader而已。
- Loader可直接指向，或者将管理权间接交给另一个管理程序。

为什么安装多重引导，最好先安装Windows，然后安装Linux？（spfdisk/spfdisk.sourceforge.net）

<h3 id="3.2.5">3.2.5 Linux安装模式下，磁盘分区的选择（极重要）</h3>

目录树结构（directory tree），根目录（root directory）是“/”。下图中方框为文件夹，波浪线方框为文件。<br>
![图05_目录树相关性示意图]({{ site.url }}assets/2018/2018-08-22-vbird-linux-note-part-01/05.gif)

文件系统与目录树的关系（挂载mount）,所谓的挂载就是利用一个目录当成进入点，将磁盘分区的数据放置在该目录下；也就是说，进入该目录就可以读取该分区的意思。<br>
![图06_目录树与分区之间的相关性]({{ site.url }}assets/2018/2018-08-22-vbird-linux-note-part-01/06.png)

假设我的硬盘分为两区，partition 1挂载到根目录，partition 2则挂载到/home这个目录。则/home下的数据是保存在partition 2中的。

初次接触Linux，只要分区“/”和“swap”即可。建议预留一个备用的剩余磁盘容量。

<h3 id="3.3.2">3.3.2 主机的服务规划与硬件的关系</h3>

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

=================================================================================
## 第4章 安装CentOS 5.x与多重引导小技巧

略

=================================================================================
## 第5章 首次登陆与在线求助 man page

- 图像化界面被称为GNOME，其资源管理器被称为Nautilus。
- 以“.”开头的文件就是隐藏文件。
- 在GNOME中，使用[ctrl]+[space]来切换成中午输入法SCIM
- KDE也是常见的窗口管理程序，（SL：树莓派的页面好像就是KDE），其资源管理器被称为Konqueror。

<h3 id="5.1.4">5.1.4 X Window与命令行模式的切换</h3>

命令行模式通常被称为：terminal或者console。<br>
Linux默认提供6个Terminal来让用户登登录，切换方式是[Ctrl]+[Alt]+[F1]~[F6]<br>
切换回图形界面桌面的方式为：[Ctrl]+[Alt]+[F7]<br>
Linux默认的登录模式分两种:
- 仅有纯文本界面（run level 3），可以使用tty1~tty6。
- 带有图形界面（run level 5），可以使用tty1~tty7。其中tty7就是开机完成后的默认等待登录的图形环境。

如果使用run level3登录的话，默认没有图形界面，可以在任意得命令行界面输入“startx”来启动。但是需要满足以下条件：
- tty7没有是空出来的，没有其他窗口软件正在运作。
- 已经安装了X Window系统，且X Server是能够顺利启动的。
- 最好要有窗口管理员，如GNOME或者KDE。
- 启动X窗口所必须要的服务，例如字形服务器（X Font Server, XFS）必须要先启动。
  
Linux默认提供了7个Run level给我们使用，可以在/etc/inittab中配置。

<h3 id="5.1.5">5.1.5 在终端界面登录linux</h3>

登录后会显示"[admin@host-192-168-101-119 ~]$"：
- 其中admin是登录账号。
- @后面的东西是主机名
- ~代表当前用户的主文件夹。所以可以cd ~
- $是提示符，root的默认提示符是“#”，一般用户的默认提示符是“$”

注销Linux“exit”命令。

<h3 id="5.2">5.2 在命令行模式下执行命令</h3>

命令行模式登录后取得的程序被称为shell，是负责最外层和用户通信的。

<h3 id="5.2.1">5.2.1 开始执行命令</h3>

一般的命令长相：[admin@host-192-168-101-119 ~]$ command [-options] parameter1 parameter2 ...
- Command是命令或者可执行文件
- 选项的[]在实际使用时并不存在。“-”有可能在全拼的时候变为“--”，比如“-h”“--help”
- 参数可能是选项的参数，或者是命令或者可执行文件的参数。
- 命令，选项，参数等几个命令之间以空格来区分。不论空几格shell都视为一格。
- 按下[Enter]之后，命令就立即开始执行。
- 如果命令太长，可以使用反斜杠（\）来转义[Enter]，使命令连续到下一行。

以下三个命令“显示主文件夹下所有隐藏文件与相关的文件属性”实际的执行结果是一样的
- ls –al ~
- ls                   -al ~
- ls –a –l ~

多语言支持，Linux是支持多语言的，所以如果出现了乱码的话， 可以尝试切换语言。
- `echo $LANG` 显示目前所支持的语言
- `LANG=en_US` 修改语言为英语语系，修改后只对本次登录生效。

<h3 id="5.2.2">5.2.2 基本命令的操作</h3>

操作几个简单的小命令:

显示日期的命令：date
- 显示年月日：date +%Y/%m/%d
- 显示是时分：date +%H:%M
- 命令之后的参数除了前面带有减号“-”外，某些情况下，也会用“+”号。

显示日历的命令：cal
- 显示整年的月历：cal 2016
- cal的基本语法：cal [[month] year] 所以可以这么用：cal 10 2009

简单好用的计算器：bc
- 输入后进入这个软件的工作环境了，然后可以输入计算方程式计算了。退出的话，使用“quit"命令。
- 默认输出的结果只有整数，通过输入”scale=3“来设置小数点后的位数。

<h3 id="5.2.3">5.2.3 重要的热键[Tab], [Ctrl]-c, [Ctrl]-d</h3>

[Tab]键：
- 接在一串命令的第一个命令的后面，为“命令补全”
- 接在一串命令的第二个命令以后时，为“文件补齐”

[Ctrl]-c：
- 中断当前执行的命令

[Ctrl]-d：
- 这个组合键代表键盘输入结束（End of File, End of Input）的意思。相当于输入exit

<h3 id="5.2.4">5.2.4 错误信息的查看</h3>

错误信息基本上都是见名知义的。

出现“command not found”错误的原因：
- 命令不存在，该软件没有安装。
- 命令所在的目录，当前的用户并没有将它加入到命令搜寻路径中，请参考bash的PATH说明。
- 打错命令。

<h3 id="5.3">5.3 Linux系统的在线求助man page与info page</h3>

直接在命令行按两下Tab键，可以显示有多少命令是可用的。

<h3 id="5.3.1">5.3.1 man page</h3>

man是manual的简写。例：man date<br>
进去man功能后，按下空格键往下翻页，按下“q”按键来离开man的环境。<br>
![图07_manpage]({{ site.url }}assets/2018/2018-08-22-vbird-linux-note-part-01/07.png)
man page各个部分的含义：
- man date后第一行`DATE（1）`表示：一般用户可使用的命令。
- `NAME`解释了这个命令的含义。
- `SYNOPSIS`说明这个命令的基本语法。
- `DESCRIPTION`详细说明语法中谈到的各个参数的用法。
- `OPTIONS`针对SYNOPSIS部分中，有列举的所有可用的选项说明。
- `COMMANDS`当这个程序（软件）在执行的时候，可以在此程序（软件）中执行的命令。
- `FILES`这个程序或数据所使用或参考或连接到的某些文件。
- `ENVIRONMENT`与这个命令相关的环境参数的说明
- `AUTHOR`这个命令的作者
- `REPORTING BUGS`有bug就提交~
- `COPYRIGHT`受到著作权法的保护
- `SEE ALSO`还可以从哪里查到该命令相关的说明文件
- `EXAMPLE`一些可以参考的范例。
- `BUGS`是否有相关的错误。

刚刚的命令有`DATE（1）`，那么除了`1`以外，还有哪些呢？<br>
**更详细的内容可以使用`man 7 man`来获取**

| 代号 | 代表内容 |
| - | - |
| 1 | 用户在shell环境中可以操作的命令或可执行文件 |
| 2 | 系统内核可调用的函数与工具等 |
| 3 | 一些常用的函数（function）与函数库（library），大部分为C的函数库（libc）|
| 4 | 设备文件的说明，通常在/dev下的文件 |
| 5 | 配置文件或者是某些文件的格式 |
| 6 | 游戏（games）|
| 7 | 惯例与协议等，例如Linux文件系统，网络协议，ASCII code等说明|
| 8 | 系统管理员可用的管理命令 |
| 9 | 与kernel有关的文件 |

在man page中可以进行的操作：

|   按键    |   功能    |
|   -   |   -   |
|   空格键  |   向下翻一页  |
|   [Page Down] |   向下翻一页  |
|   [Page Up] |   向上翻一页  |
|   [Home] |   去到第一页  |
|   [End] |   去到最后一页  |
|   /string |   向下查询string字符串  |
|   ?string |   向上查询string字符串  |
|   n,N |   利用/或?来查询字符串时，利用n来进行继续下一个的查询。N则进行继续上一个的查询。  |
|   q |   退出man page  |

man的特殊用法：
- `man -f man`获取更多与man相关的信息。若要具体查看，则利用结果中的数字，即`man 7 man`。如果不加数字直接使用`man man`时的具体查询顺序在**/etc/man.conf**中配置
- `man -k man`模糊查询。凡是带有man的都会被带出来。
- 上面的两个命令有简略写法。`whatis man`=`man -f man`、`apropos man`=`man -k man`。若要使用这两个特殊的命令，需要创建whatis数据库才行。需要以root的身份执行如下命令`makewhatis`。

<h3 id="5.3.2">5.3.2 info page</h3>

除了`man`以外，Linux还提供了一种在线求助的方法，也就是`info`。<br>
与man page一下子输出一堆信息不同的是，info page则是将文件数据拆成一个一个的段落，每个段落用自己的页面来撰写，并且在各个页面中还有类似网页的“超链接”来跳到不同的页面中。每一个独立的页面被称为一个`node`。

![图08_info_page各说明文件相关性的示意图]({{ site.url }}assets/2018/2018-08-22-vbird-linux-note-part-01/08.gif)

info page就是通过命令在各个节点中“游走”的。以下是各个命令：

|   按键    |   功能    |
|   -   |   -   |
|   空格键  |   向下翻一页  |
|   [Page Down] |   向下翻一页  |
|   [Page Up] |   向上翻一页  |
|   [Tab] |   在节点之间移动，有节点的地方，通常会以“*”显示  |
|   [Enter] |   当光标在节点上面是，可以通过该按键进入节点  |
|   B |   移动光标到该info界面当中的第一个节点处  |
|   E |   移动光标到该info界面当中的最后一个节点处  |
|   N |   前往下一个节点处  |
|   P |   前往上一个节点处  |
|   U   |   向上移动一层    |
|   S(/)    |   在info page当中进行查询 |
|   H   |   显示求助菜单    |
|   ?   |   命令一览表  |
|   Q   |   结束这次的info page |

info page必须要用nfo page的格式才行。CentOS5讲info page的文件放置到`/usr/share/info`当中。

<h3 id="5.3.3">5.3.3 其他有用的文件（documents）</h3>

linux系统中还有一些内置的帮助文档，主要是对一些软件包（packages）的说明。如果是CentOS的话，文档往往保存在`/usr/share/doc/`当中。

<h3 id="5.5">5.5 正确的关机方法</h3>

Linux系统如果不正常关机，最大的问题是可能造成文件系统的损毁（因为来不及将数据回写到文件中，所以有些服务的文件会有问题）。所以正常情况下，要关机时需要注意下面几件事：
- 查看系统的使用状态。
    - 用`who`命令来查看系统都有谁在线。
    - 用`netstat -a`命令来查看系统的联网状态。
    - 用`ps -aux`命令来查看系统的使用状态。
- 通知在线用户关机的时刻。
    - 使用`shutdown`的特别命令功能。
- 正确的关机命令使用
    - 学会使用`shutdown`和`reboot`这两个命令。
- 使用`sync`命令将数据同步写入硬盘中
- 其他相关命令：`shutdown`、`reboot`、`halt`、`poweroff`

`sync`命令：
- 作用：将内存中的数据写入到硬盘中。
- 其实`shutdown`、`reboot`、`halt`等命令在关机前都会调用`sync`，但是多做几次会比较放心。
- `sync`可以被一般账号使用，只不过一般账号用户所更新的只是自己的数据。而root用户则可以更新整个系统的数据。
  
`shutdown`命令:
- 由于Linux中，关机是很重要的操作。
- 在主机面前以tty7界面来登录系统时，无论什么身份都可以关机。
- 如果用远程管理工具的话，则只能用root权限来关机。
- 可以选择关机，重启或者进入单用户操作模式。
- 可以设置立刻关机，或者某一特定时间才关机。
- 可以设定关机信息，在关机之前，将自己设置的消息传送给在线用户。
- 可以仅发出警告信息，但是不关机。
- 可以选择是否要用fsck检查文件系统。

`shutdown`命令的语法规则：`/sbin/shutdown [-t 秒] [-arkhncfF] 时间 [警告信息]`

| 参数 | 解释 |
| - | - |
| -t sec | -t 后加秒数，就是多少秒后关机的意思 |
| -k | 不关机，只是发送警告信息 |
| -r | 在将系统服务停掉之后就重启（常用） |
| -h | 将系统的服务停掉之后就关机（常用） |
| -n | 不经过init程序，直接以shutdown的功能来关机 |
| -f | 关机并开机之后，强制略过fsck的磁盘检查 |
| -F | 系统重启之后，强制进行fsck的磁盘检查 |
| -c | 取消已经在进行的shutdown名令内容 |
| 时间 | 必填参数，指定系统关机的时间 |

范例：`/sbin/shutdown -h 10 'I will shutdown after 10 mins'`