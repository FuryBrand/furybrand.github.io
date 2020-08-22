---
layout:     post
title:      "HTTP接口的Mock工具——WireMock简易手册"
date:       2020-07-27 20:07:00
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - Mock
    - 技术
---


> 第一版是真的简易手册，简易到只是简单使用一下下

上周**TTJ**找到我，说我之前搞的那个python写的http接口mock工具用不了了。原因是不知怎么回事，nginx的配置文件被清空了。<br>
鄙人便想“那就正好直接部署下WireMock试试吧”。

## 1.简介

官网上的一句话简介`WireMock is a simulator for HTTP-based APIs. Some might consider it a service virtualization tool or a mock server.`(WireMock是基于HTTP的API的模拟器。 有些人可能会认为它是服务虚拟化工具或者是mock服务器。)说人话就是WireMock可以mock一些http协议的接口，用于开发或者测试。

## 2.工作方式介绍

WireMock支持两种工作方式：
1. 与JUnit相结合或者直接在单元测试中使用。
2. 作为独立进程运行使用。

本篇着重介绍的是第2种方式。

## 3.独立进程方式的下载及使用

在官网中有[下载链接](http://wiremock.org/docs/download-and-installation/)，jar包的位置在页面的最下方。<br>
启动命令（详细的参数介绍参考[官方手册](http://wiremock.org/docs/running-standalone/)）：
- Windows:java -jar wiremock-jre8-standalone-2.27.0.jar
- Linux:nohup java -jar /root/wiremock-jre8-standalone-2.27.0.jar --port 8888 &

![启动图]({{ site.url }}assets/2020/2020-07-27-wiremock-simple-guide/20-07-27_22-28-36.png)

我这一般windows上启动的话，就是做本地调试用，所以命令行比较简单。参考上图，可以看出启动默认占用了8080端口。并且在当前目录下新建了`__files`和`mappings`这两个文件夹。（WireMock这个工程是用`gradle`做构建管理，web容器用的是`jetty`。这两个工具都没用过，真的是学到老活到老）

服务已经启动了，接下来是如何进行mock数据的填充了，WireMock提供了两种填充数据的方式。
- 在`mappings`文件夹中提前维护相关数据。
- 发送http请求实时进行数据配置。
  - 通过postman等工具调用接口。
  - 使用Chrome的插件。[三方制作的插件在Chrome Webstore上的地址](https://chrome.google.com/webstore/detail/wiremock-extension/ikiaofdpbmofgmlhajfnhdjelkleljbl?utm_source=chrome-ntp-icon)
  - 使用WireMock自带的UI界面`http://localhost:8080/__admin/swagger-ui`

WireMock是可以根据请求的内容做一些逻辑的，既请求内容不同，返回值也不同。具体设置方式还是参考[官网手册](http://wiremock.org/docs/request-matching/)。我这里附一个Postman的[导出文件]({{ site.url }}assets/2020/2020-07-27-wiremock-simple-guide/ExportFrom-liutianyu.postman_collection.json)，可以本地启动服务试一下。

## 后记

内容不多，希望能有用。说实在的，因为也不是自己用，所以确实没有研究很深。顺便说下自己的技术观，常规工具类的东西，现用现学就行。类似nginx之类的高频使用的工具，可以尝试深挖一下。不过最好把时间用在底层原理，技术核心的学习上。新技术总是层出不穷，不可能都学完。但是新技术很多时候是为了解决某类问题而产生的，其底层技术都有一样的，所以底层技术要搞扎实。但是不是说不去“拥抱”新技术。要辩证的看，没有一种技术可以解决所有问题的。这也就需要了解新技术产生的历史，为什么来？怎么来？到哪去？

## 更新日志
- 2020年7月27日：初稿。

## 友链
- [官网](http://wiremock.org/)
- [GitHub主页](https://github.com/tomakehurst/wiremock)
- [官方手册](http://wiremock.org/docs/)

