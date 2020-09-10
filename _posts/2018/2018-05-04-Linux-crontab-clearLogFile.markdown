---
layout: post
title:  "Linux-利用crontab定时清理日志"
subtitle:   ""
date:   2018-05-04
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    false
tags:
    - Linux
    - 技术相关
---
这篇[博文](https://www.cnblogs.com/zoulongbin/p/6187238.html)和这篇[博文](https://github.com/ice7mayu/tutorial/blob/master/doc/crontab.md)对crontab有较为详细的介绍。如果日后链接失效了，可以email我。
这个[web版的时间合法性校验工具](https://crontab.guru/)特别好用。

接下来详细介绍一下步骤（没考虑重启和安装的情况）：

# 01.在/home/admin/timedTask下新建[clearLog.sh]({{ site.url }}assets/2018/2018-05-04-Linux-crontab-clearLogFile/clearLog.sh)
该脚本就是未来要定时执行的。

# 02.修改文件的执行权限
`chmod +x clearLog.sh`

# 03.设置定时任务
输入命令`crontab -e`后进入编辑模式。

在最下面添加定时任务`1 1 * * * sh /home/admin/timedTask/clearLog.sh`

# 04.重启crontab服务
`service crond restart`

(好像定时任务在添加好之后无需重启crontab服务，这个有待确认，先记下)