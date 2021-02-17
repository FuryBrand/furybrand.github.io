---
layout: post
title:  "财务计算器"
date:   2021-02-17 16:37:25 +0800
subtitle:   ""
author:     "Steve"
header-img: "img/home-bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - JS
    - 财务
---

<h1>定投计算器</h1>
<p>投资时长：<input type="text" id="DCA_Time"/>年</p>
<p>预期年化收益率：<input type="text" id="DCA_incomeRate"/>%</p>
<p>每月存入：<input type="text" id="DCA_pay"/>元</p>
<input type="button" value="计算" onclick="DCA_calc(1)">
<input type="button" value="清空" onclick="DCA_calc(2)">
<p>投资总收益：<input type="text" id="DCA_income"/>元</p>

<script type="text/javascript">
// 定投
function DCA_calc(x){
    if(x==1){
        var money = document.getElementById("DCA_pay").value; // 每月存入
        var per = document.getElementById("DCA_incomeRate").value; // 年化收益率
        var year = document.getElementById("DCA_Time").value; // 投资时长
        money = parseFloat(money);
        monthPer = Math.pow(1 + per / 100, 1 / 12) - 1;
        month = year * 12;
        // 投资总收益
        const DCA_income = money * (1 + monthPer) * (Math.pow(1 + monthPer, month) - 1) / monthPer
        document.getElementById("DCA_income").value = DCA_income.toFixed(2);
    }else if(x==2){
        document.getElementById("DCA_pay").value = "";
        document.getElementById("DCA_incomeRate").value = "";
        document.getElementById("DCA_Time").value = "";
        document.getElementById("DCA_income").value = "";
    }


}
</script>
