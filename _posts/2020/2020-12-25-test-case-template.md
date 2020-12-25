---
layout: post
title:  "一种用于应对灵活变化的测试用例模版"
date:   2020-12-25 18:57:25 +0800
subtitle:   "测试用例模版之我见"
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - JS
    - 杂文
---

> 经过了小半年的尝试，终于有了一个我相对满意的模版了～

之前一直在考虑是否要启用思维导图的方式来作为测试用例的载体。

其实去年在公司的某个项目中就进行了一下探索，但是存在一些未解决的问题。现在拿出来说，一方面是为了配合敏捷开发模型中的快速迭代。另一方面我觉得我的模版达到了一个小里程碑。所以聊一下。

目前整个业界对于测试用例的编写载体，基本有3种。
- Excel
- 思维导图
- TestLink、HP ALM等或开源，或收费的测试用例管理平台
  
TestLink没有试用过，但是HP ALM可以理解为一个加强版的，云端的带有测试用例模板的Excel。从成本（使用、迁移）来说，Excel和思维导图的成本都较低。下面我将这两种形式稍微做下对比：

Excel
- 优势：
  - 可以模板化，从而规范测试用例的编写，进而输出相对合规和高品质的测试用例。
  - 可以归档，针对稳定的功能模块，可以相对方便的复用。
  - 进度数据很好统计。
  - 可以非常直观的展现流程性的内容。
- 劣势：
  - 编写耗时较长。
  - 文字阅读量大，评审过程非常痛苦。

思维导图
- 优势：
  - 编写耗时较短。
  - 验证点简单直观。
- 劣势：
  - 基本没法归档。

其实从现在来看，随着敏捷开发替代了瀑布开发，传统的Full Test， Regression Test(Round X), Sanity Test等相对少了，用例继承的机会也变少了。所以新员工对于老流程的熟悉，其实可以用自动化测试的脚本来熟悉。

软件上用百度脑图的本地版，可以从[github](https://github.com/NaoTu/DesktopNaotu/releases)上下载。

测试用例模版如下：
![参数化]({{ site.url }}assets/2020/2020-12-25-test-case-template/testCaseTemplate.png)

[点我下载软件的.km源文件]({{ site.url }}assets/2020/2020-12-25-test-case-template/testCaseTemplate.km)

## 进度的计算公式如下

<p>请输入用例内容：</p>
<textarea rows="15" cols="80" id="testCase"></textarea>
<p><input type="button" value="统计" onclick="count()">
<p>-n（new）的数量：<pan id="underline_n"></pan></p>
<p>-p（passed）的数量：<pan id="underline_p"></pan></p>
<p>-b（blocked）的数量：<pan id="underline_b"></pan></p>
<p>-f（failed）的数量：<pan id="underline_f"></pan></p>
<p>-NA（not available）的数量：<pan id="underline_na"></pan></p>
<p>总数量为<b id="underline_all"></b>；
    通过(p+NA)的数量为<b id="underline_all_p"></b>；
    通过率(通过/总数)为<b id="underline_all_p_na_rate"></b>
</p>
<p>
    阻塞率(阻塞/总数)为<b id="underline_all_b_rate"></b>
    错误率(错误/总数)为<b id="underline_all_f_rate"></b>
    未执行率(未执行/总数)为<b id="underline_all_n_rate"></b>
</p>
<script type="text/javascript">
    function count() {
        var testCase = document.getElementById("testCase").value;
        var count_n = getCharCount(testCase, '-n');
        var count_f = getCharCount(testCase, '-f');
        var count_p = getCharCount(testCase, '-p');
        var count_b = getCharCount(testCase, '-b');
        var count_na = getCharCount(testCase, '-NA');
        document.getElementById("underline_n").innerHTML = count_n;
        document.getElementById("underline_f").innerHTML = count_f;
        document.getElementById("underline_p").innerHTML = count_p;
        document.getElementById("underline_b").innerHTML = count_b;
        document.getElementById("underline_na").innerHTML = count_na;
        var count_all = count_n + count_f + count_p + count_na + count_b;
        var count_all_p_na = count_p + count_na;
        document.getElementById("underline_all").innerHTML = count_all;
        document.getElementById("underline_all_p").innerHTML = count_all_p_na;
        document.getElementById("underline_all_p_na_rate").innerHTML = getPercentage(count_all_p_na, count_all) + '%';
        document.getElementById("underline_all_b_rate").innerHTML = getPercentage(count_b, count_all) + '%';
        document.getElementById("underline_all_f_rate").innerHTML = getPercentage(count_f, count_all) + '%';
        document.getElementById("underline_all_n_rate").innerHTML = getPercentage(count_n, count_all) + '%';
    }
    function getCharCount(str, char) {
        var regex = new RegExp(char, 'g'); // 使用g表示整个字符串都要匹配
        var result = str.match(regex);          //match方法可在字符串内检索指定的值，或找到一个或多个正则表达式的匹配。
        var count = !result ? 0 : result.length;
        return count;
    }
    function getPercentage(num, total) {
        // if(num == 0 || total == 0){
            // return 0;
        // }
        if(num == 0){
            return 0;
        }
        if(total == 0){
            return 0;
        }
        return (Math.round(num / total * 10000) / 100.00);// 小数点后两位百分比
    }
</script>