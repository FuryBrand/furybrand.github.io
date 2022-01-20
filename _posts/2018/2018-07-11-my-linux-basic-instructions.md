---
layout: post
title:  "我的Linux常用命令（持续更新）"
date:   2018-07-11 22:46:49
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - Linux
---

最近在通过《鸟哥的Linux私房菜》系统得学习linux。可是工作中还是要用Linux的，有些命令啥的就是现学现用，这个笔记就是记录这个的。

## 常规

| 命令 | 简介 | 备注
| - | - | -
|pwd |显示当前路径 |
|mv |重命名或移动 | -f 强制移动，若有重名文件直接覆盖
|cp |复制（文件名支持通配符） |-r 递归将子文件全部复制
|mkdir |创建文件夹 | -p 递归创建所有需要的目录
|/sbin/ifconfig |获取ip地址 | 
|df -h |以磁盘分区为单位查看磁盘使用量 | 
|du -sh ./ |获取当前目录的大小 |
|du -h ./ |获取当前目录的下所有文件夹的大小（含子文件夹） | 
|rz/sz |利用ssh协议在Xshell上传输文件 | 
|netstat |-a:将目前系统上所有的链接、监听、Socket数据都列出来<br>-t:列出tcp网络数据包的数据<br>-u:列出udp网络数据包的数据<br>-n：不列出进程的服务名称，以端口号来显示<br>-l：列出目前正在网络监听listen的服务<br>-p：列出该网络服务的进程 PID |列出目前系统上已在监听的网络连接及其PID：netstat –tlnp <br> netstat -tunlp &#124; grep 8005 | 
|查询linux系统的版本 |查看电脑和操作系统的信息：uname -a<br>查询内核版本：cat /proc/version<br>查询发行版本：cat /etc/issue<br>查询发行版本：lsb_release -a(适用于所有的linux，包括Redhat、SuSE、Debian等发行版，但是在debian下要安装lsb) | 
|ps -ef&#124;grep java |查找“java”相关的进程信息 | 
|ps -ef &#124;grep nginx &#124;awk '{print $2}'&#124;xargs kill -9 |杀死nginx相关的所有进程 | 
|grep -r xixi /home | 显示/home目录下的文件(包含子目录)包含xixi的行（去掉-r则不查子目录） | 
|jar -xvf game.war |解压game.war包到当前目录 | 
|which python |查找python的安装路径 | 
|alias vi |通过alias来查找别名对应的命令 | 
|echo > catalina.out  |清空日志文件 | 
|find /export -size +1000k |查找指定目录下（默认递归），大小大于1000k的文件 | 
|find /export/ -name 'log' |指定目录下（默认递归），查找名为log的文件，此时支持通配符 | 
|find的两个参数一起用来清理日志| for i in "find /export/Domains -name '*.log' -size +10000k"; do echo > $i; done | 忘了是不是这么写的了，是双引号包裹的吗？懵逼了
|rm |慎用，删除文件 | 
|rm -rf /var/log/ |完全删除该文件夹 | 
|chmod -R 777 |将文件夹以及子文件夹的权限都设置为777，R不能小写。 chmod -R 777 download | 
|date |获取系统当前时间 | 
|date -s "2018-2-6 14:25:07" |设置系统时间，注：admin可能没有权限 | 
|history |可以打印出之前所输入过的命令，然后用!123就可以指定第123号命令 | 
|truncate |将文件变为指定大小，可用于创建测试用的垃圾文件，或用于清理日志 | find ./ -name '*.out' &#124; xargs truncate -s 0 |
|yum -y install |centos下安装软件 |yum -y install git 
|ln -s /export/logs/xixixi/ logs |在当前目录创建一个软链接logs关联指定路径
| \Enter | 将超长的命令转为多行，注意“\”和回车之间没有空格等


## 账户，修改密码相关

| 命令 | 简介 | 备注 
| - | - | - 
|id |查看当前登录用户的的信息 |
|passwd admin |修改admin用户的密码，如果当前用户是root用户的话，直接输入passwd即可 |
|echo "123" &#124; passwd &#150;&#150;stdin root |非常方便快捷的修改密码的方式。 |缺点是别人可能用history来获取密码，同时密码中不能包含单引号和双引号。并且某些发行版不提供&#150;&#150;stdin这个参数。
|w |查看当前用户 |
|who |命令查看主机上的用户 |
|whoami |查看当前登录的用户 |
|lastlog |登录日志 |
|su |用户切换 |su rootmima 切换root身份<br>su -rootmima 切换root身份及shell环境<br>su admin 切换admin用户

## 压缩包 

| 命令 | 简介 | 备注 
| - | - | - 
|tar -czvf test.tar.gz a |压缩 a.c文件为test.tar.gz |
|tar -xzvf test.tar.gz |解压缩 |
|zip -r mydata.zip mydata |把当前目录下面的mydata目录压缩为mydata.zip| 
|unzip |解压zip文件。unzip xx.zip | 

