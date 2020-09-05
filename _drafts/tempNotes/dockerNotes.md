- [书](#书)
- [以Docker的形式部署MantisBT](#以docker的形式部署mantisbt)
- [实际用过的](#实际用过的)
- [Linux相关](#linux相关)

## 书
```shell
$ docker pull ubuntu:18.04
$ docker run -it ubuntu:18.04 bash
$ docker images
$ docker tag ubuntu:latest myubuntu:latest
$ docker [image] inspect ubuntu:18.04
$ docker history ubuntu:18.04
$ docker search ——filter=is-official=true nginx
$ docker rmi myubuntu:latest
$ docker ps -a
$ docker rm a21c0840213e
$ docker image prune -f
$ docker [container] commit -m "Added a new file" -a "Docker Newbee" a925cb40b3f0 test:0.1
OPENVZ模板的下载地址为http://openvz.org/Download/templates/precreated
$ cat ubuntu-18.04-x86_64-minimal.tar.gz | docker import - ubuntu:18.04
$ docker [image] build -t python:3 .
$ docker save -o ubuntu_18.04.tar ubuntu:18.04
$ docker load -i ubuntu_18.04.tar
$ docker push user/test:latest
$ docker create -it ubuntu:latest
$ docker start af
$ docker run ubuntu /bin/echo 'Hello world'
$ docker run -it ubuntu:18.04 /bin/bash
$ docker logs ce554267d7a4
$ docker pause test
$ docker stop ce5
$ docker ps -qa
$ docker restart ce554267d7a4
$ docker attach nostalgic_hypatia
$ docker exec -it 243c32535da7 /bin/bash
$ docker rm -f 2ae
$ docker export -o test_for_run.tar ce5
$ docker export e81 >test_for_stop.tar
$ docker import test_for_run.tar - test/ubuntu:v1.0
$ docker container inspect test
$ docker top test
$ docker [container] cp data test:/tmp/
$ docker container diff test
$ docker container port test
$ docker update ——cpu-quota 1000000 test
```

## 以Docker的形式部署MantisBT

[DockerHub链接](https://hub.docker.com/r/xlrl/mantisbt)

docker-compose.yml，windows下需要把`volumes`中的内容注释掉
```
mantisbt:
  image: xlrl/mantisbt:latest
  ports:
    - "8989:80"
  links:
    - mysql
  # volumes:
    # - ./config:/var/www/html/config
    # - ./custom:/var/www/html/custom
  restart: always

mysql:
  image: mariadb:latest
  environment:
    - MYSQL_ROOT_PASSWORD=root
    - MYSQL_DATABASE=bugtracker
    - MYSQL_USER=mantisbt
    - MYSQL_PASSWORD=mantisbt
  # volumes:
    # - ./mysql:/var/lib/mysql
  restart: always
```

启动命令`D:\myExplore\Docker\xlrl_mantisbt>docker-compose -f docker-compose.yml up`

启动后的首次配置信息：

```
URL: http://localhost:8989/admin/install.php
>>> username: administrator
>>> password: root

==================================================================================
Installation Options
==================================================================================
Type of Database                                        MySQL/MySQLi
Hostname (for Database Server)                          mysql
Username (for Database)                                 mantisbt
Password (for Database)                                 mantisbt
Database name (for Database)                            bugtracker
Admin Username (to create Database if required)         root
Admin Password (to create Database if required)         root
Print SQL Queries instead of Writing to the Database    [ ]
Attempt Installation                                    [Install/Upgrade Database]
==================================================================================
```

## 实际用过的
```shell
$ docker container prune  #清理掉所有处于终止状态的容器。
$ docker exec -it GRcontainerID /bin/bash #进入容器的终端，进入后通过exit退出
$ ddocker port mymysql #列出指定的容器mymysql的端口映射
$ docker images #显示镜像列表
$ docker ps #列出正在运行中的容器
$ docker ps -a #列出所有容器
$ docker stop mymysql #停止mymysql这个容器
$ docker rm mymysql #删除mymysql这个容器
$ doker load -i image_mysql.tar #导入指定的使用 docker save 命令导出的镜像。
```

## Linux相关
```
# yum源配置的路径
/etc/yum.repos.d/CentOS-Base.repo

##############################3 搭建mysql的流程
# 通过终端mysql连接到mysqld
# 如果直接执行`mysql`的话会报错`ERROR 1045 (28000): Unknown error 1045`
$ mysql -u root -p

# 查看mysqld的配置文件路径
$ which mysqld
/usr/sbin/mysqld
$ mysqld --verbose --help |grep -A 1 'Default options'
Default options are read from the following files in the given order:
/etc/my.cnf /etc/mysql/my.cnf /usr/etc/my.cnf ~/.my.cnf

# 查找mysqld安装时生成的默认密码
$ grep "password" /var/log/mysqld.log
2020-09-04T02:43:59.016429Z 1 [Note] A temporary password is generated for root@localhost: XKKq&Jw6i9jT

# 设置mysql的连接密码
mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'XdcBlt9W0vbVvYv5VVLMSv29yE';
ERROR 1819 (HY000): Your password does not satisfy the current policy requirements
mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'XdcBlt9W0vbVvYv5VVLMSv29yE234324234@@@';
Query OK, 0 rows affected (0.00 sec)

# mysqld启停
$  service mysqld restart
Redirecting to /bin/systemctl restart mysqld.service
$ service firewalld stop
Redirecting to /bin/systemctl stop firewalld.service

# 添加用户并授权可以远程访问
mysql> create user 'admin'@'%' identified with mysql_native_password by 'XdcBlt9W0vbVvYv5VVLMSv29yE234324234!!!';
Query OK, 0 rows affected (0.00 sec)
mysql> grant all privileges on *.* to 'admin'@'%' with grant option;
Query OK, 0 rows affected (0.00 sec)
mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)
```

[CentOS7安装MySQL8.0图文教程](https://blog.csdn.net/weixin_42266606/article/details/80879571)
