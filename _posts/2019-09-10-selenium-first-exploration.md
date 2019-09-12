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

### 1.input形式的下拉选

如果是select形式的下拉选，虽然我没有尝试，但是作为基本的HTML元素，推测通过`Selenium IDE`的录制应该就能搞定。我遇到的是用`<input>`做的下拉选。该下拉选形式如下：

![下拉选]({{ site.url }}assets/2019-09-10-selenium-first-exploration/微信截图_20190912094014.png)

录制的脚本并不能生效，处理方式为：
1. 触发点击激活下拉选（脚本应该会录制）；
2. 手动通过浏览器的F12开发者工具，定位要选的下拉选的选项。这里用**XPath**或者**selector**都行，只不过一个在Target对应`xpath=`，另一个对应`css=`。

![下拉选手动定位]({{ site.url }}assets/2019-09-10-selenium-first-exploration/微信截图_20190912095245.png)

![下拉选脚本]({{ site.url }}assets/2019-09-10-selenium-first-exploration/微信截图_20190912095524.png)

### 2.日期控件

针对日期控件，录制脚本的时候也是未能成功录制出来的。虽然前端的时间控件千奇百怪，但是大部分的控件在和后台交互的时候都是讲选好的时间以`<input>`的形式提交。此时的一个投机取巧的方式为，直接给控件的输入框赋值。注意，该方式其实是绕过了选择时间的过程，而是直接赋值了时间。故无法暴露控件本身存在的问题，切记。

处理方法很简单：
1. 手动通过浏览器的F12开发者工具，定位要提交的`<input>`元素。这里用**XPath**。
2. 在`Selenium IDE`通过js脚本为`<input>`元素赋值。Target中的内容如下。

```
document.querySelector('#pane-white > div > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div:nth-child(1) > div > input').value='2019-09-01  00:00:00';
```

![日期控件手动定位]({{ site.url }}assets/2019-09-10-selenium-first-exploration/微信截图_20190912100442.png)

![日期控件脚本]({{ site.url }}assets/2019-09-10-selenium-first-exploration/微信截图_20190912100630.png)

### 3.后续遇到新问题再补充吧

参考文档：
1. [selenium IDE Chrome下载安装与使用](https://blog.csdn.net/qq_33673213/article/details/90489479)
