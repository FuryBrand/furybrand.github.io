@echo off
:@=========================================
:@注：defaultBranch为默认分支，若有需要可自行修改
:@=========================================
set defaultBranch=master_test
echo 目前配置的默认分支为%defaultBranch%
set /p branch=请输入要打包的分支名，若使用默认配置则回车即可：
if  "%branch%"=="" (set branch=%defaultBranch%)
rd /s /Q .\dist\
mkdir dist
echo 开始将分支切换为%branch%
git checkout %branch%
echo 开始拉取代码
git fetch
git pull
echo 完成代码拉取！
echo ********************************************
echo 开始npm build
call npm -v
call npm run build
echo ********************************************
cd dist
echo 开始打war包
jar -cvf test.war *
echo 结束
pause