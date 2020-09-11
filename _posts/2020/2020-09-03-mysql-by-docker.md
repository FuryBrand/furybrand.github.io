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

#### 5.4 错误4-设置MySQL不区分表名的大小写

数据好不容易迁移完了，然后有一个应用起来之后，web页面提示数据库表不存在。一看，发现这个库的表名中有大写，然后把错误提示中的SQL语句放到客户端执行下，发现迁移前的数据库可以正常执行，迁移后的docker版的MySQL就提示表不存在。好吧，应该要配置docker版的MySQL不区分表名大小写。需要在`/etc/mysql/mysql.conf.d/mysqld.cnf`中添加`lower_case_table_names=1`。处理过程如下：
- 先将docker容器中的文件复制到宿主机。
- 然后添加`lower_case_table_names=1`
- 随后将文件复制到容器中。
- 最后重启容器（如果防火墙不关闭的话，容器会启动失败，如果防火墙开启的话，即使端口打开也会访问不到，这个问题的原因后面再研究）

命令行存档如下：
```
[root@Server-i-jwvdl9av3u steve]# docker cp 1a0495313ae1:/etc/mysql/mysql.conf.d/mysqld.cnf .
[root@Server-i-jwvdl9av3u steve]# vim mysqld.cnf
[root@Server-i-jwvdl9av3u steve]# cat mysqld.cnf
# Copyright (c) 2014, 2016, Oracle and/or its affiliates. All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 2.0,
# as published by the Free Software Foundation.
#
# This program is also distributed with certain software (including
# but not limited to OpenSSL) that is licensed under separate terms,
# as designated in a particular file or component or in included license
# documentation.  The authors of MySQL hereby grant you an additional
# permission to link the program and your derivative works with the
# separately licensed software that they have included with MySQL.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License, version 2.0, for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA

#
# The MySQL  Server configuration file.
#
# For explanations see
# http://dev.mysql.com/doc/mysql/en/server-system-variables.html

[mysqld]
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
datadir         = /var/lib/mysql
#log-error      = /var/log/mysql/error.log
# By default we only accept connections from localhost
#bind-address   = 127.0.0.1
# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links=0
lower_case_table_names=1
[root@Server-i-jwvdl9av3u steve]# docker cp mysqld.cnf 1a0495313ae1:/etc/mysql/mysql.conf.d/mysqld.cnf
[root@Server-i-jwvdl9av3u steve]# docker exec -it 1a0495313ae1 /bin/bash
root@1a0495313ae1:/# cat /etc/mysql/mysql.conf.d/mysqld.cnf
# Copyright (c) 2014, 2016, Oracle and/or its affiliates. All rights reserved.
# ---------------same with above---------------
# blah blah blah...
# ---------------same with above---------------
lower_case_table_names=1
[root@Server-i-jwvdl9av3u steve]# docker stop 1a0495313ae1
1a0495313ae1
[root@Server-i-jwvdl9av3u steve]# service firewalld start
Redirecting to /bin/systemctl start firewalld.service
[root@Server-i-jwvdl9av3u steve]# docker start 1a0495313ae1
1a0495313ae1
[root@Server-i-jwvdl9av3u steve]# service firewalld stop
Redirecting to /bin/systemctl stop firewalld.service
```

如此费事的原因是MySQL的镜像中不包含vim等文本编辑功能。可以安装，也可以通过上面的docker cp命令。思路来自[stackoverflow](https://stackoverflow.com/questions/30853247/how-do-i-edit-a-file-after-i-shell-to-a-docker-container)

#### 5.5 错误4-nginx转发至多MySQL容器

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


## 参考文章

- [Docker离线部署images及启动容器](https://blog.csdn.net/little_pig_lxl/article/details/89499406)
- [linux防火墙查看状态firewall、iptable](https://www.cnblogs.com/zxg-blog/p/9835263.html)
- [stackoverflow：How do I edit a file after I shell to a Docker container?](https://stackoverflow.com/questions/30853247/how-do-i-edit-a-file-after-i-shell-to-a-docker-container)

## 更新日志

- 2020年9月3日：初稿。
- 2020年9月7日：增加`5.3 错误3-admin账号无法访问`
- 2020年9月8日：增加`nginx转发至多MySQL容器`
- 2020年9月11日：增加`设置MySQL不区分表名的大小写`