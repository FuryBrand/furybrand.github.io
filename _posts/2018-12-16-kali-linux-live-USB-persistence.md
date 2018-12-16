---
layout: post
title:  "Kali Linux-制作Live USB Persistence模式的启动盘"
date:   2018-12-16 09:46:25 +0800
categories: jekyll update
---

Kali Linux含有多种渗透测试软件，是一个测试自家wifi是否可以被轻易攻破的好工具（大雾😀）。我的PC都是Win10系统的，所以还是把这个系统装到U盘里比较合适。

其实直接灌到U盘里就可以用了，但是为了保存个人文件还是用Persistence模式比较好。

## 准备条件

因为需要Linux环境来操作，所以我们需要准备：
- U盘三个，每个至少要有4GB。两个写入Kali Linux，一个用于保存镜像文件（其实主要是为了算占用容量的大小，后续可能有好的方法，再更新）。
- Kali Linux的镜像文件-[官网地址](https://www.kali.org/downloads/)，版本有很多根据自己的需要来选择，如果不确定的话，建议直接完整版`Kali Linux 64 Bit`
- 安装有`Win32 Disk Imager`或者`balenaEtcher`的PC。

官网其实有相应的教程，英文好的伙伴建议直接阅读原文：
- [创建一个可以通过USB启动的Kali Linux](https://docs.kali.org/downloading/kali-linux-live-usb-install)
- [Kali Linux Live USB Persistence](https://docs.kali.org/downloading/kali-linux-live-usb-persistence)

## Step-01、将Kali Linux写入U盘并进入系统

### 使用`balenaEtcher`将Kali Linux写入U盘
![01]({{ site.url }}assets/2018-12-16-kali-linux-live-USB-persistence/01.png)

### 使用不想制作Live USB Persistence模式的启动盘的那个U盘来进入（我们只要他的Linux环境，后续就可以格式化了）

选择U盘启动
![02]({{ site.url }}assets/2018-12-16-kali-linux-live-USB-persistence/02.jpg)

选择`Live(amd64)`进入系统
![03]({{ site.url }}assets/2018-12-16-kali-linux-live-USB-persistence/03.jpg)

系统启动中
![04]({{ site.url }}assets/2018-12-16-kali-linux-live-USB-persistence/04.jpg)

## Step-02、为U盘添加Persistence模式

### 使用fdisk -l确认挂载点

因为我的PC本身有一块机械硬盘和一块固态硬盘，所以看起来有点多。我们可以打开终端，先`fdisk -l`，再插入要添加Persisitence模式的U盘后再次执行`fdisk -l`来判断是哪个挂载点。目前我的是**/dev/sdd1**和**/dev/sdd2**。
![05]({{ site.url }}assets/2018-12-16-kali-linux-live-USB-persistence/05.jpg)

### 执行命令进行分区

以此执行以下命令。
```
end=12gb
read start _ < <(du -bcm /media/root/2A5A-5592/kali-linux-2016.2-amd64.iso | tail -1); echo $start
parted /dev/sdd mkpart primary $start $end
yes
ignore
fdisk -l
```
![06]({{ site.url }}assets/2018-12-16-kali-linux-live-USB-persistence/06.png)
![07]({{ site.url }}assets/2018-12-16-kali-linux-live-USB-persistence/07.png)

这样我们就创建了`/dev/sdd3`，然后我们用这个命令将其变为**ext3**格式。
```
mkfs.ext3 -L persistence /dev/sdd3
e2label /dev/sdd3 persistence
```
![08]({{ site.url }}assets/2018-12-16-kali-linux-live-USB-persistence/08.png)

通过以下命令创建挂载点，并写入配置文件。
```
mkdir -p /mnt/my_usb
mount /dev/sdd3 /mnt/my_usb
echo "/ union" > /mnt/my_usb/persistence.conf
umount /dev/sdd3
```

这样，一个Live USB Persistence模式的Kali Linux的启动盘就制作完成了。用该U盘重启并选择`Live USB Persistence`就可以开始玩耍了。

保存一些文件，试试是不是再次重启也生效。对了Kali Linux的默认账户密码是**root/toor**