---
layout:     post
title:      "Python-控制Chrome的登录与窗口调整"
date:       2024-07-18 19:33:00
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - 技术相关
    - Python
---

> GPT真的很好用，已经可以很大程度上辅助人写代码了。研发没时间弄，为了项目推进我直接开干

## 背景

BS架构的视频相关项目，当前版本视频长期放置之后画面会延迟，为了帮助现场用起来所以搞了自动化的脚本对程序进行初始化，登陆Web系统，跳转指定页面，控制Chrome窗口位置并最大化。

## 知识点与代码

知识点清单：
- selenium，控制浏览器
- tkinter，绘制python程序窗体
- pygetwindow，控制系统的窗口

[代码示例]({{ site.url }}assets/2024/2024-07-18-python-automatic-chrome/automate_chrome.py)

## 实施

#### 知识点1：将python打包exe可执行文件
参考这里[Python-将python文件打包成exe文件]({% post_url 2018-11-28-Python2exe %})

#### 知识点2：将python环境迁移至对象机器并离线安装

主要目的是防止对象机器没有可靠外网。

1. **导出依赖列表**：
   在开发机器上，使用`pip freeze`来创建一个包含所有已安装依赖的列表。在一个空文件夹中，打开命令行工具并执行以下命令：

   ```bash
   pip freeze > requirements.txt
   ```

   这将在当前目录下创建一个`requirements.txt`文件，里面列出了所有已安装的包及其版本。

2. **下载依赖包**：
   接下来，使用`pip download`命令来下载`requirements.txt`中列出的所有包及其依赖项。

   ```bash
   pip download -r requirements.txt -d ./
   ```

3. **在目标机器上安装依赖**：
   在目标机器上，进入对应目录，使用`pip`来安装这些包。执行以下命令：

   ```bash
   pip install --no-index *
   ```

5. **验证安装**：
   安装完成后，可以使用`pip list`命令来验证是否所有的包都已正确安装。

## 更新日志
- 2024年7月18日：初稿