## 裁切字符串

```
myvar="boobar";
${myvar:3}   #输出bar
${myvar:3:2}    #输出ba
${myvar: -4}    #输出obar 注：中间的空格是必须的
${variable#word}    #从字符串开头使用非贪婪模式匹配
phone="666-657-2657"
${phone#*-}    #输出657-2657
${variable##word}    #从字符串开头使用贪婪模式匹配
${phone##*-}    #输出2657
${variable%word}    #从字符串结尾使用非贪婪模式匹配
${phone%-*}    #输出666-657
${variable%%word}    #从字符串结尾使用贪婪模式匹配
${phone%%-*}    #输出666
```

## Nginx

| 命令 | 简介 | 备注 
| - | - | - 
|/export/servers/nginx/sbin/nginx -s reload |重启 |
|/export/servers/nginx/sbin/nginx |启动 |
|/export/servers/nginx/sbin/nginx -s stop |关闭 |

## less

| 命令 | 简介 | 备注 
| - | - | - 
|less |按页查看文件内容，同时具有向上或向下的查询功能 |
|less xix.sh |进入less程序。/字符串，为向下查找。?字符串，为向上查找。 |
|ll &#124; less |针对文件夹内文件很多的情况，这样就可以显示全了 |

## SCP
scp是secure copy的简写，用于在Linux下进行远程拷贝文件的命令。本地←→远程双向拷贝。前一个路径为源文件，后一个路径为目标文件

| 命令 | 简介 | 备注 
| - | - | - 
|scp -P 2181 /etc/hosts root@10.182.74.205:/etc/ | 将本机的host文件通过2181端口以root权限复制到指定机器的/etc/目录下 |
|scp -P 2181 root@10.182.74.205:/etc/hosts /root | 将远程服务器的host文件通过2181端口复制本机/root目录下 |
|scp -r -P 2181 root@10.182.74.205:/root /root | 将远程服务器/root下的所有文件及文件夹通过2181端口复制到本机/root目录下 |

