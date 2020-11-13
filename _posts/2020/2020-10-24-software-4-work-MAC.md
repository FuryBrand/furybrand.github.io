---
layout:     post
title:      "记从Windows办公迁移至MAC办公"
subtitle:   "MacOS软件推荐"
date:       2020-10-24 15:52:00
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - 杂文
    - macOS
    - 技术相关
---


> 由于一些特殊原因，告别了亲爱的Lenovo T490，开始用MacBook Pro（2019,10.15.7 (19H2)）了

## 适应新的机器

建议阅读[知乎上的这篇文章](https://zhuanlan.zhihu.com/p/83863239?from_voters_page=true)，首先对手上的新机器有所了解。作者的一个观点很好，用使用iPhone的角度去理解MAC，摒弃Windows的一些操作习惯。

效率控可以再看下官网提供的这些东西:
- [Mac 键盘快捷键](https://support.apple.com/zh-cn/HT201236)
- [Mac 上 Safari 浏览器中的键盘快捷键和手势](https://support.apple.com/zh-cn/guide/safari/cpsh003/mac)
- [在 Mac 上截屏或录制屏幕](https://support.apple.com/zh-cn/guide/mac-help/mh26782/mac)

## 一些常见的软件

有些软件下载下来后没有通过Mac的安全检查，比如`MySQLWorkbench`，此时需要如下路径进行允许`🍎 -> 系统偏好设置 -> 安全性与隐私`

#### Homebrew

一款MacOS上的包管理工具。[官网](https://brew.sh/)

安装命令，在终端中执行`$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`

好多软件都可以通过这个来安装，如果觉得安装别的软件时速度很慢，可以考虑网上搜一下换个源。

#### git

[官网](https://git-scm.com/download/mac)已经给出了安装方式`$ brew install git`。

#### Visual Studio Code

直接[官网](https://code.visualstudio.com/)选择MAC版本下载安装即可。

#### Python

直接[官网](https://www.python.org/ftp/python/3.9.0/python-3.9.0-macosx10.9.pkg)下载安装包安装。

#### MySQLWorkbench

MySQL的图形化客户端，虽然没那么好用，但是至少有啊😅

直接[官网](https://dev.mysql.com/downloads/workbench/)选择MAC版本下载安装即可。

#### FreeMind

免费开源的思维导图工具。20.11.03更新：FreeMind在macOS上的兼容性可以用非常糟糕来形容。于是找到了其替代品SciaReto。

直接[官网](http://freemind.sourceforge.net/wiki/index.php/Download)选择MAC版本下载安装即可。

#### SciaReto

免费开源的思维导图工具。

直接去github上取[最新的release](https://github.com/raydac/netbeans-mmd-plugin/releases)吧。

#### iTerm

直接[官网](https://www.iterm2.com/)下载安装包安装。

如何保存密码？先在任意位置创建一个文件（我在`~/.ssh/`中创建了一个`ssh_login`文件）用以保存登陆脚本，并赋予权限（我直接`chmod 777 ssh_login`了😅）。

![效果图]({{ site.url }}assets/2020/2020-10-24-software-4-work-MAC/Jietu20201024-163022.jpg)

下面是脚本文本，复制即用～

```ssh
#!/usr/bin/expect

set timeout 30
spawn ssh -p [lindex $argv 0] [lindex $argv 1]@[lindex $argv 2]
expect {
        "(yes/no)?"
        {send "yes\n";exp_continue}
        "password:"
        {send "[lindex $argv 3]\n"}
}
interact
```

然后在iTerm中进入`Command O -> Edit Profiles -> +`后按照下图配置即可。Send text at start中填写脚本路径及参数`~/.ssh/ssh_login 22 root 10.170.220.34 2FGP%czQ@1`

![效果图]({{ site.url }}assets/2020/2020-10-24-software-4-work-MAC/Jietu20201024-165248.jpg)

#### docker

直接[官网](https://www.docker.com/get-started)选择MAC版本下载安装即可。

#### Fiddler

没有经典版可以用，但是可以下载Fiddler Everywhere来用。访问[官网](https://www.telerik.com/download/fiddler-everywhere)输入邮箱，选好系统版本即可下载。

#### Postman

直接[官网](https://www.postman.com/downloads/)下载安装即可。

#### iShot

很好用的截图工具，可以直接通过快捷键`option a`来唤醒，标记完成后直接进入剪贴板。虽然拿到Windows上是人人都有的功能，但是对比了系统自带的截图工具，和腾讯推出的`截图`软件，这款iShot让我感动到哭。

从App Store中[下载](https://apps.apple.com/cn/app/ishot-%E6%88%AA%E5%9B%BE-%E5%BD%95%E5%B1%8F-2020%E5%85%A8%E6%96%B0%E9%AB%98%E5%BA%A6/id1485844094?mt=12)即可。

#### SwitchHosts!

直接[官网](https://github.com/oldj/SwitchHosts/releases/tag/v3.5.4)下载安装即可。

#### 网易MuMu

MacOS上的软件太少了，逼着我用移动端的软件😭

直接[官网](http://mumu.163.com/baidu/)选择MAC版本下载安装即可。

#### VirtualBox

为了防止有些软件只能在windows上使用，搞个虚拟机预备着。镜像正在下载，后面看看如何再来更新。

直接[官网](https://www.virtualbox.org/wiki/Downloads)选择MAC版本下载安装即可。Windows预览版的镜像[下载地址](https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewserver?wa=wsignin1.0)，发现一问题，貌似这东西需要有windows Insider计划的账号才行。。。。。。。

20.10.26更新：没有预览版账号也不要紧，可以去大名鼎鼎的[msdnitellyou](https://msdn.itellyou.cn/)上下载。不过由于下载地址是ed2k的链接，所以我们还需要用到同样大名鼎鼎的[迅雷](https://dl.xunlei.com/#mod02)。

下载好之后可以参考该[博文](https://www.cnblogs.com/andong2015/p/7688120.html)进行安装。

#### Folx

有免费版和付费的高级版，我这用的是免费版，其实目前就是挂着下windows的镜像。知乎上有人推荐就下来试试

直接[官网](https://mac.eltima.com/folx-download.html)下载安装即可。

#### Flycut

试过好几款Ditto的替代品，这个算是免费软件中最好的了吧（虽然和Ditto差了好多😭）。

直接[App Store](https://apps.apple.com/cn/app/flycut-clipboard-manager/id442160987?mt=12)中下载即可。

#### jdk

直接从[AdoptOpenJDK](https://adoptopenjdk.net/index.html?variant=openjdk8&jvmVariant=hotspot)上下载安装即可。

#### telnet

利用上面提到的`Homebrew`来安装。命令为：**brew install telnet**

#### Typora

Typora专为markdown而生的文本编辑器，支持mermaid，用markdown来画图实在是太香了。[官网]（https://typora.io/）

## 更新日志
- 2020年10月24日：初稿。
- 2020年10月：追加windows镜像下载链接和flycut。
- 2020年11月：追加telnet、SciaReto。