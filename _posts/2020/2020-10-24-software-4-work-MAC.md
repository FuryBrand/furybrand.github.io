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

如果想要**临时**取消`$ brew install XXX`时默认触发的升级操作的话，可以执行该命令`$ export HOMEBREW_NO_AUTO_UPDATE=true`。

```
Steve@ZBMAC-C657521M local % brew list
aom			fribidi			guile			libev			libsoxr			libxcb			node			python@3.9		tcl-tk			xz
bdw-gc			gdbm			harfbuzz		libevent		libtasn1		libxdmcp		opencore-amr		rav1e			telnet			zeromq
c-ares			gettext			icu4c			libffi			libtiff			libxext			openjpeg		readline		tesseract		zimg
cairo			giflib			jemalloc		libidn2			libtool			libxrender		openssl@1.1		rtmpdump		theora
dav1d			git			jmeter			libogg			libunistring		little-cms2		opus			rubberband		unbound
ffmpeg			glib			jpeg			libpng			libvidstab		lzo			p11-kit			sdl2			webp
flac			gmp			lame			libpthread-stubs	libvorbis		mpdecimal		pcre			snappy			x264
fontconfig		gnutls			leptonica		libsamplerate		libvpx			mysql@5.7		pcre2			speex			x265
freetype		gobject-introspection	libass			libsndfile		libx11			nettle			pixman			sqlite			xorgproto
frei0r			graphite2		libbluray		libsodium		libxau			nghttp2			pkg-config		srt			xvid
another-redis-desktop-manager                                                                                                  picgo
Steve@ZBMAC-C657521M local % brew list jmeter
/usr/local/Cellar/jmeter/5.3/bin/jmeter
/usr/local/Cellar/jmeter/5.3/libexec/backups/ (20 files)
/usr/local/Cellar/jmeter/5.3/libexec/bin/ (184 files)
/usr/local/Cellar/jmeter/5.3/libexec/docs/ (2083 files)
/usr/local/Cellar/jmeter/5.3/libexec/extras/ (20 files)
/usr/local/Cellar/jmeter/5.3/libexec/lib/ (114 files)
/usr/local/Cellar/jmeter/5.3/libexec/licenses/ (143 files)
/usr/local/Cellar/jmeter/5.3/libexec/printable_docs/ (72 files)
```

- `brew upgrade jmeter`升级jmeter

#### git

