---
layout:     post
title:      "用JMeter替换Postman"
subtitle:   "JMeter简易入门指南"
date:       2021-03-17 20:35:00
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - JMeter
    - 技术相关
---


> 由于安全等原因，需要弃用Postman迁移至JMeter。

## 下载及安装

macOS的话，安装及配置参考[记从Windows办公迁移至MAC办公]({% post_url 2020-10-24-software-4-work-MAC %})，Windows的话，直接官网下载就好了。

## 简单入门

#### 新增一个Thread Group

右键`Test Plan` -> `Add` -> `Threads(Users)` -> `Thread Group`

因为是代替Postman，所以目前保持如下设置即可，不用调整线程数等参数

![截图]({{ site.url }}assets/2021/2021-03-17-use-jmeter-2-replace-postman/01.png)

#### 新增一个HTTP Request并尝试请求

右键`Thread Group` -> `Add` -> `Sampler` -> `HTTP Request`

将HTTP接口的相关信息填入其中，如下：

![截图]({{ site.url }}assets/2021/2021-03-17-use-jmeter-2-replace-postman/02.png)

右键`Thread Group` -> `Start`或者通过上方的绿色播放按钮来执行。

#### 查看结果并保留Response报文

通过上面的步骤，可以发送请求，但是请求发送的成功失败，啥情况，咱不知道。所以需要增加两个Listener来看下结果。

右键`Thread Group` -> `Add` -> `Listener` -> `View Result Tree`

右键`Thread Group` -> `Add` -> `Listener` -> `Save Responses to a fail`

此时再次尝试发送请求便可以通过`View Result Tree`来看到响应的结果了。

![截图]({{ site.url }}assets/2021/2021-03-17-use-jmeter-2-replace-postman/03.png)

但是由于报文体中的内容并不能进行复制（或者说我暂时没有找到复制的方法），暂时通过`Save Responses to a fail`来将响应保存下来。

![截图]({{ site.url }}assets/2021/2021-03-17-use-jmeter-2-replace-postman/04.png)

#### 增加HTTP Header Manager

JMeter的话，相对Postman，很多东西需要自己维护好，若后端对于中文不识别，或者请求的报文体的格式没有正确识别的话，可能需要我们手动的维护下Header

右键`Thread Group` -> `Add` -> `Config Element` -> `HTTP Header Manager`

![截图]({{ site.url }}assets/2021/2021-03-17-use-jmeter-2-replace-postman/05.png)

此时再次请求的话，可以在`View Result Tree`中的`Request` - `Request Headers`中增加了刚刚设置好的Header了。

这里我曾经遇到过一个Bug，当时使用了`Add from Clipboard`按钮，页面看起来一起正常，但是请求的时候就在Header中莫名其妙的增加了一个空格，导致后端一直解析出错。后来删除了之后重新手撸了一遍就好了。

#### 简单的参数化

JMeter支持BeanShell的方式进行参数化，详细的使用方式参考官网，我这就是简单实现一个替换。

右键`Thread Group` -> `Add` -> `Pre Processors` -> `BeanShell PreProcessor`

![截图]({{ site.url }}assets/2021/2021-03-17-use-jmeter-2-replace-postman/06.png)

```
//这是一个注释，token是xixi拼装了当前的时间戳。
String token = "xixi" + "${__time(,)}";
String name;
String age;
int flag = 2;
switch (flag) {
    case 1:
        name = "liutianyu";
        age = "18";
        break;
    case 2:
        name = "liuwuxin";
        age = "108";
}
vars.put("token", token);
vars.put("name", name);
vars.put("age", age);
log.info(">>>>>>>>>>>");
log.info("刚刚发送的数据flag为：" + flag);
```

此时`HTTP Request`中需要做如下改造。

![截图]({{ site.url }}assets/2021/2021-03-17-use-jmeter-2-replace-postman/07.png)

`BeanShell PreProcessor`中是可以打印日志的，日志通过`JMeter` -> `Options` -> `Log Viewer`来激活日志窗口。

## 更新日志
- 2021年3月17日：初稿。