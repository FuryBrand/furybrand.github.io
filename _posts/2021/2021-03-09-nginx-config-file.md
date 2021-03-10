---
layout: post
title:  "记一场关于Nginx配置文件及网络问题排查步骤的分享"
date:   2021-03-09 19:22:49 +0800
subtitle:   ""
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - 技术相关
    - Nginx
---

有伙伴想听一下在排查网络环境问题上的一些经验。Nginx是一个避不开的话题，正好顺便把Nginx的一些内容一起过一下吧。下面算是该场分享的文本稿。

## 文本稿

#### 开篇

![开篇]({{ site.url }}assets/2021/2021-03-09-nginx-config-file/Nginx-data_masking-Ver0.8.001.jpeg)

大家好，我是XXX。今天和大家聊一聊Nginx的配置文件及排查网络问题步骤。

#### Nginx是什么？

![Nginx是什么？]({{ site.url }}assets/2021/2021-03-09-nginx-config-file/Nginx-data_masking-Ver0.8.002.jpeg)

C/C++

Nginx是C++写的，所以在性能上肯定会比较强。名字的含义是engine x。原作者是俄罗斯人。

HTTP server

Nginx可以作为HTTP server来代理一些静态资源文件。图片、css、js啥的

Reverse proxy server

平时的工作中，接触最多的可能就是Nginx作为反向代理服务器的情况了。反向代理服务器是一种代理服务器，通常位于专用网络中的防火墙后面，并将客户端请求定向到适当的后端服务器。 反向代理提供了更高级别的抽象和控制，以确保客户端和服务器之间网络流量的顺畅流动。测试环境的话，一般是两种情况。
1. 一台服务器中部署了多个Web服务，利用服务器的Nginx，配合客户端机器的host（或者内网的DNS）来做访问上的隔离。如果不这么搞的话，用ip加端口来访问也不是不可以。
2. 对于前后端分离式的部署架构，如前端是VUE的静态工程，后端多个Java应用提供HTTP接口的情况。Nginx可以作为HTTP server代理VUE工程，然后将特定的请求定向到后端服务。可以通过这种手段来解决跨域问题。

TCP/UDP proxy server

Nginx可以作为TCP/UDP的代理服务器，在之前的文章中，我试图利用Nginx代理MySQL服务。理论上可行，但是最终因为机器的编辑环境的依赖问题没有继续下去。

Mail proxy server(POP3, IMAP, SMTP)

既然可以搞定运输层的协议，那么基于TCP/IP的这些邮件协议也都不在话下了。

Load Balancing

反向代理的进阶就是负载均衡了。说白了就是活太多了干不过来，那就多来几个人干吧。具体的策略和配置在后面会有具体介绍，这里就不多说了。

FastCGI/SCGI/uwsgi

这个也有点意思，稍微说两句。前两个协议是给PHP用的，最后一个是给Python用的。像平时我们用Java应用的使用，Nginx是直接将HTTP转给了后端的Java应用的。但是其实Nginx也可以处理一下，将HTTP转成uwsgi之类的协议和后端通信。能猜到原因是啥吗？对，因为PHP和Python的效率较低，直接处理HTTP的效率不高，所以先由Nginx这个由C++写的程序处理一下，减轻后端服务的压力。再深的东西我也不懂了。

…

Nginx支持的还不止这些，比如ta还可以作为mp4的视频流的代理。但是我没有具体研究了。

#### Config File

![Config_File]({{ site.url }}assets/2021/2021-03-09-nginx-config-file/Nginx-data_masking-Ver0.8.003.jpeg)

Default config file - nginx.conf

Nginx的默认配置文件是“Nginx.conf“，根据安装路径的不同位置也不一定在哪。

