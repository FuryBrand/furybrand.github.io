---
layout: post
title:  "Git简明教程-从不会到能用？还是只是连接远称仓库？（笑）"
date:   2018-07-08 11:46:49 +0800
categories: jekyll update
---

- [01.下载安装Git，并在VSTS上新建一个项目](#01%E4%B8%8B%E8%BD%BD%E5%AE%89%E8%A3%85git%E5%B9%B6%E5%9C%A8vsts%E4%B8%8A%E6%96%B0%E5%BB%BA%E4%B8%80%E4%B8%AA%E9%A1%B9%E7%9B%AE)
- [02.Clone项目](#02clone%E9%A1%B9%E7%9B%AE)
- [xx.附录-常用Git命令](#xx%E9%99%84%E5%BD%95-%E5%B8%B8%E7%94%A8git%E5%91%BD%E4%BB%A4)
  - [git 的使用](#git-%E7%9A%84%E4%BD%BF%E7%94%A8)
  - [git config的使用](#git-config%E7%9A%84%E4%BD%BF%E7%94%A8)
  - [git stash的使用](#git-stash%E7%9A%84%E4%BD%BF%E7%94%A8)

**本教程针对Git的初学者**

今天介绍一下之前刚刚学的版本控制利器——Git。其实说实在的版本控制，我真正算是会用也就是今年。之前以前用Github啥的客户端直接就图形化操作，然后自己搞也不会出现冲突啥的。所以也就只知道皮毛而已。

Git的背景在这里就不过多的交代了。Git可以说是当今使用范围最广的版本控制工具。由于“分支”概念的存在，所以特别是和多人合作，并行开发。好像之前大家用集中式版本管理工具SVN，我没用过所以不敢乱说。但是某东已经从SVN切换成了Git，想必Git必有过人之处吧。

个人学习使用Git的话，还是要有个可以操练的东西才行，可以选择[Github][Github]和[Visual Studio Team Services][vsts]。Github是赫赫有名的开源项目托管的网站，缺点是免费用户的代码是开源的。VSTS的话，是微软的代码托管服务，如果是个人小团队（5人以下？）则可以免费使用。优点是代码闭源。

今天以VSTS为例，和我一起走一波连接Git的远程仓库，毕竟连上了远称仓库之后，想怎么玩就怎么玩了，Git光看效果不大，还是要操练起来才行。

# 01.下载安装Git，并在VSTS上新建一个项目
去官网下载[Git][Git]，然后一路下一步安装。（额，默认以windows为准了哈）
![下载Git]({{ site.url }}assets/2018-07-08-quick-git-grammar/001.png)

安装好Git之后，打开`Git Bash`，首先利用[`ssh-keygen`][ssh_keygen]命令来创建公钥，直接用默认路径就好，密码也可以留空，所以只需要敲击三次回车即可。随后用`cat ~/.ssh/id_rsa.pub`命令来查看生成的密钥。密钥稍后用。
![ssh]({{ site.url }}assets/2018-07-08-quick-git-grammar/002.png)

注册了微软账号之后，登陆应该要先建一个Team，因为我很久之前就建好了，这里就不演示了。然后在点击`New Project`。
![新建]({{ site.url }}assets/2018-07-08-quick-git-grammar/003.png)

填写`Project name`，`Version control`选择Git。[工作流][工作流]目前先默认就行，想要了解更多就去外链上看下吧。
![填写信息]({{ site.url }}assets/2018-07-08-quick-git-grammar/004.png)

创建成功了，选择`SSH`。后面的就是远程仓库地址。下不要关闭页面。
![仓库地址]({{ site.url }}assets/2018-07-08-quick-git-grammar/005.png)

点击`Manage SSH Keys`后，在弹出的页面上点击`Add`。将刚刚生成的密钥填写进去并`Save`
![添加ssh公钥]({{ site.url }}assets/2018-07-08-quick-git-grammar/006.png)
![添加ssh公钥]({{ site.url }}assets/2018-07-08-quick-git-grammar/007.png)

回到刚才说不要关闭页面的页面，对项目进行初始化，展开下面的选项，并点击`Initialize`。
![初始化项目]({{ site.url }}assets/2018-07-08-quick-git-grammar/008.png)

至此，项目就创建成功了。授权也弄好了。

# 02.Clone项目
在`Git Bash`页面，然后进入到我们想要下载代码的文件夹中。输入`git clone 远称仓库地址`。因为Git Bash中的命令和linux中的一样，这里就不赘述了。
![git_clone]({{ site.url }}assets/2018-07-08-quick-git-grammar/009.png)

[Git的官方介绍]已经很详细了，现在已经有了环境，就可以边看官方教程边学习了。

# xx.附录-常用Git命令

## git 的使用

| 命令 | 简介 | 备注 |
| - | - | - |
| git –version| 查看git版本| |
| git clone xxx| 克隆仓库||
| git checkout dev| 切换至dev分支| |
| git add ./xixi/heihei.txt| 将文件heihei.txt添加至staging area| |
| git add .| 将当前目录下的所有文件加入到staging area| |
| git commit -m '添加一个heihei.txt文件'| 将staging area中的文件提交到仓库| |
| git reset ./xixi/heihei.txt| 撤销添加到staging area中的指定文件| |
| git status| 查看当前仓库的状况| |
| git fetch| 从远程仓库获取最新的信息| |
| git pull| 获取远程仓库的最新版本并合并到本地| |
| git push| 将本地修改推到远程仓库| |
| git branch dev-xixi| 以当前分支创建一个dev-xixi的分支| 也可以用git checkout -b dev-xixi |
| git 


## git config的使用

| 命令 | 简介 | 备注 |
| - | - | - |
| git config --global user.name "liutianyu" | 设置全局的用户名 |  |
| git config --global --list| 列出所有全局的配置项| |
| git config --local --list| 在一个git repository下面使用，查看当前的配置| |
| git config --local user.name "liutianyu"| 设置局部用户名||
| git config --local user.email "liutianyu@x.com"| 设置局部邮箱||
| git config --system --unset credential.helper| 清除登录信息||

## git stash的使用

| 命令 | 简介 | 备注 |
| - | - | - |
| git stash save "xixi"| 创建名为“xixi”的stash，并将当前的工作区回归为初始状态。||
| git stash list| 列出当前所有的stash||
| git stash appley 0| 将序列号为0的stash中的内容恢复到当前的工作区，并且不删除||
| git reset --hard HEAD| 强制将当前的改动删掉，回归到初始状态。||
| git stash pop 0| 将序列号为0的stash中的内容恢复到当前的工作区，并且删除||
| git stash drop 0| 删除序列号为0的stash||
| git stash clear| 清空stash中的所有内容||



[Github]: https://github.com/
[vsts]: https://visualstudio.microsoft.com/zh-hans/team-services/
[工作流]: https://docs.microsoft.com/zh-cn/vsts/work/work-items/guidance/choose-process?view=vsts
[Git]: https://git-scm.com/
[ssh_keygen]: https://git-scm.com/book/zh/v1/%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A%E7%9A%84-Git-%E7%94%9F%E6%88%90-SSH-%E5%85%AC%E9%92%A5
[Git的官方介绍]: https://git-scm.com/book/zh/v1/%E8%B5%B7%E6%AD%A5-%E5%85%B3%E4%BA%8E%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6