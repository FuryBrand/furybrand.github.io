---
layout: post
title:  "Selenium初探"
date:   2019-09-10 21:06:25 +0800
categories: jekyll update
---

## 背景

虽然以前接触过selenium，但是那时候对前端的知识还是“一窍不通”的状态。最近跟着单位的大佬**韩老师**学了些前端知识。刚好现在跟的项目，有一块儿类似注册登录的页面，需要录入9个信息，太长了啊，实在是不想反复重复了。刚好看到躺在Chrome里的Selenium IDE，于时便动手录了一段脚本，然后就舒服了~~

## 脚本录制

先打开`Selenium IDE`，然后创建Project和Tests，之后输入好要访问的URL。随后点击**REC**录制按钮后会弹出一个新的浏览器页面，跟着操作就好了。

`感觉最近GitHub的访问速度都巨慢，下面是一个gif动图，如果载入太慢的话，就右键保存本地之后看吧😓`

![录屏动图]({{ site.url }}assets/2019-09-10-selenium-first-exploration/14.gif)

## 脚本导出

点击某个**Test**后面的三个小点，就有**Export**按钮了。可以导出`Java JUnit`、`JavaScript Mocha`、`Python pytest`三种语言的脚本。具体使用我还没有尝试，但是看起来应该会较为方便的融入到一些测试框架中去。

## 典型问题

上面的录制只是针对了最简单的文本输入框进行的录制。录制虽然方便，但是目前还没有那么全能，啥都能录，还有些东西是`Selenium IDE`的录制功能搞不定，这时候就需要特殊处理了。