## lrzsz
[lrzsz官网](http://freecode.com/projects/lrzsz/)<br>
lrzsz是一个unix通信套件提供的X，Y，和ZModem文件传输协议。<br>
在centos中安装`yum install lrzsz`。<br>
如果服务器不能连接外网的话，就通过该[地址](http://mirror.centos.org/centos/6/os/x86_64/Packages/lrzsz-0.12.20-27.1.el6.x86_64.rpm)下载后通过`yum install lrzsz-0.12.20-27.1.el6.x86_64.rpm`来进行安装。

| 命令 | 简介 | 备注 
| - | - | - 
| sz /home/admin/log1.log  | 将log文件从服务器下载到本机 |
| rz | 页面弹出文件选择的页面，可以上传文件

## vim

~~按道理，vim应该抽空做专题的，不过先暂时做个记录吧。~~拒绝重复造轮子，需要学习vim的朋友，直接去[鸟站](https://linux.vbird.org/linux_basic/centos7/0310vi.php)把`第九章、vim 程式編輯器`看完，就从入门到精通了。当然也可以去vim的[官网](https://www.vim.org/docs.php)上找到一些有用的资料。我这里只是记录下我的笔记。

vim有12种编辑模式，其中6种是basic modes。Normal mode、Visual mode、Select mode、Insert mode、Cmdline mode、Ex mode

```mermaid!
graph LR
	A[Normal mode] -->|i,I,o,O,a,A,r,R| B[Insert mode]
	B -- ESC --> A
	A -->|:/?| C[Cmdline mode]
	C -- ESC --> A
```

#### Normal mode

光标移动，复制粘贴，批量删除等

| 命令 | 功能 
| - | - 
| h,j,k,l | 移动光标⬅️,⬇️,⬆️,➡️
| 数字 hjkl方向键 | 向指定方向移动一定步数
| Ctrl f | 向下翻页
| Ctrl b | 向上翻页
| 数字 space | 向右步进指定数字的步数
| 0 或 Home | 移动到该行最前
| $ 或 End | 移动到该行最后
| G | 移动到这个文件的最后一行
| 数字 G | 移动到这个文件的第“数字”行
| x | 等同于delete
| X | 等同于backspace
| dd | 删除光标所在行
| d1G | 删除光标所在行至第一行的所有数据
| dG | 删除从光标所在行到最后一行的所有数据
| yy | 复制光标所在行
| 数字 yy | 复制光标所在的及向下的“数字”行
| p 或 P | 粘贴
| u | 撤销（等同于Microsoft Office中的Ctrl z）
| Ctrl r | 恢复撤销（等同于Microsoft Office中的Ctrl y）


#### Cmdline mode

搜索替换

| 命令 | 功能 
| - | - 
| /word | 向下查找“word”字符串
| ?word | 向上查找“word”字符串
| n | 继续执行上一次的查找
| N | 反向执行上一次的查找
| :10,15s/word1/word2/g | 在10至15行中查找“word1”并将其替换为“word2”
| :1,$s/word1/word2/gc | 全局查找“word1”并将其替换为“word2”
| :1,$s/word1/word2/g | 全局查找“word1”并将其替换为“word2”，但是每一次替换前都需要确认。

环境更改

| 命令 | 功能 
| - | - 
| :set nu | 显示行号
| :set nonu | 取消显示行号
| :syntax on | 语法高亮开
| :syntax off | 语法高亮关

文件保存等

| 命令 | 功能 
| - | - 
| :w | 保存
| :w! | 强制保存
| :q | 退出
| :q! | 强制退出
| :wq | 保存并推出
| :wfile2 | 将文件另存为“file2”
| :rfile | 将文件"file"中的内容追加到目前光标所在位置的后面
| :! ls /home | 暂时离开当前编辑页并执行一个linux命令

多文件编辑

| 命令 | 功能 
| - | - 
| :files | 列出目前vim打开的所有文件
| :n | 编辑下一个文件
| :N | 编辑上一个文件

多窗口编辑

| 命令 | 功能 
| - | - 
| :sp | 当前文件多窗口显示
| :sp /etc/hosts | 在新窗口中打开新文件
| ctrl w j或k | 光标焦点在上下窗口中移动，注意ctrl和w放开后再按方向键
| ctrl w q | 结束当前窗口


#### Visual mode、Select mode

| 命令 | 功能 
| - | - 
| v | 字符选择
| V | 行选择
| Ctrl v| 块选择
| y | 将被选择部分复制
| d | 将被选择部分删除

## job control

| 命令 | 功能 
| - | - 
| ls -lh & | &用以将当前命令放到后台执行，注意stdout和stderr的重定向
| Ctrl z | 将程序暂停
| Ctrl c | 将程序强行停止
| jobs -l | 查看后台的工作状态
| fg %1 | 将后台中的第一个任务拿到前台来执行
| bg %2 | 将后台暂停的第2个任务变为后台执行 


## 查看系统资源占用相关命令
[鸣谢1](https://www.cnblogs.com/chengJAVA/p/6115061.html)
[鸣谢2](https://www.cnblogs.com/x123811/p/7488167.html)

| 命令 | 简介 | 备注 
| - | - | - 
|free |总体内存占用的查看 | 1.默认按kb显示，free -m来用mb表示<br>2.Mem行，total=used+free，其中buffers和cached虽然计算在used内， 但其实为可用内存。<br>3.下一行是刨除buffers和cache的结果，是真实的可用内存。<br>Swap：内存交换区的使用情况。| 
|ps auxw &#124; head -1;ps auxw&#124;sort -rn -k4&#124;head -5 |查看内存占用前五的进程 | 
|ps auxw&#124;head -1;ps auxw&#124;sort -rn -k3&#124;head -5 |查看CPU占用前五的进程 | 
|top |查看系统整体的负载情况 | 
|ps -ef &#124; grep xixi &#124; grep -v 'grep' &#124; awk '{print $2}' |输出xixi相关的进程的PID |可以配合for循环加kill -9就清理调相关的进程

#### 查看CPU信息

```shell
# 总核数 = 物理CPU个数 X 每颗物理CPU的核数 
# 总逻辑CPU数 = 物理CPU个数 X 每颗物理CPU的核数 X 超线程数

# 查看物理CPU个数
cat /proc/cpuinfo| grep "physical id"| sort| uniq| wc -l

# 查看每个物理CPU中core的个数(即核数)
cat /proc/cpuinfo| grep "cpu cores"| uniq

# 查看逻辑CPU的个数
cat /proc/cpuinfo| grep "processor"| wc -l
```

## CentOS7的默认防火墙firewall

```shell
# 查看firewall服务状态
$ systemctl status firewalld
# 查看firewall的状态
$ firewall-cmd --state
# 启动firewalld.service服务
$ service firewalld start
Redirecting to /bin/systemctl start mysqld.service
# 重启firewalld.service服务
$ service firewalld restart
Redirecting to /bin/systemctl restart mysqld.service
# 关闭firewalld.service服务
$ service firewalld stop
Redirecting to /bin/systemctl stop mysqld.service
# 查看防火墙规则
$ firewall-cmd --list-all
# 查询端口是否开放
$ firewall-cmd --query-port=8080/tcp
# 开放80端口
$ firewall-cmd --permanent --add-port=80/tcp
# 移除端口
$ firewall-cmd --permanent --remove-port=8080/tcp
# 重启防火墙(修改配置后要重启防火墙)
$ firewall-cmd --reload
```

## 批量解压文件到压缩包文件名的文件夹中

```
for i in `ls /data/app/mobile/lib`
do
unzip $i -d /data/app/mobile/lib/${i%-*}
done
```

参考截取字符串


## 更新记录

- 2020年9月：增加firewall
- 2020年11月：整理vim
- 2021年1月：批量解压