“include domains/*;”

注意“Nginx.conf“中的“include domains/*;”的用法，会将指定路径下的内容全部载入到一起作为配置文件生效。最后在程序中应该是一个文件，所以此时是存在优先级的问题的。

Server Block(listen directive & server_name entries & location)

当一个请求进来的时候，Nginx会先判断应该是哪个server来处理这个请求。此时listen命令有最高优先级，若匹配到则无需关心server_name。listen决定了这个server块儿监听的是哪个ip和端口。示例中监听的是HTTP请求的默认端口80。当匹配到了多个server，此时会用server_name项来进行匹配。server_name支持通配符的匹配。有自己的优先级规则。server_name之后就是location的匹配了，location支持正则，也有多个优先级，重点说一个。“常规字符串匹配，如果有多个location都能匹配的话，优先匹配表达式最长的location”。匹配到了某一个location之后，会根据proxy_pass进行定向。若配置成了ip+端口，就直接转发走了。若配置成了upstream里配置的参数，则会使用负载均衡策略生效。另外查询log的话，参考access_log和error_log。

关于server块儿的介绍，具体可以参考[T-记一次Nginx分享]({% post_url 2020-09-02-nginx %})中的2.1，2.2。

#### Load balancing

![Load_balancing]({{ site.url }}assets/2021/2021-03-09-nginx-config-file/Nginx-data_masking-Ver0.8.004.jpeg)

提前声明，这部分都总结前人和官网的说明，我没有手动试验过。

round-robin(default)

轮询调度，就是一个一个来，标记为down的是手动下线的。标记为backup的是当所有的机器都不可用时才会用到ta。

least-connected

最小连接数，因为不是所有的请求，在服务器端的处理时长都相同。如果有些请求堆积了，那就让别人来处理，大原则是保持最小连接数。

ip-hash

相同来源的ip，会给到某个特定的后端服务。用以解决session在多个后端服务中不共享的问题。但是现在如果走算法的话可以解决这个问题。

server weights

权重，按照我们分配的权重分配。

#### Load balancing(3rd party)

![Load_balancing_3rd_party]({{ site.url }}assets/2021/2021-03-09-nginx-config-file/Nginx-data_masking-Ver0.8.005.jpeg)

fair

按后端服务器的响应时间来分配请求，响应时间短的优先分配。

url_hash

按访问url的hash结果来分配请求，使每个url定向到同一个后端服务器，后端服务器为缓存时比较有效。

#### Serving Static Content

![Serving_Static_Content]({{ site.url }}assets/2021/2021-03-09-nginx-config-file/Nginx-data_masking-Ver0.8.006.jpeg)

稍微介绍下[localized-kityminder](https://github.com/FuryBrand/localized-kityminder)的部署架构。

#### Http Request

![Http_Request]({{ site.url }}assets/2021/2021-03-09-nginx-config-file/Nginx-data_masking-Ver0.8.007.jpeg)

稍微介绍下HTTP请求的流程。重点是多级缓存。对应了为啥我们配置了Host还要清理浏览器缓存等问题。

ping

ping无法判断tcp/ip配置的是否正确，但是可以看下本机的host配置的是否正确。

telnet

telnet可以判断指定端口是否可用。

curl

curl是通过命令行发送HTTP请求，是真正的走了HTTP协议的。

#### share an issue of go-live

![share_an_issue_of_go-live]({{ site.url }}assets/2021/2021-03-09-nginx-config-file/Nginx-data_masking-Ver0.8.008.jpeg)

分享一个上线过程中的问题。UAT环境验证通过的版本，上到线上之后就不好用了。发现有些资源请求不到。原来公司在域名到服务器那一层用了负载均衡，导致新版本的资源文件请求到了IP1上。乱了。

#### End

我前面说的全部内容，在一些情况下可能都是假的。所以具体问题具体分析，逻辑才是无敌的。为逻辑干杯🍻

## 相关资料

- [What Is a Reverse Proxy Server?(nginx.com)](https://www.nginx.com/resources/glossary/reverse-proxy-server/)
- [nginx.org offical site](https://nginx.org/en/)
- [nginx.org documentation](https://nginx.org/en/docs/)
- [nginx.org change log](http://hg.nginx.org/nginx)
- [nginx.org source code(zip)](http://hg.nginx.org/nginx/archive/tip.zip)
- [How nginx processes a request(nginx.org)](http://nginx.org/en/docs/http/request_processing.html)

## 更新日志
- 2021年03月09日：初稿。