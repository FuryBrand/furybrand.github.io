---
layout: post
title:  "Postman-几个小把戏"
date:   2019-10-09 18:44:25 +0800
subtitle:   ""
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - Postman
    - 技术相关
---

`Postman`应该是目前比较好用的测试HTTP接口的工具，由于它可以发送几乎所有类型的HTTP请求，所以堪称是“全能战士”。另附[官网链接](https://www.getpostman.com/)。

由于没有中文版，我发现了一个中国版的`Postman`，名叫`ApiPost`，另附[官网链接](https://www.apipost.cn)。这个我没用，但是瞄了一眼界面，可以说和`Postman`一毛一样，评价貌似也可以，需要的兄弟可以试试看。

今天我主要是来分享几个我常用的小把戏。所以默认读者已经用过`Postman`发送过请求，如果想看一些更详细的文章的话，这里有一个[51testing的专题](http://www.51testing.com/zhuanti/postman.htm)。另附一个[Postman使用方法的博客](https://blog.csdn.net/fxbin123/article/details/80428216)。


## 写在最前面

下面的所有内容都从Postman中导出来了，下载后可以直接导入后使用（[点我下载Postman导出的Collections]({{ site.url }}assets/2019/2019-10-9-postman-small-tricks/MyExplore_Blog.postman_collection.json)）。不过由于示例的服务是我局域网内的一个临时接口，所以可能只能作为语法参考了。或者参考这篇文章（[Python-mock一个提供http协议的服务]({% post_url 2018-12-5-Python-mock-http %})）来在本机提供一个临时接口以供调用。

## 不可不知的大前提

- `Pre-request Script`中的脚本在发送请求前会自动执行，脚本语言是Javascript，默认内置了一些JS库，比如`CryptoJS`。
- `View -> Show Postman Console`是很好用的调试工具，可以看到请求具体发送出去的信息，也可以看到脚本中`console.log("");`打印出的信息。

## 1.参数化

很多时候我们测试不可能一次通过，而验证问题或者复现问题只需要在报文中改一个唯一的值，比如*订单号*、*身份证号码*、*手机号码*等等，就可以。这里我们利用参数化可以简单实现这个需求。

`Request Headers`和`Request Body`中的内容都可以通过{% raw %}{{paramName}}{% endraw %}的形式进行参数化。

![参数化]({{ site.url }}assets/2019/2019-10-9-postman-small-tricks/1.png)
![脚本]({{ site.url }}assets/2019/2019-10-9-postman-small-tricks/2.png)

## 2.如何应对一个有签名算法的接口

为了防止接口调用的过程中被恶意攻击篡改，一般暴露在公网的接口往往都需要调用方携带签名进行请求。那么如何应对一个有签名算法的接口呢？

两个系统对接时一般都会有对接的接口文档，如果需要签名的话，一般会提供相应的加密算法的源码。开发兄弟往往可以拿着源码直接去写程序了，而我们如果在`Postman`上使用这样一个接口的话，就需要我们用Javascript来实现对应的加密算法了😓

一般的签名都是用到了MD5算法，好在`Postman`中内置了`CryptoJS`可以轻松处理它。

![签名]({{ site.url }}assets/2019/2019-10-9-postman-small-tricks/3.png)

## 3.网站需要登录咋整

说起登录就很容易联想起Http身份认证了，这个要具体问题具体分析。举个最简单的例子，设置路由器的时候，网页会弹出一个弹窗要求输入用户名和密码，这种身份认证是`HTTP Basic Authentication`，可以在`Postman`主窗口中的`Authorization`进行配置即可。

我要聊的是通过Session和Cookie实现的登录。之前处理过这样的问题，架构是前端独立的Vue应用，后端业务逻辑为Java应用。通过日志拿到了前端调用后端的请求报文，但是想自己模拟的时候发现直接发送请求会被登录拦住。这时候最简单的处理方式就是通过浏览器登录，然后用F12开发者工具拿到对应的cookie后通过`Postman`直接带着cookie就可以发送请求了。

![浏览器]({{ site.url }}assets/2019/2019-10-9-postman-small-tricks/4.png)
![Cookie]({{ site.url }}assets/2019/2019-10-9-postman-small-tricks/5.png)

## 4.base64编解码和Tests

有时和外部接口交互的时候规定了传输的编码格式比如base64等。对我们来说肯定是utf8有可读性了。那么就需要将入参报文和出参报文进行base64的编解码。编码自然是参考[1.参数化](#1%e5%8f%82%e6%95%b0%e5%8c%96)，在`Pre-request Script`中进行编码。为了提到出参的可读性，在`Tests`中进行解码，将原本的以base64编码的出参转换成可读的utf8编码格式并展示在`Test Results`中。详情参考下面两图。

![Pre-request_Script]({{ site.url }}assets/2019/2019-10-9-postman-small-tricks/6.png)
![Tests]({{ site.url }}assets/2019/2019-10-9-postman-small-tricks/7.png)

这里有一个坑，我当时阻塞了很久，从本节的第一张图可以看出来，出参是分了多行的。这也是我当时实测接口的状况，导致做转换时，`Tests`中的第6行一直报错。后来才发现原来是换行符的锅。所以才有了第3行去换行去回车的代码。

## 5.在请求前的请求

有点绕口，其实就是在点击`Send`按钮后，在此请求发出去前，先通过Pre-request Script执行一次http请求，从而获取一些信息。我的实际场景是外部系统和我交互的时候需要签名，而研发那边提供了一个http接口，我先调这个接口就可以得到签名。省的我自己写签名的算法了。那么问题来了，我不能每次请求都手动调下研发提供的然后手动填sign吧，这样好麻烦。所以就在报文正式请求前先请求一次提供签名的接口，然后将得到的签名填到sign上，从而实现偷懒，具体不同的接口在参数上可能有所区别，抛砖引玉吧。详情参考下面两图。

![Body]({{ site.url }}assets/2019/2019-10-9-postman-small-tricks/8.png)
![Pre-request_Script]({{ site.url }}assets/2019/2019-10-9-postman-small-tricks/9.png)

## 6.重复发送请求——Runner的使用

背景：为了测试Web页面的翻页功能，需要一些数据做支持。之前尝试过使用Selenium，这次尝试使用Postman。以后有机会可以试试jmeter，应该也可以做到。

方案：使用Postman的Runner功能，对指定接口进行多次请求。可以参考[Postman的官方手册](https://learning.postman.com/docs/running-collections/working-with-data-files/)，其实我也是用了官方的接口做范例的。踩过的坑是MS Excel在保存csv文件的时候，将原本的`,`保存成了`空格`，导致导入给Postman的时候没法正确识别。

步骤：
1. 下载`写在最前面`中附的Collection`MyExplore`并使用Request`6.重复发送请求——Runner的使用`。（以我的实际场景来说，我是使用了Postman的Import-Raw Text功能，配合Chrome的copy-copy as cURL(bash)来导入的，这样就不用设置cookie等参数了，很方便。[参考](https://m.weibo.cn/status/4544056790628230?)）
2. 进入`Runner`，选择Collection，勾选需要执行的`Request`。设定循环次数15次，设置延迟时间，选择数据源文件[点我下载import_data.csv]({{ site.url }}assets/2019/2019-10-9-postman-small-tricks/import_data.csv)后Run就可以了。如果每次调用时的入参有多个，那么预览的时候数据的展示一定是下面所示的那样。如果不是的话，大概率是csv文件有问题。除了csv文件以外，还支持json的方式导入数据，但是做数据的话，我觉得csv会方便一点。

![Runner]({{ site.url }}assets/2019/2019-10-9-postman-small-tricks/10.png)

## 7.活用cURL

curl是一个命令行工具，可以用URL来传输数据。[官网](https://curl.se/)，[github主页](https://github.com/curl/curl)

很多软件都支持curl有不同程度的支持。
- Chrome：导出
- Postman：导出&导入
- JMeter：导入

Postman的导入可以参考：
![curl导入]({{ site.url }}assets/2019/2019-10-9-postman-small-tricks/311606208094_.pic_hd.jpg)

Postman的导出可以参考：
![curl导出]({{ site.url }}assets/2019/2019-10-9-postman-small-tricks/iShot2020-12-08_18.17.47.jpg)

## 更新日志

2020年3月30日：追加`5.在请求前的请求`
2020年9月15日：追加`重复发送请求——Runner的使用`
2020年12月8日：追加`活用cURL`