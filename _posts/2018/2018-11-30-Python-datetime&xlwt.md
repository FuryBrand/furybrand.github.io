---
layout: post
title:  "Python-浅解datetime和xlwt"
date:   2018-11-30 23:50:25 +0800
subtitle:   ""
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - Python
---

这两天写了个小工具，从任务管理平台的数据库中获取数据，然后在excel中绘制出甘特图。初衷是为了方便排期，因为会有一些优先级被升级的任务插队，但是又不能很直观得知道谁在这个时段有空。

虽然甘特图可以很容易体现出任务进行过程中的一些里程碑，以及什么时段该由谁来做什么事情。但是当每个人都是多任务并行的时候，甘特图并不能直观的体现出每个人的工作饱和度。因为假设功能测试阶段，需要投入100%的精力，但是各种联调阶段可能就并不需要投入这么多了，虽然可以通过调整权重来体现工作饱和度。可是权重怎么算更准呢？

不管怎么说，由于这个小工具需要操作时间和excel，所以用到了datetime和xlwt，既然用了就稍稍整理下吧。

## 1. datetime

datetime是python中基本的日期和时间类型。包含了很多可用的类型：**datetime.date**、**datetime.time**、**datetime.datetime**等，因为mysql中保存时间使用了**DATETIME**类型。而使用pymysql读取出来的值就刚好是**datetime.datetime**，所以基本用的这个。我也没深入理解这俩东西，就是稍微记录下怎么用吧。如果有时间的话，其实读一下手册看看源码还是挺有帮助的。[手册(python3的)](https://docs.python.org/3/library/datetime.html)

### 1.1 用法

新建一个python文件，将下面的代码复制进去执行下就行。其实直接看也行，因为输出的结果也标记出来了。

```python
import datetime

# 获取当天
today = datetime.datetime.today()
print('today',today) #today 2018-12-01 00:39:21.844169
# 获取7天前
print('7 days befor:', today - datetime.timedelta(days=7)) #7 days befor: 2018-11-24 00:39:21.844169
# 将字符串的时间转换为datetime
date = datetime.datetime.strptime("2018-11-30 0:39:25", "%Y-%m-%d %H:%M:%S")
print('date:',date) #date: 2018-12-01 00:39:25
# 获取两个datetime的日期差
days = (date - today).days
print('days', days) # days -2
# 补充一个坑，因为数据库中获取的时间可能没有具体是小时分钟数，所以在和today计算日期差的时候可能会不准，可以通过如下方法将today中的小时分钟抹去。
today = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
```

## 2. xlwt

选用xlwt纯属巧合，python操作excel的三方库有很多。随便搜了下，觉得这个好像能挺好用的就用了，实际使用起来也很可以。

直接用pip安装就好：`pip install xlwt`

[手册](https://xlwt.readthedocs.io/en/latest/)、[GitHub地址](https://github.com/python-excel/xlwt)

### 2.1 用法

新建一个python文件，将下面的代码复制进去执行下就行。执行后会在python文件所在目录生成一个**xixi.xls**的文件。

```
import datetime
import xlwt

# 获取一个excel文件
file = xlwt.Workbook()
# 新建一个sheet（cell_overwrite_ok=True标识可以重复写单元格）
table = file.add_sheet('甘特图',cell_overwrite_ok=True)

# 设置格式1：显示日期为这样的格式：12/1（num_format_str用的是excel中“设置单元格格式”中的“自定义”中的“类型”中的内容）
style0 = xlwt.XFStyle()
style0.num_format_str = r'm/d'

# 设置格式2：设置背景色
style1 = xlwt.XFStyle()
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
# May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
pattern.pattern_fore_colour = 23
style1.pattern = pattern

# 传入横坐标、纵坐标、内容、格式来绘制表格
table.write(0,0,datetime.datetime.today(),style0)
table.write(0,1,'2018/12/01',style1)
# 保存excel文件
file.save('xixi.xls')
```