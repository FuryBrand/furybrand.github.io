@echo off
:@=========================================
:@ע��defaultBranchΪĬ���ύ�����ݣ���ǰ���ڣ���������Ҫ�������޸�
:@=========================================
set defaultBranch=%date%
echo ��Log��ĿǰĬ�ϵ��ύ����Ϊ��%defaultBranch%��
set /p branch=������Ҫ�ύ��comment��
if  "%branch%"=="" (set branch=%defaultBranch%)
git add .
echo ��Log��git add .ִ�����
git commit -m "%branch%"
echo ��Log��git commit -mִ�����
git push
echo ��Log��git pushִ�����
