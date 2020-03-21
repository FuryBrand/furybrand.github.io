---
layout: post
title:  "Java-用MessageFormat来替换占位符"
date:   2019-03-03 23:57:25 +0800
subtitle:   ""
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - Java
---

最近开始Java写自动化测试脚本（虽然不太会Java，但是单位有现成的Java自动化框架，所以就写吧，其实编程语言都差不多，当作学习了😀）。

在处理回传的时候没有将回传的报文进行对象化，而是用了较为简单暴力的方式-占位符。Python中可以用占位符的方式来很方便的拼装报文，我想Java中肯定也有，果然，一搜就有那就是`java.text.MessageFormat`。

## 简单的用法-xml格式的回传报文

首先假设我们有个回传的报文，报文结构长成这个熊样。

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!--  Copyright w3school.com.cn -->
<note>
	<to>{0}</to>
	<from>{0}</from>
	<heading>{1}</heading>
	<body>Don't forget the meeting!</body>
</note>
```

把需要替换的部分，用占位符占好。从`{0}`开始以此类推。然后传一个数组过去，程序就会完成替换。请参考下面的代码。[附ideone的链接](https://ideone.com/PLkmWB)

```java
/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;
import java.text.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		String x = "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?><!--  Copyright w3school.com.cn --><note><to>{0}</to><from>{0}</from><heading>{1}</heading><body>Don't forget the meeting!</body></note>";
		String[] argus = {"George","Reminder"};
		x = MessageFormat.format(x, argus);
		System.out.println(x);
	}
}
```

## 进阶的用法-json格式的回传报文

由于MessageFormat用`{}`来作为占位符的标识符，所以当回传报文为json格式的时候就需要特殊对待了。

同样的首先假设我们有个回传的报文，报文结构长成这个熊样。

```json
{
    "employees": [
        {
            "firstName": "{0}",
            "lastName": "Gates"
        },
        {
            "firstName": "{0}",
            "lastName": "Bush"
        },
        {
            "firstName": "{1}",
            "lastName": "Carter"
        }
    ]
}
```

在MessageFormat中，我们用单引号`'`来特殊处理`{}`，就是用两个单引号来包住大括号`'{'`，从而让MessageFormat认为它只是一个普通的大括号。

这里要多说一嘴，因为用单引号来作为**Escape character**，所以当源字符串中要显示单引号的时候，需要用两个单引号来表示一个单引号。针对上面的json回传报文的替换，请参考下面的代码。[附ideone的链接](https://ideone.com/Lzgivv)

```java
/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;
import java.text.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		String x = "'{'\"employees\":['{'\"firstName\":\"{0}\",\"lastName\":\"Gates\"'}','{'\"firstName\":\"{0}\",\"lastName\":\"Bush\"'}','{'\"firstName\":\"{1}\",\"lastName\":\"Carter\"'}']'}'";
		String[] argus = {"George","Reminder"};
		x = MessageFormat.format(x, argus);
		System.out.println(x);
	}
}
```

## 遇到的一个坑


这个坑简直太坑了，我们的自动化框架是从Excel中读取数据的，而json中的一个大括号我们是肯定要加单引号的。但是，框架在读取Excel的时候，第一个单引号是默认忽略的，我不知道算不算是一个Bug....反正我排查了好久，因为总是报错，我就一直以为是我没用好单引号的位置。。。。。