---
layout:     post
title:      "工欲善其事必先利其器"
subtitle:   "工程师的推荐软件(Windows)"
date:       2020-04-11 12:00:00
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - 杂文
    - Windows
    - 技术相关
---
> free software和open source software中有很多带劲的软件。推荐走一波

我的“怪癖”，要么用买的软件，要么用免费软件，当然如果迫不得已的话，那啥都能用了😀。免费软件也可以细分两种，一种是**free software**免费使用，但是源代码不对外开放，可能一些高级功能会收费啥的。另一种是**open source software**就是源代码开源，免费使用。至于能不能用开源代码集成到我的产品中来售卖，就要看具体的开源协议了。下面会从几个纬度来介绍，我常用的软件。

## 小工具（体验为本，效率制胜）

- 截图工具
  1. snipaste，在同事FNN电脑上发现的，是聊天工具常见组件的加强版，有个牛逼的功能是可以讲截的图pin在页面上，用来做对比好用极了。[官网](https://www.snipaste.com/)
  2. ShareX，安装之后键盘上的*PrintScreen*突然变得高频起来了，牛逼之处在于可以长截图。推测是锁定窗体之后模拟进行滚动实现的，推测哈，不一定是。不过安装就完事儿了对吧。[GitHub主页](https://github.com/ShareX/ShareX)
  3. automatic-screenshotter，看名字就知道这是专门为“狠人”准备的工具。它的主要功能就是全自动截图，我是设置了每隔5s进行一次截图。由于我个人对记忆极其不信任，为了防止测试过程中的一些细节无法精准还原所以安装了个软件。[官网](https://www.donationcoder.com/software/mouser/popular-apps/automatic-screenshotter)
- 剪贴板工具——Ditto，虽然win10自带了云同步剪贴板，这款工具实在是太强了。貌似可以无线记录复制过的文本和图片（我怕把硬盘搞爆了，所以设置了上限，不过上限有点大——999999999条😁所以记得把缓存文件的位置改下，我的缓存文件有18G.......）。能记录图片就很牛逼了，还支持文本的检索，那找之前复制过的测试环境服务器密码简直就是分分钟。[官网](https://ditto-cp.sourceforge.io/)
- HOST切换工具——SwitchHosts，地球人都知道的快速切换本机Host文件的工具。[GitHub主页](https://github.com/oldj/SwitchHosts)
- 录屏工具——ScreenToGif，可以录制屏幕并转换为Gif动图，同时可以进行简单的编辑，增加字幕等。简直就是报bug神器，Jira上可以直接预览，聊天工具基本也支持直接预览。语言描述很麻烦的问题，一个录屏就可以轻松描述。[GitHub主页](https://github.com/NickeManarin/ScreenToGif)
- 文件管理——Everything，找文件特别方便，而且很快。[官网](https://www.voidtools.com/)
- 跨系统跨设备共享一套键鼠——Synergy，在局域网内可以跨系统共享一套键鼠，如果您有两个机器（如：Windows+Ubuntu），可以像连接扩展屏幕一样用一套键鼠来控制两个机器[官网](https://symless.com/synergy) [GitHub主页](https://github.com/symless/synergy-core)
- 快捷启动器——Wox，`被誉为 Alfred 的 Windows 版最佳替代品`，通过Alt+Space激活一个文本框，可以实现快捷查找文件、应用启动器、网页检索、词典等功能。依赖 `Everything`、`Python`。具体请看[GitHub主页](https://github.com/Wox-launcher/Wox)
- IOS投屏工具——Free Airplay Receiver for windows，实现了Airplay的接收端功能，不只有windows版，还有Linux版等，方便手机演示内容用。具体请看[GitHub主页](https://github.com/xfirefly/Airplay-SDK/tree/master/windows-receiver)
- 邮件格式转换工具（MSG↔EML），使用方法“Advanced → Import/Export → Convert MSG to EML”，详情参考[How to save a mail into an .eml-file with Outlook?](https://superuser.com/a/799994)。软件下载参考[GitHub_Release页](https://github.com/stephenegriffin/mfcmapi/releases/latest)，下载对应系统类型的EXE文件即可，如 `MFCMAPI.x64.exe.21.0.21127.03.zip`。

## 数据库

其实没有找到特别完美的数据库工具，目前手里有两款。

1. HeidiSQL，这个就很厉害了。ta不仅可以连接MySql，还可以连接MS SQL Server、SQLite等5种数据库。同时支持sql格式化等操作。只是在我这连接测试环境MySql数据库时，偶尔闪退🤦‍♂️。所以不是工作中的主力，而是平时使用的主力。[官网](https://www.heidisql.com/)
2. SQLyog，俗称小海豚。这是我平时工作的主力工具，由于使用的是开源版本，导致连格式化sql都做不到。好在，测试工作的话，平时常用的sql就那些，写一次以后就能一直用了。倒也没有太大影响。[GitHub主页](https://github.com/webyog/sqlyog-community)
3. MySQL Workbench。提供了Windows版本，我在Windows上没试过...[官网](https://dev.mysql.com/downloads/workbench/)
4. DBeaver。有个很厉害的伙伴在用，我没试用过。[官网](https://dbeaver.io/)
5. AnotherRedisDesktopManager，redis客户端，其实我没咋用过(⊙﹏⊙)。不过8.3K的Star，应该能挺好用吧。[GitHub主页](https://github.com/qishibo/AnotherRedisDesktopManager)

## SSH

SSH工具PuTTY就挺带劲了，但是比起MobaXterm或者XShell来，缺少连接管理，也不能很方便的记录用户名密码。以下两个工具都是基于PuTTY进行的扩展，所以要先安装Putty。

1. SuperPuTTY，支持了多窗口，连接可以借助文件夹以树状形式存储。并且可以支持保存密码。（以明文保存密码，其实有些不安全，但是测试环境的话就问题不大。同时明文的话后续也好找，不会忘了密码）但是不支持文件传输。追加一下密码的保存方式，因为本质还是用的PuTTY，所以其实是用PuTTY的命令行来保存密码。即在**Extra PuTTY Auguments**中填入`<b>`-pw&nbsp;&nbsp;liutianyu@!U`</b>`[GitHub主页](https://github.com/jimradford/superputty)
2. mRemoteNG，功能基本和SuperPuTTY相同，但是密码是以密文保存的。同时支持上传文件到远程服务器。[GitHub主页](https://github.com/mRemoteNG/mRemoteNG)
3. Tera Term，没有深度使用过，就是下来试了下。反正可以用就是了。[Tera Term官网](https://ttssh2.osdn.jp/index.html.en)

## SFTP/FTP

1. WinSCP，Windows平台的老牌免费FTP工具，支持FTP、SFTP、WebDAV等协议。[官网](https://winscp.net/eng/download.php)
2. FileZilla，提供客户端和服务端两款软件。客户端覆盖Windows、Linux、Mac OS，并支持FTP、FTPS、SFTP协议。服务端则只支持Windows平台，提供FTP、SFTP的支持。[官网](https://filezilla-project.org)

## 屏幕录制

Windows10 好像为了游戏直播还是啥所以具备了录屏功能，但是没咋研究。推荐的是下面这款。

1. EV录屏，有VIP版本，高级功能需要VIP，但是平时简单录个屏啥的，免费版本就足够了。[官网](https://www.ieway.cn/)
2. OBS Studio，同事LGX推荐的，还没有亲自体验，但是貌似可以按照窗口进行后台录制，同时还可以作为直播软件配合斗鱼等平台食用，感觉有点强。[GitHub主页](https://github.com/jp9000/obs)

## 思维导图

1. xmind，这个挺有名，但是现在的产品线搞得我很迷。之前PC端的XmindZEN是免费的，现在我看官网上又没有了。我目前是用Xmind的移动版画下思维导图，别的也没啥了。[官网](https://www.xmind.net/)
2. freemind，客户端覆盖Windows、Linux、Mac OS的思维导图工具，但是页面比较老，之前尝试寻找好用的思维导图工具的来写用例的使用用过。[官网](http://freemind.sourceforge.net/wiki/index.php/Main_Page)

## 文本编辑工具

1. Visual Studio Code，VS Code一生推。ta已经不是一个简单的编辑工具了，甚至可以算是一个IDE。同时大量的插件让ta可以做很多事情。最常用的就是文本内容对比、格式化XML/JSON/EDI。[GitHub主页](https://github.com/microsoft/vscode)
2. editplus，同事ZP推荐的，还没有亲自体验。[官网](https://www.editplus.com/)
3. Notepad++，同事LGX推荐的，还没有亲自体验。[官网](https://notepad-plus-plus.org/)
4. Typora专为markdown而生的文本编辑器，支持mermaid，用markdown来画图实在是太香了。[官网]（https://typora.io/）

## UML建模

1. JUDE，小巧实用，最后一个社区版是5.5.2。[下载链接]({{ site.url }}assets/2020/2020-04-11-software-4-work/JUDE-Community-5-5-2.zip)

## 系统工具

1. Rufus, a free and open source USB stick writing tool。Ubuntu官网推荐的制作U盘启动盘的工具。[官网](https://rufus.ie/)
2. Wireless Network Watcher，可以查看同一局域网下全部计算机或设备，会显示IP地址、MAC地址、制造网卡的公司。[官网](https://www.nirsoft.net/utils/wireless_network_watcher.html)。我下了一份做备份，[下载链接]({{ site.url }}assets/2020/2020-04-11-software-4-work/wnetwatcher.zip)

## 图片工具

1. digiKam，Professional Photo Management with the Power of Open Source。图片管理工具，没探索太多功能，我只用他来把jpeg转换成heif用。[官网](https://www.digikam.org/)

## Windows10小技巧

### “微软拼音输入法”输入时间戳

Windows 设置 ➡ 时间和语言 ➡ 语言 ➡ 中文(中华人民共和国) ➡ 选项 ➡ 微软拼音 ➡ 选项 ➡ 词库和自学习 ➡ 添加或编辑自定义短语 ➡ 添加

然后拼音和短语，短语提供两个如下范例：

```
%yyyy%-%MM%-%dd% %HH%:%mm%:%ss%
%yyyy%%MM%%dd%_%HH%%mm%%ss%
```

第一个输出格式样例为 `2022-01-05 12:31:09`。第二个输出的格式样例为 `20220105_123151`。

## 更新日志

- 2020年4月11日：初稿。
- 2020年7月27日：追加Wox和synergy
- 2020年9月2日：追加JUDE
- 2020年9月11日：追加AnotherRedisDesktopManager
- 2021年2月：追加MySQL Workbench、DBeaver
- 2021年6月：追加Free Airplay Receiver for windows、automatic-screenshotter
- 2021年9月：追加Rufus、Wireless Network Watcher
- 2022年1月：追加“微软拼音输入法”输入时间戳
