---
layout: post
title:  "Postman-几个小把戏"
date:   2019-10-09 18:44:25 +0800
categories: jekyll update
---

`Postman`应该是目前比较好用的测试HTTP接口的工具，由于它可以发送几乎所有类型的HTTP请求，所以堪称是“全能战士”。另附[官网链接](https://www.getpostman.com/)。

由于没有中文版，我发现了一个中国版的`Postman`，名叫`ApiPost`，另附[官网链接](https://www.apipost.cn)。这个我没用，但是瞄了一眼界面，可以说和`Postman`一毛一样，评价貌似也可以，需要的兄弟可以试试看。

今天我主要是来分享几个我常用的小把戏。所以默认读者已经用过`Postman`发送过请求，如果想看一些更详细的文章的话，这里有一个[51testing的专题](http://www.51testing.com/zhuanti/postman.htm)。另附一个[Postman使用方法的博客](https://blog.csdn.net/fxbin123/article/details/80428216)。

目录：
- [不可不知的大前提](#%E4%B8%8D%E5%8F%AF%E4%B8%8D%E7%9F%A5%E7%9A%84%E5%A4%A7%E5%89%8D%E6%8F%90)
- [1.参数化](#1%E5%8F%82%E6%95%B0%E5%8C%96)
- [2.如何应对一个有签名算法的接口](#2%E5%A6%82%E4%BD%95%E5%BA%94%E5%AF%B9%E4%B8%80%E4%B8%AA%E6%9C%89%E7%AD%BE%E5%90%8D%E7%AE%97%E6%B3%95%E7%9A%84%E6%8E%A5%E5%8F%A3)
- [3.网站需要登录咋整](#3%E7%BD%91%E7%AB%99%E9%9C%80%E8%A6%81%E7%99%BB%E5%BD%95%E5%92%8B%E6%95%B4)

## 不可不知的大前提

- `Pre-request Script`中的脚本在发送请求前会自动执行，脚本语言是Javascript，默认内置了一些JS库，比如`CryptoJS`。
- `View -> Show Postman Console`是很好用的调试工具，可以看到请求具体发送出去的信息，也可以看到脚本中`console.log("");`打印出的信息。

## 1.参数化

很多时候我们测试不可能一次通过，而验证问题或者复现问题只需要在报文中改一个唯一的值，比如*订单号*、*身份证号码*、*手机号码*等等，就可以。这里我们利用参数化可以简单实现这个需求。

`Request Headers`和`Request Body`中的内容都可以通过`{{paramName}}`的形式进行参数化。

![参数化]({{ site.url }}assets/2019-10-9-postman-small-tricks/微信截图_1.png)
![脚本]({{ site.url }}assets/2019-10-9-postman-small-tricks/微信截图_2.png)

另附[Postman导出的Collections]({{ site.url }}assets/2019-10-9-postman-small-tricks/MyExplore.postman_collection.json)，下载后可以直接导入后使用，不过由于示例的服务是我局域网内的一个临时接口，所以只能勉强参考下语法啥的了。

## 2.如何应对一个有签名算法的接口

为了防止接口调用的过程中被恶意攻击篡改，一般暴露在公网的接口往往都需要调用方携带签名进行请求。那么如何应对一个有签名算法的接口呢？

两个系统对接时一般都会有对接的接口文档，如果需要签名的话，一般会提供相应的加密算法的源码。开发兄弟往往可以拿着源码直接去写程序了，而我们如果在`Postman`上使用这样一个接口的话，就需要我们用Javascript来实现对应的加密算法了😓

一般的签名都是用到了MD5算法，好在`Postman`中内置了`CryptoJS`可以轻松处理它。

![签名]({{ site.url }}assets/2019-10-9-postman-small-tricks/微信截图_3.png)

另附[Postman导出的Collections]({{ site.url }}assets/2019-10-9-postman-small-tricks/MyExplore.postman_collection.json)，下载后可以直接导入后使用，不过由于示例的服务是我局域网内的一个临时接口，所以只能勉强参考下语法啥的了。

## 3.网站需要登录咋整

说起登录就很容易联想起Http身份认证了，这个要具体问题具体分析。举个最简单的例子，设置路由器的时候，网页会弹出一个弹窗要求输入用户名和密码，这种身份认证是`HTTP Basic Authentication`，可以在`Postman`主窗口中的`Authorization`进行配置即可。

我要聊的是通过Session和Cookie实现的登录。之前处理过这样的问题，架构是前端独立的Vue应用，后端业务逻辑为Java应用。通过日志拿到了前端调用后端的请求报文，但是想自己模拟的时候发现直接发送请求会被登录拦住。这时候最简单的处理方式就是通过浏览器登录，然后用F12开发者工具拿到对应的cookie后通过`Postman`直接带着cookie就可以发送请求了。

![浏览器]({{ site.url }}assets/2019-10-9-postman-small-tricks/微信截图_4.png)
![Cookie]({{ site.url }}assets/2019-10-9-postman-small-tricks/微信截图_5.png)

另附[Postman导出的Collections]({{ site.url }}assets/2019-10-9-postman-small-tricks/MyExplore.postman_collection.json)，下载后可以直接导入后使用，不过由于示例的服务是我局域网内的一个临时接口，所以只能勉强参考下语法啥的了。
