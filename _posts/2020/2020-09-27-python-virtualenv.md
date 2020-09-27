---
layout:     post
title:      "Python-virtualenv"
date:       2020-09-27 19:10:00
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - 技术相关
    - Python
---

> 总用总忘，总结一波（呸，就是用的少，用的多了就不忘了）

## 建立虚拟环境

首先尝试使用该命令：`> python -m venv my_env`

如果上述命令报错（按道理不会，因为python3内置了venv模块），则可能需要安装virtualenv包。尝试使用如下命令：
- 方式1：`> pip install --user virtualenv`
- 方式2：`# sudo apt-get install python-virtualenv`

安装好之后使用该命令创建虚拟环境：`virtualenv my_env` 。若需要指定python版本则使用参数如：`virtualenv my_env ——python=python3`

## 激活虚拟环境

Linux首先尝试使用该命令：`# source my_env/bin/activate`
Windows使用cmd：`> my_env\Scripts\activate`

## 停止使用虚拟环境

命令：`deactivate`

## 在虚拟环境中安装Django（其他包同理）

命令：`pip install Django`

## 更新日志
- 2020年9月27日：初稿