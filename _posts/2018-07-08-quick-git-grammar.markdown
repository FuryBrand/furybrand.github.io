---
layout: post
title:  "Git简明教程-从不会到能用（笑）"
date:   2018-07-08 11:46:49 +0800
categories: jekyll update
---
**本教程针对Git的初学者**

今天介绍一下之前刚刚学的版本控制利器——Git。其实说实在的版本控制，我真正算是会用也就是今年。之前以前用Github啥的客户端直接就图形化操作，然后自己搞也不会出现冲突啥的。所以也就只知道皮毛而已。

Git的背景在这里就不过多的交代了。Git可以说是当今使用范围最广的版本控制工具。由于“分支”概念的存在，所以特别是和多人合作，并行开发。好像之前大家用集中式版本管理工具SVN，我没用过所以不敢乱说。但是某东已经从SVN切换成了Git，想必其必有过人之处吧。

个人使用Git的话，可以选择[Github][Github]和[Visual Studio Team Services][vsts]。Github是赫赫有名的开源项目托管的网站，缺点是免费用户的代码是开源的。VSTS的话，是微软的代码托管服务，如果是个人小团队（5人以下？）则可以免费使用。优点是代码闭源。

今天以VSTS为例，和我一起走一波Git入门。

# 01.在VSTS上新建一个项目
注册了微软账号之后，登陆应该要先建一个Team，因为我很久之前就建好了，这里就不演示了。然后在点击`New Project`。
![新建]({{ site.url }}assets/2018-07-08-quick-git-grammar/01.png)

填写`Project name`，`Version control`选择Git。[工作流][工作流]目前先默认就行，想要了解更多就去外链上看下吧。
![填写信息]({{ site.url }}assets/2018-07-08-quick-git-grammar/02.png)

创建成功了，红框部分就是远称仓库的地址了。
![仓库地址]({{ site.url }}assets/2018-07-08-quick-git-grammar/03.png)

点击上一张图片中的`Generate Git credentials`按钮，创建一个密码。
![创建密码]({{ site.url }}assets/2018-07-08-quick-git-grammar/04.png)

至此，项目就创建成功了。

# 02.下载安装Git，Clone项目






[Github]: https://github.com/
[vsts]: https://visualstudio.microsoft.com/zh-hans/team-services/
[工作流]: https://docs.microsoft.com/zh-cn/vsts/work/work-items/guidance/choose-process?view=vsts