[官网](https://git-scm.com/download/mac)已经给出了安装方式`$ brew install git`。

#### Visual Studio Code

直接[官网](https://code.visualstudio.com/)选择MAC版本下载安装即可。

#### Python

直接[官网](https://www.python.org/ftp/python/3.9.0/python-3.9.0-macosx10.9.pkg)下载安装包安装。

安装pip，`$ python3 -m pip install --upgrade pip setuptools wheel`

#### MySQLWorkbench

MySQL的图形化客户端，虽然没那么好用，但是至少有啊😅

直接[官网](https://dev.mysql.com/downloads/workbench/)选择MAC版本下载安装即可。

#### FreeMind

免费开源的思维导图工具。20.11.03更新：FreeMind在macOS上的兼容性可以用非常糟糕来形容。于是找到了其替代品SciaReto。

直接[官网](http://freemind.sourceforge.net/wiki/index.php/Download)选择MAC版本下载安装即可。

#### SciaReto

免费开源的思维导图工具。

直接去github上取[最新的release](https://github.com/raydac/netbeans-mmd-plugin/releases)吧。

#### DesktopNaotu

基于百度FEX团队的开源产品[KityMinder](https://github.com/fex-team/kityminder-core)的本地离线运行的版本。

直接去github上取[最新的release](https://github.com/NaoTu/DesktopNaotu/releases)吧。

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

一个小坑：如果在执行的过程中出现了类似`zsh: event not found:_+`的报错，那么可能是密码中包含了shell的关键字，比如我的是**2FGP%c!_+**，此时需要使用escape character “\”，即将命令写为`~/.ssh/ssh_login 22 root 10.170.220.34 2FGP%c\!_+`

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

下载好之后可以参考该[博文](https://www.cnblogs.com/andong2015/p/7688120.html)进行安装。如果想共享宿主机的文件夹，需要进入`菜单栏 Devices ->Shared Folders ->Shared Folders Settings...`并进行如设置。

![设置图]({{ site.url }}assets/2020/2020-10-24-software-4-work-MAC/iShot2021-02-09.png)

关闭Windows的自动更新：Windwos+R，输入“gpedit.msc”回车，在本地注册表编辑器中依次打开：计算机配置-管理模板-Windows组件-windows 更新，在右侧将“配置自动更新”和“允许自动更新立即安装”的状态改为“已禁用”，重启电脑，查看一下。参考[永久关闭win10自动更新
](https://answers.microsoft.com/zh-hans/windows/forum/all/%E6%B0%B8%E4%B9%85%E5%85%B3%E9%97%ADwin10%E8%87%AA/29ebb211-8189-4c96-abab-31a851cc75a9)

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

#### LICEcap

LICEcap是轻量级的gif录制软件，功能上没有Windows平台上独占的ScreenToGif多，但是胜在跨平台。[官网]（https://www.cockos.com/licecap/）、[github主页]（https://github.com/justinfrankel/licecap）

#### LibreOffice

已经好几年没用过LibreOffice了，界面让我感到惊艳。[官网]（https://www.cockos.com/licecap/）

#### The Unarchiver

可以解压rar格式的免费软件。[App Store](https://apps.apple.com/us/app/the-unarchiver/id425424353?mt=12)上下载即可。

#### JMeter

利用上面提到的`Homebrew`来安装。命令为：**brew install jmeter**。相关说明[参考](https://formulae.brew.sh/formula/jmeter)

响应结果的中文若显示为乱码（不是一坨横线）的，需要在`/usr/local/Cellar/jmeter/5.0/libexec/bin`中的`jmeter.properties`文件进行如下设置`sampleresult.default.encoding=UTF-8`

如果中文显示为一坨横线，则是语言与外观不兼容导致。处理方式为`JMeter->Options->Look and Feel->Metal`

#### MySQL

利用上面提到的`Homebrew`来安装。5.7版本的安装命令为：**brew install mysql@5.7**。下面记录下安装完成之后的相关信息。

```shell
==> Installing dependencies for mysql@5.7: openssl@1.1
==> Installing mysql@5.7 dependency: openssl@1.1
==> Pouring openssl@1.1-1.1.1i.catalina.bottle.tar.gz
==> Caveats
A CA file has been bootstrapped using certificates from the system
keychain. To add additional certificates, place .pem files in
  /usr/local/etc/openssl@1.1/certs

and run
  /usr/local/opt/openssl@1.1/bin/c_rehash

openssl@1.1 is keg-only, which means it was not symlinked into /usr/local,
because macOS provides LibreSSL.

If you need to have openssl@1.1 first in your PATH run:
  echo 'export PATH="/usr/local/opt/openssl@1.1/bin:$PATH"' >> ~/.zshrc

For compilers to find openssl@1.1 you may need to set:
  export LDFLAGS="-L/usr/local/opt/openssl@1.1/lib"
  export CPPFLAGS="-I/usr/local/opt/openssl@1.1/include"

==> Summary
🍺  /usr/local/Cellar/openssl@1.1/1.1.1i: 8,067 files, 18.5MB
==> Installing mysql@5.7
==> Pouring mysql@5.7-5.7.32.catalina.bottle.2.tar.gz
==> /usr/local/Cellar/mysql@5.7/5.7.32/bin/mysqld --initialize-insecure --use
==> Caveats
We've installed your MySQL database without a root password. To secure it run:
    mysql_secure_installation

MySQL is configured to only allow connections from localhost by default

To connect run:
    mysql -uroot

mysql@5.7 is keg-only, which means it was not symlinked into /usr/local,
because this is an alternate version of another formula.

If you need to have mysql@5.7 first in your PATH run:
  echo 'export PATH="/usr/local/opt/mysql@5.7/bin:$PATH"' >> ~/.zshrc

For compilers to find mysql@5.7 you may need to set:
  export LDFLAGS="-L/usr/local/opt/mysql@5.7/lib"
  export CPPFLAGS="-I/usr/local/opt/mysql@5.7/include"


To have launchd start mysql@5.7 now and restart at login:
  brew services start mysql@5.7
Or, if you don't want/need a background service you can just run:
  /usr/local/opt/mysql@5.7/bin/mysql.server start
==> Summary
🍺  /usr/local/Cellar/mysql@5.7/5.7.32: 319 files, 234.4MB
==> Caveats
==> openssl@1.1
A CA file has been bootstrapped using certificates from the system
keychain. To add additional certificates, place .pem files in
  /usr/local/etc/openssl@1.1/certs

and run
  /usr/local/opt/openssl@1.1/bin/c_rehash

openssl@1.1 is keg-only, which means it was not symlinked into /usr/local,
because macOS provides LibreSSL.

If you need to have openssl@1.1 first in your PATH run:
  echo 'export PATH="/usr/local/opt/openssl@1.1/bin:$PATH"' >> ~/.zshrc

For compilers to find openssl@1.1 you may need to set:
  export LDFLAGS="-L/usr/local/opt/openssl@1.1/lib"
  export CPPFLAGS="-I/usr/local/opt/openssl@1.1/include"

==> mysql@5.7
We've installed your MySQL database without a root password. To secure it run:
    mysql_secure_installation

MySQL is configured to only allow connections from localhost by default

To connect run:
    mysql -uroot

mysql@5.7 is keg-only, which means it was not symlinked into /usr/local,
because this is an alternate version of another formula.

If you need to have mysql@5.7 first in your PATH run:
  echo 'export PATH="/usr/local/opt/mysql@5.7/bin:$PATH"' >> ~/.zshrc

For compilers to find mysql@5.7 you may need to set:
  export LDFLAGS="-L/usr/local/opt/mysql@5.7/lib"
  export CPPFLAGS="-I/usr/local/opt/mysql@5.7/include"


To have launchd start mysql@5.7 now and restart at login:
  brew services start mysql@5.7
Or, if you don't want/need a background service you can just run:
  /usr/local/opt/mysql@5.7/bin/mysql.server start
```

#### npm

利用上面提到的`Homebrew`来安装。安装命令为：**brew install npm**。

#### drawio-desktop

流程图的好手，但是貌似易用性较之Microsoft Viso还是差点意思，不过可以打开vsdx也算是挺牛了。drawio-desktop是diagrams.net的桌面版，直接去[github release地址](https://github.com/jgraph/drawio-desktop/releases/)下载吧。

#### Scroll-Reverser

Mac的触控板和的方向非常诡异（手往左上移动，图片也往左上移动😓我想让ta往又下移动啊），在设置里反转之后，鼠标的滚轮居然也反了，干～.～。通过Scroll-Reverser完美解决。[Github地址](https://github.com/pilotmoon/Scroll-Reverser)、[官网地址](https://pilotmoon.com/scrollreverser/)

#### keka

7-zip官网上推荐的工具，我就用过给压缩包增加密码这样的简单功能。[官网](https://www.keka.io/en/)。[下载链接](https://d.keka.io/)

#### 视频下载

YouTube上的视频下载需要使用`youtube-dl`（[官网](http://ytdl-org.github.io/youtube-dl/index.html)[GitHub工程地址](https://github.com/ytdl-org/youtube-dl)）和`FFmpeg`（[官网](https://ffmpeg.org/)）。

`youtube-dl`是使用了官方手册指导进行安装（注意youtube-dl还依赖python）。
```
sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
```

`FFmpeg`是使用了`Homebrew`来安装。安装命令为：**brew install ffmpeg**

简单的使用手册：
```
# 查看该视频的各种格式
liutianyu@ZMC Downloads % youtube-dl --list-formats https://www.youtube.com/watch\?v=zFQV0kw5saM
[youtube] zFQV0kw5saM: Downloading webpage
[info] Available formats for zFQV0kw5saM:
format code  extension  resolution note
249          webm       audio only tiny   52k , webm_dash container, opus @ 52k (48000Hz), 4.44MiB
250          webm       audio only tiny   69k , webm_dash container, opus @ 69k (48000Hz), 5.96MiB
140          m4a        audio only tiny  129k , m4a_dash container, mp4a.40.2@129k (44100Hz), 11.06MiB
251          webm       audio only tiny  137k , webm_dash container, opus @137k (48000Hz), 11.71MiB
160          mp4        256x144    144p   53k , mp4_dash container, avc1.4d400c@  53k, 30fps, video only, 4.58MiB
278          webm       256x144    144p   84k , webm_dash container, vp9@  84k, 30fps, video only, 7.23MiB
133          mp4        426x240    240p  120k , mp4_dash container, avc1.4d4015@ 120k, 30fps, video only, 10.31MiB
242          webm       426x240    240p  170k , webm_dash container, vp9@ 170k, 30fps, video only, 14.57MiB
134          mp4        640x360    360p  226k , mp4_dash container, avc1.4d401e@ 226k, 30fps, video only, 19.35MiB
243          webm       640x360    360p  365k , webm_dash container, vp9@ 365k, 30fps, video only, 31.23MiB
135          mp4        854x480    480p  351k , mp4_dash container, avc1.4d401f@ 351k, 30fps, video only, 30.07MiB
244          webm       854x480    480p  650k , webm_dash container, vp9@ 650k, 30fps, video only, 55.55MiB
136          mp4        1280x720   720p 1205k , mp4_dash container, avc1.4d401f@1205k, 30fps, video only, 103.00MiB
247          webm       1280x720   720p 1320k , webm_dash container, vp9@1320k, 30fps, video only, 112.80MiB
18           mp4        640x360    360p  650k , avc1.42001E, 30fps, mp4a.40.2 (44100Hz), 55.61MiB
22           mp4        1280x720   720p 1338k , avc1.64001F, 30fps, mp4a.40.2 (44100Hz) (best)
# 下载所有语言的字幕、并将视频进行合并
liutianyu@ZMC Downloads % youtube-dl --write-sub --all-subs --write-auto-sub -f 136+140 https://www.youtube.com/watch\?v=zFQV0kw5saM
[youtube] zFQV0kw5saM: Downloading webpage
[download] Destination: 【これで決まり！】新井恵理那のふるさとの味をご紹介！　恵理那とラピスの部屋#17-zFQV0kw5saM.f136.mp4
[download] 100% of 103.00MiB in 00:40
[download] Destination: 【これで決まり！】新井恵理那のふるさとの味をご紹介！　恵理那とラピスの部屋#17-zFQV0kw5saM.f140.m4a
[download] 100% of 11.06MiB in 00:04
[ffmpeg] Merging formats into "【これで決まり！】新井恵理那のふるさとの味をご紹介！　恵理那とラピスの部屋#17-zFQV0kw5saM.mp4"
Deleting original file 【これで決まり！】新井恵理那のふるさとの味をご紹介！　恵理那とラピスの部屋#17-zFQV0kw5saM.f136.mp4 (pass -k to keep)
Deleting original file 【これで決まり！】新井恵理那のふるさとの味をご紹介！　恵理那とラピスの部屋#17-zFQV0kw5saM.f140.m4a (pass -k to keep)
```

更多的使用方式[【备份】youtube-dl使用介绍](https://www.jianshu.com/p/6bae57859325)


## 更新日志
- 2020年10月24日：初稿。
- 2020年10月：追加windows镜像下载链接和flycut。
- 2020年11月：追加telnet、SciaReto、Typora、LICEcap、DesktopNaotu、LibreOffice。
- 2020年12月：追加The Unarchiver、JMeter、npm。
- 2021年1月：追加drawio-desktop、Scroll-Reverser。
- 2021年1月：追加视频下载。
- 2021年4月：追加keka。