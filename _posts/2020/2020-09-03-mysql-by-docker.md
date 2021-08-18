---
layout:     post
title:      "记一次在测试环境云服务器上搭建运行在Docker中的MySQL"
date:       2020-09-03 21:18:00
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - MySQL
    - Docker
    - 技术相关
---


> Docker真香~，作为轻量级的虚拟化技术，Docker有很多优势，具体，哎，后面再聊吧😀

## 1.背景

响应集团要求，测试环境集体上云。可是云数据库的资源木有了。。。。。所以只能申请一台云服务器自己来搭MySQL。刚好最近也在学Docker相关的东西。想来若各条线自己用自己的MySQL，那还是上Docker比较好。一方面自己是Docker的初学者，另一方面目前量级太小，也就没用上Kubernetes和Rancher啥的。

## 2.安装Docker

Docker的安装方式可以参考[官方手册](https://docs.docker.com/engine/install/)。我的机器是CentOS8的，测试环境默认不能连接外网，而且这台机器的yum好像还有些问题，没法安装本地的rpm包。所以用了一个野路子来安装Docker。

我用的是最新版本[docker-19.03.12.tgz](https://download.docker.com/linux/static/stable/x86_64/docker-19.03.12.tgz)，下载后上传至云服务器。以root用户来操作比较方便つ﹏⊂

```shell
$ tar xzvf docker-19.03.12.tgz
$ cp docker/* /usr/bin/
$ dockerd &
```

我这没有给docker加入到自启动中哈，所以每次需要手动启动docker。

## 3.导入镜像

首先在可以联网的我的windows笔记本中下载镜像文件，mysql是提供了官方镜像文件在dockerhub上的[网页链接](https://hub.docker.com/_/mysql)。

由于原本测试环境用的是5.7版本的MySQL，故在我的windows笔记本中执行

```shell
>docker pull mysql:5.7
>docker save mysql:5.7 > ./image_mysql.tar
```

将`image_mysql.tar`复制到云服务器后执行`$ docker load -i ./image_mysql.tar`命令即可载入镜像到docker。

## 4.准备镜像

MySQL的用户数据可以由Docker容器来管理，参考[Docker官方手册](https://docs.docker.com/engine/tutorials/dockervolumes/#adding-a-data-volume)。也可以放在宿主机的指定目录下，在启动容器的时候通过挂在的方式来载入，参考[Docker官方手册](https://docs.docker.com/engine/tutorials/dockervolumes/#mount-a-host-directory-as-a-data-volume)。MySQL官方推荐第二种方式。故，需要创建自己的目录。

```shell
$ mkdir -p /qcteam/mysql
$ docker run --name ibteam-mysql -p 3358:3306 -v /qcteam/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw-haha -e MYSQL_USER=admin -e MYSQL_PASSWORD=admin -d mysql:5.7 --skip-name-resolve
```

稍微解释下命令含义：
- `--name ibteam-mysql`指定容器的名称为**ibteam-mysql**。
- `-p 3358:3306`将容器内部的端口3306映射到宿主机的3358端口。
- `-v /qcteam/mysql:/var/lib/mysql`将宿主机路径`/qcteam/mysql`挂载到容器的`/var/lib/mysql`下。
- `-e MYSQL_ROOT_PASSWORD=my-secret-pw-haha等`是MySQL的环境变量，具体参考[dockerhub](https://hub.docker.com/_/mysql)的`Environment Variables`部分。
- `-d`后台运行容器，并返回容器ID。
- `mysql:5.7`指定镜像名称和tag。

## 5.踩坑开始

实际总是没有想象中的那么顺利。踩坑开始~

#### 5.1 错误1-启动失败

```
[root@Server-i-ez15oy6wta ~]# docker run --name ibteam-mysql -v /qcteam/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw-haha -d mysql:5.7 -e MYSQL_USER=admin -e MYSQL_PASSWORD=admin
b9b580de15e01d71855306fbcb89343106a8cf99343b7bbbb0f5eab94fddd809
docker: Error response from daemon: OCI runtime create failed: container_linux.go:349: starting container process caused "process_linux.go:449: container init caused \"write /proc/self/attr/keycreate: permission denied\"": unknown.
[root@Server-i-ez15oy6wta ~]# docker: Error response from daemon: OCI runtime create failed: container_linux.go:349: starting container process caused "process_linux.go:449: container init caused \"write /proc/self/attr/keycreate: permission denied\"": unknown.
```

原因是SELINUX开启导致docker run失败了。修改`/etc/selinux/config`文件，设置SELINUX=disabled。

```
# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#     enforcing - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
#     disabled - No SELinux policy is loaded.
SELINUX=disabled
# SELINUXTYPE= can take one of these three values:
#     targeted - Targeted processes are protected,
#     minimum - Modification of targeted policy. Only selected processes are protected.
#     mls - Multi Level Security protection.
SELINUXTYPE=targeted
```

#### 5.2 错误2-端口不通

启动成功后，通过本机无法连接数据库，排查是防火墙的原因，但是我即使开放了端口也依然无法访问，最后只能停掉了防火墙。但是停掉防火墙之后又会导致Docker没法把MySQL给run起来。。。。。最后暂时只能run的时候打开防火墙，run起来之后关闭防火墙。。。。。

关于CentOS7的默认防火墙firewall的一些操作。更多linux命令参考[我的Linux常用命令（持续更新）]({% post_url 2018-07-11-my-linux-basic-instructions %})
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

**2021年8月18日更新**

关闭firewalld会引入别的问题，比如重启某个容器的时候会产生如下报错。

```shell
[root@Server-i-jwvdl9av3u ~]# docker restart fff8182066ff
Error response from daemon: Cannot restart container fff8182066ff: driver failed programming external connectivity on endpoint mysql-v1 (b9de0189a32b84faab60c29fb8d9922b5eaeb6f684f231b8651534a0fe880847):  (iptables failed: iptables --wait -t nat -A DOCKER -p tcp -d 0/0 --dport 3358 -j DNAT --to-destination 172.17.0.3:3306 ! -i docker0: iptables: No chain/target/match by that name.
```

目前docker在宿主机上是以原生应用程序的方式运行的，docker在做镜像内和宿主机间的端口映射是通过一个名为docker0的interface来完成的（通过下面的ifconfig可以确认）。将该interface添加至firewalld的管理中就可以避免docker和firewalld的冲突。也就可以解决端口不通的问题。

```shell
[root@Server-i-jwvdl9av3u ~]# ifconfig
docker0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
        inet6 fe80::42:3eff:fec6:d897  prefixlen 64  scopeid 0x20<link>
        ether 02:42:3e:c6:d8:97  txqueuelen 0  (Ethernet)
        RX packets 33235054040  bytes 47398854406962 (43.1 TiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 43848079027  bytes 12940616216545 (11.7 TiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

使用如下命令将interface docker0加入到firewalld的trusted zone

```shell
[root@Server-i-jwvdl9av3u ~]# firewall-cmd --permanent --zone=trusted --change-interface=docker0
[root@Server-i-jwvdl9av3u ~]# firewall-cmd --reload
```

同时配合上面提到的firewalld的相关操作将端口开放即可彻底解决该问题。
#### 5.3 错误3-admin账号无法访问

本机的客户端连接的时候提示`Access denied for user 'admin'@'172.17.0.1' (using password: YES)`。本质就是需要进行特定ip的访问授权，但是奇怪的是root账号没有进行任何设置直接登录就没有问题。忘记在哪里看到的资料了，好像是MySQL的Docker镜像为了方便使用，给root默认开了各种情况下的访问授权。总之，咱还是先记录下处理过程吧

```
[root@Server-i-ez15oy6wta ~]# docker exec -it ibteam-mysql bash
root@559218d389cb:/# mysql
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)
root@559218d389cb:/# mysql -uroot -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 38
Server version: 5.7.31 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use mysql
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> select host, user from user;
+-----------+---------------+
| host      | user          |
+-----------+---------------+
| %         | admin         |
| %         | root          |
| localhost | mysql.session |
| localhost | mysql.sys     |
| localhost | root          |
+-----------+---------------+
5 rows in set (0.00 sec)

mysql> select host, user, plugin from user;
+-----------+---------------+-----------------------+
| host      | user          | plugin                |
+-----------+---------------+-----------------------+
| localhost | root          | mysql_native_password |
| localhost | mysql.session | mysql_native_password |
| localhost | mysql.sys     | mysql_native_password |
| %         | root          | mysql_native_password |
| %         | admin         | mysql_native_password |
+-----------+---------------+-----------------------+
5 rows in set (0.00 sec)

mysql> create user 'admin'@'172.17.0.1' identified with mysql_native_password by 'b9b580de15e01d71855306fbcb89343106a8cf99343b7bbbb0f5eab94fddd809';
Query OK, 0 rows affected (0.00 sec)

mysql> grant all privileges on *.* to 'admin'@'172.17.0.1' with grant option;
Query OK, 0 rows affected (0.00 sec)

mysql> select host, user, plugin from user;
+------------+---------------+-----------------------+
| host       | user          | plugin                |
+------------+---------------+-----------------------+
| localhost  | root          | mysql_native_password |
| localhost  | mysql.session | mysql_native_password |
| localhost  | mysql.sys     | mysql_native_password |
| %          | root          | mysql_native_password |
| %          | admin         | mysql_native_password |
| 172.17.0.1 | admin         | mysql_native_password |
+------------+---------------+-----------------------+
7 rows in set (0.00 sec)

mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)

mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)

mysql> flush privileges;
Query OK, 0 rows affected (0.01 sec)
```

#### 5.4 错误3-nginx转发至多MySQL容器

其实严格意义来说这不是一个错误。由于服务器端口受限，只有固定的数个端口对外开放，故我想用nginx进行代理，将mysql的TCP请求根据url的不同转给特定的后端Docker容器来处理。经过调研之后发现可行，但是需要在编译nginx的时候追加参数`--with-stream_ssl_preread_module`([link2 nginx.org](http://nginx.org/en/docs/stream/ngx_stream_ssl_preread_module.html))。无奈我这nginx是yum装的啊。。。。重新进行编译，发现一堆的依赖没有安装，披荆斩棘安了5个依赖，不行了，哥们我实在整不动了。。。。放一个[stackoverflow的链接](https://stackoverflow.com/questions/34741571/nginx-tcp-forwarding-based-on-hostname/40135151#40135151)吧，具体的思路是从这里来的。

**10 hours later**

早上八点到了单位开始尝试我前一天回去的路上想到的新方案，既然在Docker的宿主机上进行转发的路不通，那么是否可以借助其他条线的部署应用的云主机上的nginx来进行转发呢？反正目的是按照条线或者系统进行MySQL的隔离，那么就将转发方式由集中式转发变为分布式。

```
原预想
10.0.0.1 (Docker & nginx & mysqls)
mysql1.com ─┬─► nginx at 10.0.0.1:3358 ─┬─► mysql_docker at 10.0.0.1:1000
mysql2.com ─┤                           ├─► mysql_docker at 10.0.0.1:1001
mysql3.com ─┤                           ├─► mysql_docker at 10.0.0.1:1002
新方案
10.0.0.1 (Docker & mysqls)
10.0.1.1 (nginx & Tomcat)
10.0.1.2 (nginx & Tomcat)
10.0.1.3 (nginx & Tomcat)
mysql1.com ──► nginx at 10.0.1.1:3358 (eg: Other Tomcat Application work at 10.0.1.1:8001) ──► mysql_docker at 10.0.0.1:1000
mysql2.com ──► nginx at 10.0.1.2:3358 (eg: Other Tomcat Application work at 10.0.1.2:8001) ──► mysql_docker at 10.0.0.1:1001
mysql3.com ──► nginx at 10.0.1.3:3358 (eg: Other Tomcat Application work at 10.0.1.3:8001) ──► mysql_docker at 10.0.0.1:1002
```

结果发现，nginx可以支持TCP协议的转发，但是需要在编译nginx的时候追加参数`--with-stream`([link2 nginx.org](http://nginx.org/en/docs/stream/ngx_stream_core_module.html))并且是在version 1.9.0以后才支持的。哥们一看10.0.1.1上的nginx版本是`nginx version: nginx/1.0.0`。😭哥们真的不搞了，不搞了。。。。。。。但是还是记录一下配置文件该怎么写吧，注意不要写到http的块儿里面。
```
stream {
    # 添加socket转发的代理
    upstream socket_proxy {
        # 转发的目的地址和端口
        server 11.51.192.224:3358 weight=5 max_fails=3 fail_timeout=30s;
    }

    # 提供转发的服务，即访问3358，会跳转至代理socket_proxy指定的转发地址
    server {
       listen 3358;
       proxy_connect_timeout 1s;
       proxy_timeout 3s;
       proxy_pass socket_proxy;
    }
}
```

**10 minutes later**

我想，如果为了隔离权限的话，其实用账号来隔离也可以，只是相对更加麻烦一些。。。。。。。。。

#### 5.5 错误4-docker_start的诡异错误

这套环境运行了一段时间，一次某位研发哥哥验证自己工具类在并发情况下是否有问题，将咱的redis打懵了。然后我试图重启redis失败，尝试重启一个MySQL容器也失败。会报如下错误：

```
[root@Server-i-jwvdl9av3u ~]# docker start 27b674ae128c
Error response from daemon: driver failed programming external connectivity on endpoint some-redis (83255f39845510dfbe82e85066017862c4acfd66771b02641b328c82a843b07a):  (iptables failed: iptables --wait -t nat -A DOCKER -p tcp -d 0/0 --dport 22000 -j DNAT --to-destination 172.17.0.4:6379 ! -i docker0: iptables: No chain/target/match by that name.
 (exit status 1))
Error: failed to start containers: 27b674ae128c

[root@Server-i-jwvdl9av3u ~]# docker run --name some-redis1 -p 22003:6379 -d redis:5.0.5
dc17ca309e57bf06b58495c9a32233b8101e7ecce7554c72941a49be65329468
docker: Error response from daemon: driver failed programming external connectivity on endpoint some-redis1 (e926ed6af5f4ee1bfebf71364d7efa89138bcb01ef8b1608ec145dacad1bc1dc):  (iptables failed: iptables --wait -t nat -A DOCKER -p tcp -d 0/0 --dport 22003 -j DNAT --to-destination 172.17.0.4:6379 ! -i docker0: iptables: No chain/target/match by that name.
 (exit status 1)).
```

一顿尝试无果后，最后的解决方式是stop了所有的容器之后，`kill -9 dockerd`（因为暂时装的原生docker，也不知道怎么正常退出😅）。然后重新启动docker再启动容器就好。不过确认了一点，run的时候给的参数，在start或者restart的时候都会带上，不用担心端口映射被搞丢的情况发生。

## 参考文章

- [Docker离线部署images及启动容器](https://blog.csdn.net/little_pig_lxl/article/details/89499406)
- [linux防火墙查看状态firewall、iptable](https://www.cnblogs.com/zxg-blog/p/9835263.html)
- [stackoverflow：How do I edit a file after I shell to a Docker container?](https://stackoverflow.com/questions/30853247/how-do-i-edit-a-file-after-i-shell-to-a-docker-container)
- [CentOS7, CentOS8 firewalld docker 端口映射问题，firewall开放端口后，还是不能访问，解决方案](https://www.jianshu.com/p/0767eca968e6)

## 更新日志

- 2020年9月3日：初稿。
- 2020年9月：增加`5.3 错误3-admin账号无法访问`、`nginx转发至多MySQL容器`、`设置MySQL不区分表名的大小写`
- 2020年10月：增加`docker_start的诡异错误`，将`设置MySQL不区分表名的大小写`移走
- 2021年8月18日：补充“5.2 错误2-端口不通”，待解决问题closed。