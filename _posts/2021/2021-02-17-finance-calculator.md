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

<h1>收益率计算器</h1>
<p>买入价格：<input type="text" id="mairujia"/>元</p>
<p>卖出价格：<input type="text" id="maichujia"/>元</p>
<p>持有年限：<input type="text" id="chiyounianxian"/>年</p>
<input type="button" value="计算" onclick="jisuanTwo(1)">
<input type="button" value="清空" onclick="jisuanTwo(2)">
<p>总收益率：<input type="text" id="zongshouyilv"/>元</p>
<p>年化收益率：<input type="text" id="nianhuashouyilv"/>元</p>

<script type="text/javascript">
// 计算收益率
function jisuanTwo(x){
    if(x==1){
        var mairujiaNum = document.getElementById("mairujia").value;
        var maichujiaNum = document.getElementById("maichujia").value;
        var chiyounianxianNum  = document.getElementById("chiyounianxian").value;

        console.log(mairujiaNum);
        console.log(maichujiaNum);
        console.log(chiyounianxianNum);
        // 这里是总收益率，后面是%，所以要*100；
        var zongshouyilv = (maichujiaNum - mairujiaNum)/mairujiaNum * 100;
        console.log(zongshouyilv);
        document.getElementById("zongshouyilv").value = zongshouyilv.toFixed(3);

            var nianhuashouyilv = Math.pow(maichujiaNum/mairujiaNum, 1/chiyounianxianNum)-1;
            console.log(nianhuashouyilv);

        document.getElementById("nianhuashouyilv").value = (nianhuashouyilv*100).toFixed(3);
    }else if(x==2){
        document.getElementById("mairujia").value = "";
        document.getElementById("maichujia").value = "";
        document.getElementById("chiyounianxian").value = "";
        document.getElementById("zongshouyilv").value = "";
        document.getElementById("nianhuashouyilv").value = "";
    }

}
</script>

<h1>最终收益计算器</h1>
<p>本金：<input type="text" id="benjin"/>元</p>
<p>年华收益率：<input type="text" id="shouyilv"/>%</p>
<p>投资年限：<input type="text" id="touzinianxian"/>年</p>
<input type="button" value="计算" onclick="jisuanOne(1)">
<input type="button" value="清空" onclick="jisuanOne(2)">
<p>最终收益：<input type="text" id="zuizhongshouyi"/>元</p>

<script type="text/javascript">
// 计算最终收益
function jisuanOne(x){
    if(x==1){
        var benjinNum = new BigNumber(document.getElementById("benjin").value);
        var shouyilvNum = new BigNumber(document.getElementById("shouyilv").value);
        var touzinianxianNum = new BigNumber(document.getElementById("touzinianxian").value);
        var shouyiNum = new BigNumber(1+shouyilvNum/100);
        var zuizhongshouyi = benjinNum.multipliedBy(shouyiNum.pow(touzinianxianNum)).valueOf();
        console.log(zuizhongshouyi);
        if(String(zuizhongshouyi).indexOf(".")==-1){
            document.getElementById("zuizhongshouyi").value =zuizhongshouyi
            console.log(zuizhongshouyi);
        }else{
            var splitArr = String(zuizhongshouyi).split('.');
            document.getElementById("zuizhongshouyi").value =splitArr[0]+'.'+splitArr[1].substr(0,3);
            console.log(zuizhongshouyi);
        }
    }else if(x==2){
        document.getElementById("benjin").value = "";
        document.getElementById("shouyilv").value = "";
        document.getElementById("touzinianxian").value = "";
        document.getElementById("zuizhongshouyi").value = "";
    }

}
</script>


<h1>非劳动收支平衡计算器</h1>
<p>本金：<input type="text" class="benjin"/>元</p>
<p>月定投：<input type="text" class="dingtoujine"/>元</p>
<p>年华收益率：<input type="text" class="nianhuashouyi"/>%</p>
<p>月支出：<input type="text" class="yuezhichu"/>元</p>
<input type="button" value="计算" onclick="jisuanFour(1)">
<input type="button" value="清空" onclick="jisuanFour(2)">
<p>月均获得收益：<input type="text" class="yueshouyi"/>元</p>
<p>非劳动收支平衡所需时间：<input type="text" class="time"/></p>

<script type="text/javascript">
// 非劳动收支平衡
function jisuanFour(x){
    if(x==1){
        var benjin = $(".benjin").val();
        var dingtoujine = $(".dingtoujine").val();
        var nianhuashouyi = $(".nianhuashouyi").val();
        var yuezhichu = $(".yuezhichu").val();

        var monthYield = Math.pow(1 + nianhuashouyi / 100, 1 / 12) - 1;
        var month = 0
        var income = 0
        do{
            month++
            var gain = (dingtoujine * (1 + monthYield) * (Math.pow(1 + monthYield, month) - 1)) / monthYield
            var earning = benjin * Math.pow(1 + monthYield, month)
            income = (gain + earning) * monthYield
        }while(yuezhichu > income)
        $(".yueshouyi").val(income.toFixed(2));
        $(".time").val(Math.floor(month / 12)+'年'+month % 12+'个月');
    }else if(x==2){
        document.getElementsByClassName("benjin")[0].value = "";
        document.getElementsByClassName("dingtoujine")[0].value = "";
        document.getElementsByClassName("nianhuashouyi")[0].value = "";
        document.getElementsByClassName("yuezhichu")[0].value = "";
    }

}
</script>