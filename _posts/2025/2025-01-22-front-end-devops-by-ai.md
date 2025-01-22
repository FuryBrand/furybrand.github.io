---
layout:     post
title:      "xin法-实战前端工程维护"
date:       2025-01-14 19:33:00
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - 技术相关
    - JS
    - xin实践
---

> 组内现在没有前端同学，之前的工程是从其他组协调前端同学支持开发的。招聘一直不顺利，导致现在项目二期的时候又去借人，然后由于框架不同，又起了一个新工程......如果再这么搞，后面就是屎山代码无疑了。而且协调资源这个事情不牢靠，得遵循人家的排期和优先级。所以基于底线思维，我准备熟悉一下前端，尝试在AI的帮助下自己修改逻辑。本次的需求非常简单，修改一个后台跳转按钮的展示逻辑，如果是管理员就展示该按钮。这里做一个笔记，好帮助组内和其他遭遇类似处境的同学。

## 1. 确认该前端工程所使用的技术栈

我这个工程有一个简单的`README.md`，节省了我们该步骤的时间。如果没有这些，可以尝试通过工程内的目录结构询问AI，得到技术栈的信息。

```markdown
# Vue 3 + TypeScript + Vite

This template should help get you started developing with Vue 3 and TypeScript in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

## Recommended Setup

- [VS Code](https://code.visualstudio.com/) + [Vue - Official](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (previously Volar) and disable Vetur

- Use [vue-tsc](https://github.com/vuejs/language-tools/tree/master/packages/tsc) for performing the same type checking from the command line, or for generating d.ts files for SFCs.

### Get Start

node -v >=18

npm install pnpm

pnpm install

pnpm run dev
```

基于上述的`README.md`，在AI的帮助下，我们了解到了一些关键信息。该工程使用了Vue3和TypeScript技术，并且使用Vite作为编译打包工具。开发工具使用的是VS Code + Vue插件。我们需要先安装node，然后通过node的包管理工具npm安装pnpm，然后pnpm会基于`package.json`、`pnpm-lock.yaml`文件安装相关依赖。最后用`pnpm run dev`命令，就可以在本地启动了。

## 2. 准备系统环境并了解前端工程如何启动

