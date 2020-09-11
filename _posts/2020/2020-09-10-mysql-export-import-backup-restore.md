---
layout:     post
title:      "MySQL的导入与导出、备份与还原"
date:       2020-09-10 21:18:00
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - MySQL
    - 技术相关
---

> 说一千道一万，其实主要聊的就是mysqldump😀

## 介绍

在MySQL的官网上是这么介绍mysqldump的`A Database Backup Program`。具体的用法可以参考MySQL的[官方手册](https://dev.mysql.com/doc/refman/5.7/en/mysqldump.html)。

## 导出

万变不离其宗，导出依赖的是mysqldump这个工具（组件、命令）。所以下面的命令就是核心了。
```
C:\Program Files\MySQL\MySQL Server 5.7\bin>mysqldump -uroot -psdfsdf123 --host=192.168.61.201 --port=3306 --databases game movie > test.sql
mysqldump: [Warning] Using a password on the command line interface can be insecure.

C:\Program Files\MySQL\MySQL Server 5.7\bin>
```

说明一下字段：
- `-u`用户。
- `-p`密码。
- `--host=`MySQL服务端的地址。
- `--port=`MySQL服务端的端口。
- `--databases `库名，多个库可以用空格间隔开。
- ` > test.sql`导出到当前的路径下。

试过小海豚等一些工作，我发现`MySQL Workbench`不错，可以批量导出多个库，也有好多选项可以选。路径是`Server - Data Export`。
![选项]({{ site.url }}assets/2020/2020-09-10-mysql-export-import-backup-restore/mysql_workbench.png)

然后执行过程的log如下：
```
18:28:15 Dumping xixixi_hub, xixixi_business, xixixi_output
Running: mysqldump.exe --defaults-file="c:\users\steveliu\appdata\local\temp\tmpbyfmhp.cnf"  --user=root --host=192.168.61.201 --protocol=tcp --port=3306 --default-character-set=utf8 --single-transaction=TRUE --databases "xixixi_hub" "xixixi_business" "xixixi_output"
18:32:33 Export of D:\steveliu\Documents\dumps\Dump20200910-1.sql has finished
```

## 备份

备份其实就是定时执行mysqldump，目前还没有搞起来，后面工具化之后再来记录。

## 导入&还原

本质是通过mysql这个工具（客户端、命令）来执行sql脚本。如`$ mysql -uroot -p123456 < Dump20200910-1.sql`。也可以通过可视化的客户端来进行导入，`MySQL Workbench`就是个不错的选择。

执行过程的log如下：
```
18:34:56 Restoring D:\steveliu\Documents\dumps\Dump20200910-1.sql
Running: mysql.exe --defaults-file="c:\users\steveliu\appdata\local\temp\tmp1af9r7.cnf"  --protocol=tcp --host=11.51.193.15 --user=root --port=6379 --default-character-set=utf8 --comments  < "D:\\steveliu\\Documents\\dumps\\Dump20200910-1.sql"
18:39:49 Import of D:\steveliu\Documents\dumps\Dump20200910-1.sql has finished
```

## 更新日志
- 2020年9月10日：初稿。