---
layout: post
title:  "我的Linux常用命令（持续更新）"
date:   2018-07-11 22:46:49 +0800
categories: jekyll update
---
最近在通过《鸟哥的Linux私房菜》系统得学习linux。可是工作中还是要用Linux的，有些命令啥的就是现学现用，这个笔记就是记录这个的。

### 常用

| 命令 | 简介 | 备注
| - | - | -
|pwd |显示当前路径 |
|mv |重命名或移动 |
|cp |复制 |-r 递归将子文件全部复制 
|mkdir |创建文件夹 | 
|/sbin/ifconfig |获取ip地址 | 
|zip -r mydata.zip mydata |把当前目录下面的mydata目录压缩为mydata.zip| 
|unzip |解压zip文件。unzip xx.zip | 
|tar |将文件压缩成tar文件| 
|df -h |查看磁盘使用量 | 
|rz/sz |利用ssh协议在Xshell上传输文件 | 
|netstat |-a:将目前系统上所有的链接、监听、Socket数据都列出来<br>-t:列出tcp网络数据包的数据<br>-u:列出udp网络数据包的数据<br>-n：不列出进程的服务名称，以端口号来显示<br>-l：列出目前正在网络监听listen的服务<br>-p：列出该网络服务的进程 PID |列出目前系统上已在监听的网络连接及其PID：netstat –tlnp<br>netstat -tunlp &#124; grep 8005 | 
|查询linux系统的版本 |查看电脑和操作系统的信息：uname -a<br>查询内核版本：cat /proc/version<br>查询发行版本：cat /etc/issue<br>查询发行版本：lsb_release -a(适用于所有的linux，包括Redhat、SuSE、Debian等发行版，但是在debian下要安装lsb) | 
|ps -ef&#124;grep java |查找“java”相关的进程信息 | 
|jar -xvf game.war |解压game.war包到当前目录 | 
|which python |查找python的安装路径 | 
|alias vi |通过alias来查找别名对应的命令 | 
|echo > catalina.out  |清空日志文件 | 
|find /export -size +1000k |查找指定目录下，大小大于1000k的文件 | 
|find /export/ -name '*log*' |指定目录下，模糊查找 | 
|find的两个参数一起用来清理日志| for i in \`find /export/Domains -name '*.log' -size +10000k\`; do echo > $i; done | 
|rm |慎用，删除文件 | 
|rm -rf /var/log/ |完全删除该文件夹 | 
|chmod -R 777 |将文件夹以及子文件夹的权限都设置为777，R不能小写。 chmod -R 777 download | 
|date |获取系统当前时间 | 
|date -s "2018-2-6 14:25:07" |设置系统时间，注：admin可能没有权限 | 
|history |可以打印出之前所输入过的命令，然后用!123就可以指定第123号命令 | 

### 账户，修改密码相关

| 命令 | 简介 | 备注 
| - | - | - 
|id |查看当前登录用户的的信息 |
|passwd admin |修改admin用户的密码，如果当前用户是root用户的话，直接输入passwd即可 |

### 压缩包 

| 命令 | 简介 | 备注 
| - | - | - 
|tar -cvjpf etc.tar.bz2 ./ngin |打包 |
|tar -xvjf　etc.tar.bz2 |解压缩 |

### Nginx

| 命令 | 简介 | 备注 
| - | - | - 
|/export/servers/nginx/sbin/nginx -s reload |重启 |
|/export/servers/nginx/sbin/nginx |启动 |
|/export/servers/nginx/sbin/nginx -s stop |关闭 |

### less

| 命令 | 简介 | 备注 
| - | - | - 
|less |按页查看文件内容，同时具有向上或向下的查询功能 |
|less xix.sh |进入less程序。/字符串，为向下查找。?字符串，为向上查找。 |
|ll &#124; less |针对文件夹内文件很多的情况，这样就可以显示全了 |

### 查看系统资源占用 [鸣谢](https://www.cnblogs.com/chengJAVA/p/6115061.html)

| 命令 | 简介 | 备注 
| - | - | - 
|free |总体内存占用的查看 | 1.默认按kb显示，free -m来用mb表示<br>2.Mem行，total=used+free，其中buffers和cached虽然计算在used内， 但其实为可用内存。<br>3.下一行是刨除buffers和cache的结果，是真实的可用内存。<br>Swap：内存交换区的使用情况。| 
|ps auxw &#124; head -1;ps auxw&#124;sort -rn -k4&#124;head -5 |查看内存占用前五的进程 | 
|ps auxw&#124;head -1;ps auxw&#124;sort -rn -k3&#124;head -5 |查看CPU占用前五的进程 | 
|top |查看系统整体的负载情况 | 


### SCP
scp是secure copy的简写，用于在Linux下进行远程拷贝文件的命令。本地←→远程

| 命令 | 简介 | 备注 
| - | - | - 
|scp -P 2181 /etc/hosts root@10.182.74.205:/etc/ | 将本机的host文件通过2181端口以root权限复制到指定机器的/etc/目录下 |