- [Node.js官网](https://nodejs.org/zh-cn)下载安装包并安装。 
- 命令行执行`npm install pnpm`
- 命令行执行`pnpm install`
- 命令行执行`pnpm run dev`

看似很简单，但是其实每一步都可能有坑，但是不要紧，在思路整体明确，大方向确定的前提下，只需要一个一个问题去解决就好了。AI是个博学的好老师，但是他也有他的局限性，当前主流的与LLM交互的方式还是文本。对比人类他虽然有海量的知识，但是他缺少信息收集的媒介，在沟通时对问题掌握的信息就不全，更何况他还可能有“幻觉”。所以现阶段人类和AI搭配才能极大的提升生产力。

扯远了，回来，我当时在执行`pnpm run dev`的时候报错如下。

```bash
liutianyu@ZB-BL657NBY MINGW64 /x/coding/Edge (master)
$ pnpm run dev

> edge@1.0.0 dev X:\coding\Edge
> vite

error when starting dev server:
Error: listen EADDRNOTAVAIL: address not available 36.110.181.172:8080
    at Server.setupListenHandle [as _listen2] (node:net:1915:21)      
    at listenInCluster (node:net:1994:12)
    at GetAddrInfoReqWrap.callback (node:net:2203:7)
    at GetAddrInfoReqWrap.onlookupall [as oncomplete] (node:dns:132:8)
 ELIFECYCLE  Command failed with exit code 1.
```

尝试在代码库中寻找`36.110.181.172`无果。于是我递进式的问了以下几个问题。

```txt
----------------------------------------------------------------------------------------
## 对话1：执行pnpm run dev命令后，系统自动做了哪些动作

## 回答：

执行 pnpm run dev 命令后，系统会自动执行以下动作：

读取 package.json 文件：

pnpm run dev 会首先查找项目根目录下的 package.json 文件，以找到与 dev 相关的脚本命令。
查找 scripts 字段：

在 package.json 文件中，pnpm 会查找 scripts 字段下的 dev 脚本。这个字段通常定义了一系列可以通过 pnpm run <script> 执行的命令。
执行指定的命令：

一旦找到 dev 脚本，pnpm 会执行该脚本中定义的命令。这通常是启动开发服务器的命令，例如 vite、webpack-dev-server、next dev 等，具体取决于项目的构建工具和配置。
例如，如果 dev 脚本是 "vite", 那么 pnpm run dev 实际上是在执行 vite 命令，启动 Vite 开发服务器。
启动开发环境：

根据 dev 脚本的定义，通常会启动一个开发服务器。这可能包括以下动作：
编译和打包源代码。
监听文件变化并进行热重载（Hot Module Replacement）。
在浏览器中打开项目的开发地址（通常是 http://localhost:3000 或其他端口）。
处理依赖：

在执行过程中，pnpm 可能会解析和加载项目的依赖，确保所有必要的包都可用。
如果开发服务器需要的依赖没有安装，通常会出现错误提示。
输出日志信息：

pnpm 和开发服务器会在终端中输出相关的日志信息，包括编译进度、错误信息、警告以及开发服务器的运行地址等。
通过这些步骤，pnpm run dev 为开发者提供了一个实时更新的开发环境，便于进行代码编写和调试。具体的行为可能会因项目的配置和使用的工具而有所不同。

----------------------------------------------------------------------------------------
## 对话2：package.json中的scripts如下：

“scripts”: {
“dev”: “vite”,
“build”: “vue-tsc && vite build”,
“preview”: “vite preview”,
“prepare”: “husky”,
“test”: “vitest”,
“test-unit”: “vitest -c vitest.unit.config.ts”,
“lint:eslint”: “eslint --cache --max-warnings 0 "{src,mock}//*.{vue,js,ts,tsx}" --fix",
“lint:prettier”: "prettier --write "src//.{js,ts,json,tsx,css,less,scss,vue,html,md}"",
“lint:stylelint”: "stylelint --cache --fix "src/**/.{vue,css,scss,postcss,less}" --cache --cache-location node_modules/.cache/stylelint/”,
“lint”: “pnpm lint:eslint && pnpm lint:prettier && pnpm lint:stylelint”
},

## 回答：

在 package.json 文件中，scripts 字段定义了一系列可以通过 pnpm run <script> 来执行的命令。这些脚本用于简化常见的开发任务。让我们逐一了解你提供的这些脚本的作用：

dev: "vite"

启动 Vite 开发服务器。运行 pnpm run dev 时，项目会在开发模式下启动，支持热重载，方便开发和调试。
build: "vue-tsc && vite build"

首先运行 vue-tsc 进行 TypeScript 类型检查，确保代码没有类型错误。
然后运行 vite build，使用 Vite 进行生产环境的构建，将项目打包为可部署的静态文件。
preview: "vite preview"

启动一个本地服务器来预览生产构建的内容。这通常用于在部署之前验证构建结果。
prepare: "husky"

用于初始化 Husky，以便在项目中设置 Git 钩子。通常在安装依赖后自动执行。
test: "vitest"

运行 Vitest 测试框架，执行项目中的测试用例。
test-unit: "vitest -c vitest.unit.config.ts"

使用指定的配置文件 vitest.unit.config.ts 运行 Vitest，通常用于单元测试。
lint:eslint: "eslint --cache --max-warnings 0 \"{src,mock}/**/*.{vue,js,ts,tsx}\" --fix"

使用 ESLint 对指定目录中的文件进行语法检查和修复。
--cache：启用缓存以加快后续运行速度。
--max-warnings 0：将警告视为错误。
--fix：自动修复可以修复的问题。
lint:prettier: "prettier --write \"src/**/*.{js,ts,json,tsx,css,less,scss,vue,html,md}\""

使用 Prettier 格式化指定目录中的文件。
lint:stylelint: "stylelint --cache --fix \"src/**/*.{vue,css,scss,postcss,less}\" --cache --cache-location node_modules/.cache/stylelint/"

使用 Stylelint 检查和修复样式文件。
--cache：启用缓存。
--fix：自动修复可以修复的问题。
--cache-location：指定缓存位置。
lint: "pnpm lint:eslint && pnpm lint:prettier && pnpm lint:stylelint"

依次运行 ESLint、Prettier 和 Stylelint，对项目进行全面的代码质量检查和格式化。
这些脚本帮助开发者自动化常见的开发任务，提高开发效率和代码质量。根据项目需求，可以自定义和扩展这些脚本。

----------------------------------------------------------------------------------------
## 对话3：vite的启动配置文件是什么

## 回答：
Vite 的启动配置文件通常是 vite.config.js 或 vite.config.ts，具体取决于你使用的是 JavaScript 还是 TypeScript。这个配置文件用于定义 Vite 的各种配置选项，包括开发服务器设置、构建选项、插件配置等。

典型的 Vite 配置文件结构
以下是一个简单的 vite.config.js 示例：

import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  server: {
    host: 'localhost',
    port: 3000,
    open: true, // 自动打开浏览器
  },
  build: {
    outDir: 'dist', // 输出目录
  },
});

如果你使用 TypeScript，可以使用 vite.config.ts：

import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  server: {
    host: 'localhost',
    port: 3000,
    open: true,
  },
  build: {
    outDir: 'dist',
  },
});

配置文件的常用选项
plugins: 用于配置 Vite 插件，例如 Vue、React 等框架插件。
server: 配置开发服务器选项，如 host、port、open（自动打开浏览器）等。
build: 配置构建选项，包括 outDir（输出目录）、rollupOptions（自定义 Rollup 选项）等。
resolve: 配置模块解析选项，如别名设置。
css: 配置 CSS 相关选项，如预处理器设置。
使用 Vite 配置文件
默认路径: Vite 会在项目根目录下自动寻找 vite.config.js 或 vite.config.ts。
自定义路径: 如果你的配置文件不在默认路径，可以使用 vite --config <path> 来指定配置文件位置。
这些配置选项可以根据项目的具体需求进行调整，以实现更复杂的功能和优化。Vite 的配置文件通过 defineConfig 函数来定义，这样可以获得更好的类型提示和错误检查，特别是在使用 TypeScript 时。

```

然后我在`vite.config.ts`中找到了如下配置：

```json
server: {
    host: 'local.xxx.com',
    port: 8080,
    open: true,
    proxy: {
      '^/camera/|^/event/|^/ws/|^/user/': {
        target: 'http://192.168.0.129:8000',
        changeOrigin: true,
        ws: true,
        headers: {
          referer: 'http://192.168.0.129:8000',
          origin: 'http://192.168.0.129:8000',
        },
      },
    },
  }
```

然后尝试`ping local.xxx.com`发现可达，且地址就是先前的`36.110.181.172`。那么就很明确了，估计前端同事在本地是有配置host的，那么解决方案就是：

A. 修改配置文件中的host为`127.0.0.1`或者`localhost`  
B. 配置本机的host文件，将local.xxx.com指向`127.0.0.1`

我选择了B选项，毕竟不修改代码、尽量贴近原始的开发环境显然出错的风险较低。

## 3. 学习前端工程的目录结构并尝试寻找需要修改逻辑的位置

事后来看，这部分消耗的时间几乎是最多的，我用了半天左右的时间研究代码，因为完全没有前端经验，所以阅读起来很费事。感觉本质是不具备前端工程的思维，这部分没有办法，只能硬嗑。下面记录下我当时的思路。

首先使用`dir /b`命令导出工程的根目录，然后和AI对话，学习每个文件夹的作用。为了方便，我直接把作用标记在下面了。
```txt
X:\coding\Edge>dir /b    
.eslintrc.cjs   `ESLint 配置文件，用于定义代码检查规则。`
.gitignore  `Git 忽略文件，指定哪些文件或文件夹不应被 Git 版本控制。`
.husky  `Husky 配置文件夹，用于 Git 钩子管理。`
.prettierignore `指定 Prettier 格式化时应忽略的文件。`
.prettierrc.cjs `Prettier 配置文件，用于代码格式化的规则。`
.stylelintrc.json `Stylelint 配置文件，用于 CSS 的代码检查。`
.vscode `VS Code 配置文件夹，通常包含项目特定的编辑器设置。`
cert    `可能存放证书文件，通常用于 HTTPS 开发环境。`
components.d.ts `TypeScript 的类型声明文件，可能是自动生成的，用于组件类型信息。`
dist    `构建输出文件夹，存放生产环境的打包文件。`
index.html  `项目的入口 HTML 文件。`
node_modules    `存放通过 npm 或 pnpm 安装的依赖包。`
package.json    `项目的元数据文件，包含项目的依赖、脚本和其他配置信息。`
pnpm-lock.yaml  `pnpm 的锁定文件，确保项目依赖的一致性。`
postcss.config.js   `PostCSS 的配置文件，用于处理 CSS。`
public  `用于存放静态资源的文件夹，直接复制到构建输出中。`
README.md   `项目的自述文件，通常包含项目的简介、安装和使用说明。`
src `项目的源代码文件夹，包含应用的主要代码。`
stats.html  `可能用于性能分析或构建报告的 HTML 文件。`
tailwind.config.js  `Tailwind CSS 的配置文件，用于自定义 Tailwind 的主题和插件。`
tsconfig.json   `TypeScript 配置文件，定义 TypeScript 编译器的选项。`
tsconfig.node.json  `通常是为 Node.js 环境定制的 TypeScript 配置。`
vite.config.ts  `Vite 的配置文件，用于定义构建和开发服务器的设置。`
vite.config.ts.timestamp-1724318016989-dd586d9058247.mjs    ``
vitest.config.ts    `用于 Vitest 测试框架的配置文件。`
vitest.unit.config.ts   `用于 Vitest 测试框架的配置文件。`
```

ok，那么源代码应该在src文件夹中。
```txt
X:\coding\Edge>cd src 

X:\coding\Edge\src>dir /b
App.vue `这是 Vue.js 应用的根组件。通常包含应用的基本布局和路由出口（router-view）。`
assets  `存放静态资源，如图像、字体等。通常会通过 Webpack 或 Vite 进行处理和打包。`
auto-imports.d.ts   `自动生成的类型声明文件，通常用于自动导入功能的类型支持。这可能与某些插件（如 unplugin-auto-import）相关。`
components  `存放可复用的 Vue 组件。组件是应用的基本构建块，通常用于封装 UI 元素和逻辑。`
layout  `存放应用的布局组件。这些组件通常定义应用的整体结构，如导航栏、侧边栏、页脚等。`
locales `存放国际化（i18n）资源文件，通常是 JSON 或 JavaScript 文件，用于多语言支持。`
main.ts `应用的入口文件。在这里初始化 Vue 实例，注册全局组件、插件，并挂载到 DOM。`
router  `存放路由配置文件。通常包含一个定义应用路由的文件（如 index.ts），使用 Vue Router 来管理页面导航。`
services    `存放与业务逻辑相关的服务代码，通常用于与后端 API 交互、数据处理等。`
stores  `存放状态管理相关文件，通常使用 Vuex 或 Pinia 来管理应用的全局状态。`
styles  `存放全局样式文件，如 CSS、SCSS 等。可以包含应用的主题、变量和混入等。`
types   `存放 TypeScript 类型定义文件，通常用于定义接口、类型别名和其他类型相关的内容。`
utils   `存放工具函数和辅助库。这些函数通常是与业务无关的通用功能。`
views   `存放页面级组件，这些组件通常对应于路由定义的页面。`
vite-env.d.ts   `Vite 的环境变量类型声明文件，通常用于扩展 TypeScript 对 Vite 特定环境变量的支持。`
__tests__   `存放测试文件。通常使用 Jest、Vitest 或其他测试框架进行单元测试、集成测试等。`
```

接下来就是死磕的重点，太长了我就不附对话记录了，重点说下问的思路。
- 问AI页面展示是通过哪些文件组合展示出来的
- 然后把可能的文件粘给AI让他帮忙做解读
- 如果解读的太粗略，就请AI用语法的维度做更细致的解读

这样一点点抽丝剥茧，就可以定位到要修改的位置了。我大致记录下自己通过这个经历后，对前端工程的一个初步认识。

关于文件的具体阅读顺序： 
1. src\main.ts，是初始化文件，在我手上的工程中设置和初始化一个 Vue.js 应用程序，包括状态管理、路由和样式。文件中用到了'./router'、'./App.vue'。使用App.vue加载了touter
2. src\App.vue，设置了应用程序的全局配置，包括语言包和自定义的本地化配置，并使用 Element Plus 的组件来实现。
3. src\router\index.ts，router文件夹下只有这一个文件，这个文件整体上定义了一个基本的路由系统，并提供了动态添加路由和全局路由守卫的机制。实际在这里发现了一些视图组件`*.vue`和一个用户管理模块`import { useUser } from '@/stores'`
4. 由于我是要修改一个按钮的展示逻辑，所以就在组件中继续挖，找到了`SideBar.vue`。

关于VUE3的一些特性：
- 响应式数据：在 Vue.js 中，响应式数据是指当数据发生变化时，相关的视图会自动更新的数据。这种机制允许开发者专注于业务逻辑和数据管理，而不需要手动操作 DOM 来更新视图。
- 生命周期钩子：Vue 3 的生命周期钩子包括 beforeCreate、created、beforeMount、mounted、beforeUpdate、updated、beforeUnmount、unmounted 等，用于在组件的不同阶段执行特定的逻辑。（用大白话讲就是页面元素被触发时会同步触发我们写好的逻辑）


## 4. 尝试修改逻辑并测试代码

`SideBar.vue`中定义了我要修改的按钮的展示逻辑，当前是通过userStore.url是否为空决定的。

此处引入一个新概念`Pinia`：
- Pinia 是 Vue 3 中的一种状态管理库，它被设计为 Vuex 的替代方案，提供了一种更现代、更轻量级的方式来管理应用程序的状态。
- Pinia 中最核心的概念是 Store。Store 是 Pinia 的基础单元，用于管理应用程序的状态。每个 store 都是一个独立的模块，可以包含状态（state）、派生状态（getters）和改变状态的方法（actions）。

由于需求是我需要用登录系统的用户角色判断一个按钮是否展示，所以去看了下userStore的属性，然后在User相关代码里新增了一行`console.log(role, site, userid, username, configurl)`。

使用`pnpm run dev`启动工程尝试调试，发现了role的具体值，然后就是改原来的逻辑，将userStore.url的判断改为userStore.role的判断。

再次测试，ok，没问题


## 5. 学习前端工程如何打包

直接问到了答案，就一个命令`pnpm run build`就可以。

```bash
liutianyu@ZB-BL657NBY MINGW64 /x/coding/Edge (master)
$ pnpm run build

> edge@1.0.0 build X:\coding\Edge
> vue-tsc && vite build

vite v5.2.11 building for production...
transforming (7) src\router\index.tsBrowserslist: caniuse-lite is outdated. Please run:
  npx update-browserslist-db@latest
  Why you should do it regularly: https://github.com/browserslist/update-db#readme
✓ 1615 modules transformed.
dist/assets/pinia-legacy-AaEUKLuD.js             3.74 kB │ gzip:   1.87 kB
dist/assets/@vueuse/core-legacy-BtJbpWYn.js      3.87 kB │ gzip:   1.91 kB
dist/assets/index-legacy-Bu8rlQgE.js             6.26 kB │ gzip:   3.13 kB
dist/assets/index-legacy-B2FL9NkE.js             9.81 kB │ gzip:   4.22 kB
dist/assets/vue-router-legacy-DjPqxA3w.js       22.77 kB │ gzip:   9.01 kB
dist/assets/manual-monitor-legacy-21OfHFM-.js   34.71 kB │ gzip:  10.55 kB
dist/assets/index-legacy-Bx7DxTqD.js            41.71 kB │ gzip:   9.42 kB
dist/assets/polyfills-legacy-CloPzPML.js        47.34 kB │ gzip:  18.66 kB
dist/assets/vue-legacy-rvlWBwQr.js             105.20 kB │ gzip:  39.96 kB
dist/assets/video-monitor-legacy-DdGQ5CQs.js   364.61 kB │ gzip:  93.13 kB
dist/assets/element-plus-legacy-BrGRby7B.js    433.86 kB │ gzip: 137.17 kB
dist/index.html                            2.86 kB │ gzip:   1.14 kB
dist/assets/img-DGGNUpYF.png              11.50 kB
dist/assets/login_bg-CWzTXAxG.webp       232.57 kB
dist/assets/index-CrpbdW4S.css             1.33 kB │ gzip:   0.60 kB
dist/assets/index-M5Ong37e.css             1.41 kB │ gzip:   0.57 kB
dist/assets/index-9V8B37-U.css             6.22 kB │ gzip:   1.99 kB
dist/assets/manual-monitor-CBT3uaAD.css   14.27 kB │ gzip:   3.15 kB
dist/assets/video-monitor-4QQwoTR2.css   140.80 kB │ gzip:  20.94 kB
dist/assets/pinia-DzOI_rpy.js              3.66 kB │ gzip:   1.88 kB
dist/assets/@vueuse/core-J9Te5kc0.js       3.79 kB │ gzip:   1.91 kB
dist/assets/index-DQlIsuG9.js              4.76 kB │ gzip:   2.51 kB
dist/assets/index-B-omhTdP.js              5.49 kB │ gzip:   2.98 kB
dist/assets/manual-monitor-DCJul52a.js    20.59 kB │ gzip:   7.68 kB
dist/assets/vue-router-0Z6UGjoa.js        23.12 kB │ gzip:   9.43 kB
dist/assets/index-Bwt9aLT2.js             40.17 kB │ gzip:   8.77 kB
dist/assets/vue-BUczWptF.js              106.70 kB │ gzip:  41.75 kB
dist/assets/video-monitor-VuL7gF2g.js    224.50 kB │ gzip:  74.40 kB
dist/assets/element-plus-BxSyl5RP.js     443.41 kB │ gzip: 144.74 kB
✓ built in 30.89s
```

## 6. 发布及线上测试

这一步也比较简单了，观察一下之前打包好的文件结构，发现就是和`dist`文件夹的内容相同，直接扔到服务器上就可以了。只能说，很幸运，没有遇到别的问题。重启服务器后测试发现逻辑已经生效了。

ok，搞定~

## 7. 写在最后

我是用的是单位提供的`GPT-4o-0806`，之前coding的时候也用过`豆包`，我觉得在我的使用方法下，主流AI没有本质区别，因为他是Co-pilot，我是Pilot。

另外，和前端同学沟通之后，还有一种方式可以方便的定位代码，使用浏览器插件`Vue.js devtools`。但是我还没研究，有机会再分享一下。

## 更新日志
- 2025年1月14日：初稿