@echo off
:@=========================================
:@注：defaultBranch为默认提交的内容（当前日期），若有需要可自行修改
:@=========================================
set defaultBranch=%date%
echo 【Log】目前默认的提交内容为“%defaultBranch%”
set /p branch=请输入要提交的comment：
if  "%branch%"=="" (set branch=%defaultBranch%)
git add .
echo 【Log】git add .执行完成
git commit -m "%branch%"
echo 【Log】git commit -m执行完成
git push
echo 【Log】git push执行完成