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
```
