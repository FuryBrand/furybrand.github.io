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
    - 技术
---


> Docker真香~，作为轻量级的虚拟化技术，Docker有很多优势，具体，哎，后面再聊吧😀

## 1.背景

响应集团要求，测试环境集体上云。可是云数据库的资源木有了。。。。。所以只能申请一台云服务器自己来搭MySQL。刚好最近也在学Docker相关的东西。想来若各条线自己用自己的MySQL，那还是上Docker比较好。一方面自己是Docker的初学者，另一方面目前量级太小，也就没用上Kubernetes和Rancher啥的。

## 2.安装Docker

Docker的安装方式可以参考[官方手册](https://docs.docker.com/engine/install/)。我的机器是CentOS7的，测试环境默认不能连接外网，而且这台机器的yum好像还有些问题，没法安装本地的rpm包。所以用了一个野路子来安装Docker。

我用的是最新版本[docker-19.03.12.tgz](https://download.docker.com/linux/static/stable/x86_64/docker-19.03.12.tgz)，下载后上传至云服务器。以root用户来操作比较方便つ﹏⊂

```shell
$ tar xzvf docker-19.03.12.tgz
$ cp docker/* /usr/bin/
$ dockerd &
```

我这没有给docker加入到自启动中哈，所以每次需要手动启动docker。

## 3.导入镜像

首先在可以联网的本机中下载镜像文件，mysql是提供了官方镜像文件在dockerhub上的[网页链接](https://hub.docker.com/_/mysql)。

由于原本测试环境用的是5.7版本的MySQL，故在本机中执行

```shell
>docker pull mysql:5.7
>docker save mysql:5.7 > ./image_mysql.tar
```

将`image_mysql.tar`复制到云服务器后执行`docker load -i ./image_mysql.tar`命令即可载入镜像到docker。

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

## 5.启动的坑

实际总是没有想象中的那么顺利。踩坑开始~

#### 5.1 错误1

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

#### 5.2 错误2

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

## 参考文章

- [Docker离线部署images及启动容器](https://blog.csdn.net/little_pig_lxl/article/details/89499406)
- [linux防火墙查看状态firewall、iptable](https://www.cnblogs.com/zxg-blog/p/9835263.html)

## 更新日志
- 2020年9月3日：初稿。