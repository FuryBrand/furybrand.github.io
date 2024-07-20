#!/bin/bash
# 程序：完成add、commit、push的git动作
# History:
# 2021年6月29日：初稿
#PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin:/mingw64/bin/git
#export PATH
read -p "Please input the COMMENT that you want to commit: " input
if [ "$input" == "" ]; then
    comment=$(date +%Y/%m/%d_%H:%M)
else
    comment=$input
fi
echo -e "The COMMENT is \a \n$comment\n"
echo -e "We will excute 'git add .'"
git add .
echo -e "We will excute 'git commit -m'"
git commit -m "$comment"
echo -e "We will excute 'git push'"
git push
exit 0