@echo off
:@=========================================
:@ע��defaultBranchΪĬ�Ϸ�֧��������Ҫ�������޸�
:@=========================================
set defaultBranch=master_test
echo Ŀǰ���õ�Ĭ�Ϸ�֧Ϊ%defaultBranch%
set /p branch=������Ҫ����ķ�֧������ʹ��Ĭ��������س����ɣ�
if  "%branch%"=="" (set branch=%defaultBranch%)
rd /s /Q .\dist\
mkdir dist
echo ��ʼ����֧�л�Ϊ%branch%
git checkout %branch%
echo ��ʼ��ȡ����
git fetch
git pull
echo ��ɴ�����ȡ��
echo ********************************************
echo ��ʼnpm build
call npm -v
call npm run build
echo ********************************************
cd dist
echo ��ʼ��war��
jar -cvf test.war *
echo ����
pause