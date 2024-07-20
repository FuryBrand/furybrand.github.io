---
layout:     post
title:      "FFmpeg-使用笔记"
date:       2024-07-20 18:01:00
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - 技术相关
    - FFmpeg
---

> 做了两年多的视频相关的产品了，这里记录一下ffmpeg在日常生活中的一些应用。

## 简介

应该是传统视频领域中最强大的音视频处理软件了，但是由于是命令行软件，所以上手对于非软件行业的用户有一点点门槛。市面上很多音视频相关的软件都是基于FFmpeg做页面开发而来的。

[官方下载链接](https://ffmpeg.org/download.html)

## 场景一：视频裁切与拼接

废话少说，直接上命令行了。

使用ffmpeg截取并拼接视频的命令：

```ssh
$ sudo ffmpeg -i /home/temp/20231021/ch09_20231017132740_3_0_1107.mp4 -ss 00:20:24 -to 00:23:55 -c:v copy -c:a copy 1.mp4
$ sudo ffmpeg -i /home/temp/20231021/ch09_20231017164347_3_0_6D08.mp4 -ss 00:27:57 -to 00:44:57 -c:v copy -c:a copy 2.mp4
$ sudo ffmpeg -i /home/temp/20231021/ch09_20231017212736_3_0_2504.mp4 -ss 00:24:11 -to 00:25:49 -c:v copy -c:a copy 3.mp4
$ sudo ffmpeg -f concat -i file -c copy /data3/11011318471320206009.mp4
$ cat file
file '1.mp4'
file '2.mp4'
file '3.mp4'
```

## 场景二：视频转码H.265

目前主流的视频是H.264编码的，H.265编码相对压缩比更高，实测各类电影、视频在进行H.265编码后，体积缩减至原始文件的六分之一左右。类似的相对较新的编码格式还有AV1、VP9，但是我没有进行实测。

使用FFmpeg转码时可以使用CPU也可以使用对应的GPU进行硬件加速。但是压缩比来看，CPU的效果明显更好。从时间成本来看，GPU加速进行转码的话，速度极快。

1. **CPU转码**：

   - -i：指定源文件
   - -c:v libx265：指定视频编码为 libx265 ，也就是将视频重新编码为 H.265 格式。
   - preset medium：设置编码为 medium 。其实不指定也行，medium就是默认值。preset的设置会影响编码的速度和质量平衡，我实际测试过veryslow，质量并没有显著提高，medium是我认为最优的选项。
   - map_metadata 0：复制输入文件的元数据。
   - tag:v hvc1：为输出视频设置标签 hvc1。可以解决转码后的文件不被iPhone识别的问题。
   - <p>map 0:v:0</p>：从输入文件中选择第一个视频流。
   - map 0:a：保留所有的音频流。
   - map 0:s：保留所有的音频流。

   ```bash
   ffmpeg -i E:\2h265\XXXX.mp4 -c:v libx265 -preset medium -map_metadata 0 -tag:v hvc1 -map 0:v:0 -map 0:a E:\2h265_output\XXXX.mp4
   ```

2. **GPU转码（NVIDIA平台）**：

   - -c:v hevc_nvenc：使用NVIDA的GPU进行H.265编码，逻辑上和FFmpeg编译的版本有关系，不过我的NVDIA GeForce RTX 4060可以直接使用。

   ```bash
   ffmpeg -i E:\2h265\XXXX.mp4 -c:v hevc_nvenc -preset medium -map_metadata 0 -tag:v hvc1 -map 0:v:0 -map 0:a E:\2h265_output\XXXX.mp4
   ```

#### 我的转码程序

我的程序需要满足以下几项需求：
- 更高的压缩比，为了节省空间（省购买硬盘的钱）。
- 保留手机拍摄视频的时间戳及地理位置信息，同时需要解决IOS、安卓的兼容性，因为我是双持用户，照片会两处备份。
- 转码需要保留电影的多音轨、多字幕。

程序是基于python的实现，安卓上是通过Termux来运行的。虽然平台不同，但是实测转码结果相同。

1. **Windows版本**：

   [Windows版命令行转码工具]({{ site.url }}assets/2024/2024-07-20-ffmpeg-notes/h264_to_h265_tool.zip)

2. **安卓版本**：
   等写完再补充。

## 更新日志
- 2024年7月20日：初稿。