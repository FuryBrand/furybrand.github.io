@echo off

REM 声明采用UTF-8编码
chcp 65001

echo.
echo MySQL数据库备份脚本
echo.
echo *****************************
echo.
echo 备份日期：%date%
echo 备份时间：%time%
echo.
echo *****************************
echo.
echo 开始备份...
echo.
::set nowtime=%date:~3,4%年%date:~8,2%月%date:~11,2%日%time:~0,2%时%time:~3,2%分
set "nowtime=%date:~3,4%%date:~8,2%%date:~11,2% %time:~0,2%%time:~3,2%"
set "nowtime=%nowtime: =0%"
::数据库名称
set dbname=forlovetolove
::数据库的账号
set user=root
::数据库密码
set password=xixixihahaha
::数据库地址
set host=127.0.0.1
::数据库端口
set port_num=3306

::执行导出操作
 "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump" --column-statistics=0 --default-character-set=utf8mb4 -P%port_num% -h%host% -u%user% -p%password% %dbname%  > %dbname%_%nowtime%.sql

echo.
echo MySQL数据库备份完成
echo.

@echo on
@pause
