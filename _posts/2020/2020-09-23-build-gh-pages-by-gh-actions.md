---
layout:     post
title:      "利用Github Actions来构建发布Github Pages"
date:       2020-09-23 21:50:00
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - 技术相关
    - 持续集成
---

> 踩了一些坑，趁热打铁抓紧记下来

## 背景

最近较为深度试用了一下Typora，发现它原生支持mermaid，很香。具体mermaid的使用还是老套路，参考[官方手册](https://mermaid-js.github.io/mermaid/#/)。

咱这博客也是markdown写的，想着要是能支持mermaid的话该有多好啊~于是开始了上下而求索之路。

## 找jekyll的插件

最开始找到的是[jekyll-mermaid](https://github.com/jasonbellamy/jekyll-mermaid)，不好用。复盘一下，其实还是自己犯傻逼，看着readme写的很完备就上了。完全没考虑这个工程已经是6年前的了。。。。。。

后来找到了[jekyll-spaceship](https://github.com/jeffreytse/jekyll-spaceship)，这个是真牛逼，支持好多小功能（包含mermaid）。在Gitpod上验证了一下可行，就往Github上推了。发现还是不行呢🤬

原来Github默认只支持safe模式，只提供指定的一些[白名单内的插件](https://pages.github.com/versions/)。

## 试用travis

每次触发构建都要很久，然后也没有成功，具体错误没有查就转投Github Action上了😜

## 试用Github Actions

不愧是Github自家产品，入口在工程Web主页的`Actions`里，点击进去就发现Github Acions已经识别了工程是`Jekyll`的。然后有一个推荐的构建yml文件。我试了下不好使。我用的是[jekyll官网提供](https://jekyllrb.com/docs/continuous-integration/github-actions/)的yml文件。可以直接参考咱这个工程的[yml文件](https://github.com/FuryBrand/furybrand.github.io/blob/master/.github/workflows/jekyll.yml)。

注意里面有一个名为`JEKYLL_PAT`的环境变量。这个是Github的`Personal access tokens`，是为了赋予部署应用使用Github API的。申请路径为`Account icon -> Settings -> Developer settings -> Personal access tokens`。我给的权限是**admin:public_key, admin:repo_hook, repo**，暂时没有纠结给多给少，反正好用（那应该是给多了😓）。我们需要把申请到的token填写到`Project home page -> Settings -> Secrets`中，key肯定就是`JEKYLL_PAT`嘛。

综上，每次在master分支上推新代码时，就可以触发构建了。

哦哦，还有一点，在`Project home page -> Settings -> Options -> GitHub Pages`中选择分支为`gh-pages`哈，因为GitHub Actions在构建好之后是默认推这个分支的。

## 更新日志
- 2020年9月23日：初稿