---
layout: post
title:  "测试团队如何更好的的保证软件产品质量——MTSC2019有感"
date:   2019-07-13 15:04:16 +0800
subtitle:   ""
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - 杂文
---

由于单位有MTSC2019的票，所以有幸听到了科大讯飞AI营销业务群测试架构师孙玉的分享《打破职能局限-科大讯飞百亿级交互业务的缺陷预防之路》。

本来以为是一个技术分享，去了之后才发现其实讲的是质量保证，即跳出测试本身的职能，同时带有QA的角色成分进行缺陷预防，从而实现质量保证。其实这与在**LY姐**带领下的京东物流开放平台测试团队在质量保证这条路上的探索方向有异曲同工之妙。

## QA？QC？反正我之前是傻傻分不清

在聊具体内容前，我想先聊一下什么是QA(Quality Assurance)，QC(Quality Control)。我以前一直以为都是保证质量嘛，应该是一个东西咯。后来和单位的大佬**R哥**聊过之后才意识到这俩根本不是一个东西。QA和QC都是在ISO 9000中提出的一个概念。ISO 9000系列标准是国际标准化组织设立的标准，与品质管理系统有关。一般来讲若一个企业通过了ISO 9000的标准，就可以表示他们的产品是通过一个有品质的规范化标准的流程下诞生的，那么可以说是有品质保证的。一般来讲在制造、信息技术、科技服务等很多行业都会有ISO的身影。ISO 9000目前发展到ISO 9000:2015，从[官网](https://www.iso.org/obp/ui/#iso:std:iso:9000:ed-4:v1:en:term:3.3.6)中我们可以了解到QA和QC的定义。

- quality assurance: part of quality management focused on providing confidence that quality requirements will be fulfilled.
- quality control: part of quality management focused on fulfilling quality requirements.

所以QA要做的事请贯穿了整个软件产品的研发生命周期。而QC做的则是软件产品研发完成后，正式投入使用前的检查。所以说软件测试团队的职责是QC。我了解到的，我们单位的QA的一部分工作是制定软件产品整个研发生命周期的一些标准，比如过程中要输出的文档啊，过程中的各种流程规范啊等等。

## 现在测试团队职责是什么？

窃以为抛开社会大环境，抛开所处小环境谈定位谈职责就是耍流氓。

从社会大环境看。在软件行业的蛮荒时代，哪要什么测试。只要功能人无我有，那我就牛逼。而现在呢？“可别出线上问题”、“客户可别投诉啊”、“测试通过了没有？”。质量越来越重要。

而从所处小环境来看。如果一个初创公司，或者是一个新组建的小团队，可能就不需要复杂的流程和制度，重要的是为团队找到靠谱的人才。而团队成长到一定规模，就势必要规范化。

所以，对于大厂的具备一定规模的研发队伍来说，测试不是单纯的发现程序问题，更重要的是在有限的资源下如何规范的专业的守护软件系统的质量。

传统的测试团队是在软件产品研发完成后，再进行测试。但我们都知道Bug发现的越晚，修复的成本就越高。所以如果有些问题，能够前置解决，那么对公司的成本控制就会更有帮助。毕竟现在已经进入资本寒冬了，大家都要勒紧裤腰带过生活。所以现在测试团队也需要做质量过程管理的事请，即讲缺陷预防引入到整个产品的研发流程中。QA从宏观进行把控，而QC作为质量管理的一环，又是与研发产品同事协同工作的人或许在一些点上比QA更有优势。

或许同去MTSC的**Y哥**用一句简单的话说出了真相“现在测试团队要做的就是帮助提升产品和研发的工作质量。”

## 现有的工作流是什么样的？

没有调研别的大厂的工作流是什么样的，不过我们和科大讯飞的这个ppt里的基本一致，我就做个伸手党不自己做图了。

![工作流]({{ site.url }}assets/2019-07-13-impressions-of-MSTC2019/20190713164816.webp)

对了，为了方便描述，后文中的A团队就是我们团队。B团队指的是科大讯飞AI营销业务群的测试团队。

## “需求阶段”的改善

B团队在这个阶段，做了两点。
1. 需求拆分
2. 需求测试

所谓需求拆分就是对需求进行解耦，因为大型需求往往伴随着预估时间不准确，影响范围大，方案更容易产生漏洞。这种拆分后的小轻快的需求可以快速开发上线。其落实人员为产品经理，测试则负责推进和辅助。

所谓需求测试，就是在coding前先过一下该需求的整体设计方案，找出需求本身的问题。落实人员为测试人员。不过B团队在做这件事的时候遇到了一些问题还没有解决：

1. 占用大量时间，变更后，又得重新测试
2. 需求问题各方争执不下，难以定论
3. 产品对需求测试产生了依赖

关于以上两点，A团队并没有做“需求拆分”，原因是A团队的业务特征，往往一个项目很大，会涉及整个很长的业务流程，这时候光参与的产品经理就有6、7人。这种项目就不适合拆分。而一些小需求的话，本身就不大，也就没有必要拆分。

关于“需求测试”，A团队也在做。不过并没有遇到B团队分享出的这些问题。我觉得究其原因，主要是因为A团队没有用力过猛。B团队会针对需求进行测试同时输出一个叫做“测试框架”的思维导图，且其需求测试还带有“是否最优设计”的目的。这两点会直接引起问题1和问题2。

A团队的做法是这样的，“需求测试”直接在需求评审时做，但是目的只有一个即“方案是否有漏洞”。若有漏洞则评审不通过，且记录在案，后续对产品经理的绩效可能会造成影响，这就解决了问题3；同时因为不输出额外的东西，而需求评审本身就是应该有的流程，故解决了问题1；因为术业有专攻，且很难有一个设计能满足所有情况，势必会有所取舍，所以“是否最优设计”不在我们考虑的范围内，我们可能会提出建议，但是不会撕这件事儿，也就解决了问题2。

## “设计阶段”的改善

B团队在这个阶段，主要做了一个叫做“jira交付规范”的事情，其实就是研发在开发过程中将接口文档及设计文档上传至jira平台。该工作的落实人员是研发人员。分享中提到了一个很有趣的现象，说是大部分的研发人员习惯边做边想，最后的结果就是除了代码一无所有，这导致在了解一些逻辑的时候，只能“扒代码”😓。关于这个观点我深以为然，其实不止研发，我自己写工具的时候也基本上是这样的。对此A团队的做法是推动研发进行概要设计评审，即在测试开始前研发讲一下他的具体实现，这样在测试开始前可以先检查一下实现思路是否有问题，避免测试资源的盲目投入，同时可以了解一些实现的具体细节。测试是也可以更游刃有余。不过现在刚开始推行，还不清楚具体的效果。

## “编码阶段”的改善

B团队在这个阶段，做了两点。
1. 构建“版本质量考核体系”。
2. 提出“版本发布构建规范”。

### “版本质量考核体系”

针对第一点的构建“版本质量考核体系”，B团队在其研发团队内部制定了质量考核标准，同时进行月度的缺陷统计，并且根据统计记录会有相应的考核评分从而落实绩效的奖惩机制。****以此来敦促研发自测，消灭低级缺陷。****这里B团队做的很棒的点就是“合理的考核标准”及“弹性拔高标准”。首先考核标准要指定的合理，符合当前团队的质量现状，不能标准指定太高然后大家都达不到。当研发的质量成长起来之后也要适度提高标准，即时刻留有上升的空间。很合理，不过这里在真正实施的时候可能会面临两个问题。
1. 质量考核标准的维度单一。
2. 考核标准的提高可能会面临阻力。

第一个问题`质量考核标准的维度单一`，单纯从公布出来的PPT上来看。只是根据总工时以及几种严重程度的缺陷数量来评分A-E的5个等级。首先单薄的考核维度并不能全方位的展现研发团队的质量，同时将考核重点聚焦到缺陷数量和严重程度上，且考核结果与绩效挂钩容易引起研发和测试之间的对立关系。最后的结果可能是缺陷记录不准确导致质量分不准确，或者研发及测试团队的关系持续恶化。在ISTQB中提到过`测试的心理学`的概念，抛出过这样的观点`测试过程中发现的失效，可能会被看成是测试员对产品和作者的指责。`【“我发现了一个bug” VS “我觉得这里和预期不太一致”😀】所以测试很有可能会被认为是一种破坏性的活动。面对这种不可避免的现象，我个人的理解是一方面提高我们测试人员自身的人与人之间沟通的能力。另一方面就是在“规则”制定的时候尝试回避矛盾，而不是制造矛盾，毕竟无论测试还研发要协作为了服务于输出好的产品。

第二个问题`考核标准的提高可能会面临阻力`，人都有惰性，当考核标准提搞时，势必会引起研发的反对。而按照传统配比来说，往往一个测试部门对应多个研发部分，所以想要提高考核标准可能真的很难。

说起****敦促研发自测，消灭低级缺陷****这件事，我一直觉得我们的研发也有提升的空间。之前我们A团队在此做出的尝试是要求研发给出自测记录（日志，报文，截图等）。但是实际效果比不是很好，别的团队我不太清楚，但是我面临的现状是研发本身不了解上下游的业务逻辑，只清楚自己开发的这部分功能，这样在开发的过程中就不会特意去考虑上下游基于业务的调用，即使自己自测通过了，也没办法屏蔽串流程联调时的一些业务维度的低级缺陷。我的思考是，面对这种情况，本身需要研发负责人对于整体业务有相当强的掌控，从而在进行研发任务分配时就考虑到任务之间的关联关系，提前做好预防。

既然聊到了质量考核体系，可以稍微说下A团队对于质量考核体系的构建，研发团队的质量分由“过程质量”及“线上质量”两部分组成。SEPG给出线上质量分。测试团队给出的是过程质量分。过程质量包含5个方面，13个评分点。涵盖提测质量、缺陷数量及严重程度、研发对于缺陷的修正速度、代码实现方案的变更、上线及UAT事故等诸多方面。同时按照月为单位输出质量报告。不干预研发团队的绩效考核，只输出质量报告供其参考。

### “版本发布构建规范”

B团队在提测版本控制上面对的问题是：
1. 版本内容漏写，错写。
2. 改动的影响范围不明确。
3. 业务联动不说明。
4. 代码提交有遗漏或者多余。

关于这部分内容我还有一些点没有想明白，比如“如何合理管理版本和分支”、“如何实践DevOps”等等。先照本宣科B团队在PPT中展示的他们的应对手段：
1. 有序的发版制度：串行或者并行，不同的研发模式有着不同的发版方式。
2. 规范CI构建说明：研发人员需要在构建时说明目的、开发/设计范围、新增/修改说明、已知问题、联调范围。
3. Diff代码：重视每一行提交的代码。

不太清楚B团队具体在技术上实现到了什么程度，我理解主要是通过Checklist的形式，让研发人员在提测时自行进行梳理。减少提测过程引入的缺陷。

这种A团队也有`研发提测清单`、`研发上线配置清单`等。其实这里我更想了解的是如何实践DevOps(Development&Operations)。因为随着社会的高速发展，需求方对于软件研发团队的要求也越来越高，我们要有能力应对频繁的需求变化，还要保证质量的前提下做到快速开发。所以软件开发模型也从传统的瀑布模型，经历了敏捷开发模型，中遇到DevOps开发模型。要做到DevOps，就要离不开CI(continuous integration持续集成)/CD(continuous delivery持续交付)。不是说部署了一个CI服务器，Jenkins之类的就是持续集成了。CI的实践离不开人的行为规范(如研发代码提交规范)，也离不开自动化回归测试、代码静态扫描等。我们A团队应该也没有实现真正意义上的持续集成。我们的研发团队还是会按照不同的需求和项目，拉出不同的开发分支，提测时合并到测试分支，测试通过后合并到开发分支这种传统套路。不过以后我们应该也会走上CI/CD，DevOps这条路上吧。因为现在我们测试团队正在紧锣密鼓的丰富着我们的自动化测试用例，时机成熟之时，便是实践DevOps之日吧，哈哈哈

另附一些DevOps的文章：
- [对于持续集成实践的常见问题的解答](https://www.jianshu.com/p/c17ba58f4c74)
- [从无到有：京东持续集成实践分享](http://mini.eastday.com/mobile/180207224805430.html)
- [为什么大公司一定要使用DevOps?](https://blog.csdn.net/g6U8W7p06dCO99fQ3/article/details/82056948)

## “测试阶段”的改善

B团队在这个阶段，做了“缺陷复盘”。分析缺陷起因，进行人员缺陷统计，缺陷类型统计，最后输出复盘总结报告。从而对研发人员进行指导。

对应的，A团队的行为是前文提到的“月度质量报告”。同时针对典型项目，也会展开针对整个项目的专题分析。不只分析测试发现的缺陷，还会分析UAT过程中发现的缺陷以及整个测试过程。从而对研发及测试人员进行指导。有时还会梳理出一些流程上的改善意见，进而辅助整个团队的提升。

## 其它改善

B团队还做了“版本力度精准切割”。也就是当版本之间间隔较远时，会导致改动功能点太多，合并的代码量级较大。从而无法确定影响范围，也更容易引入缺陷。从B团队给出的数据来看，当版本小且多的时候，缺陷数量明显减少。这其实和CI有一曲同工之妙，研发减少分支的数量，而是持续提交可以编译的代码，CI服务器检测代码变动，同时定时编译并执行自动化回归测试，最后给出报告。这样可以将潜在Bug提前暴露，同时减少了研发后期合并分支时大量待合并文件带来的痛苦。所以，还是要走DevOps，哈哈哈

## 写在最后

谢谢，感谢可以看到这里的看官。也感谢为了完成这篇文章我讨教过的各位大佬、前辈。推翻了好多次，终于写完了。过程中收获很多，每次和前辈们讨教时就会意识到自己的想法是多么的幼稚。现在依然觉得自己来写个很不够格，如履薄冰、忐忑不安的心情谁懂😅

另附:
- ![打破职能局限-科大讯飞百亿级交互业务的缺陷预防之路-孙玉-0622_pub.pdf]({{ site.url }}assets/2019-07-13-impressions-of-MSTC2019/pdf.pdf)