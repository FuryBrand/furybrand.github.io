---
layout: post
title:  "这是一个测试jekyll上如何写html和js的测试页面"
date:   2019-06-26 23:20:25 +0800
categories: jekyll update
---

<style>
table{
border:1px solid #ccc;
border-radius: 3%;
padding:5px;
}
table tr td{
width:20px;
height:20px;
padding:5px;
text-align: center;
line-height:20px;
border: 1px solid #f9f9f9;
box-shadow: 0 0 3px rgba(0,0,0,0.9);
}
</style>
<table align="center">
<tr>
<td class="td_orange" colspan="5" id="content"></td>
</tr>
<tr>
<td class="td_orange" colspan="5" id="result"></td>
</tr>
<tr>
<td onclick="appContent(this)">1</td>
<td onclick="appContent(this)">2</td>
<td onclick="appContent(this)">3</td>
<td onclick="appContent(this)">*</td>
<td onclick="appContent(this)">/</td>
</tr>
<tr>
<td onclick="appContent(this)">4</td>
<td onclick="appContent(this)">5</td>
<td onclick="appContent(this)">6</td>
<td onclick="appContent(this)">+</td>
<td onclick="appContent(this)">-</td>
</tr>
<tr>
<td onclick="appContent(this)">7</td>
<td onclick="appContent(this)">8</td>
<td onclick="appContent(this)">9</td>
<td onclick="appContent(this)">(</td>
<td onclick="appContent(this)">)</td>
</tr>
<tr>
<td class="td_orange" onclick="appContent(this)">c</td>
<td onclick="appContent(this)">0</td>
<td onclick="appContent(this)">.</td>
<td onclick="appContent(this)">del</td>
<td class="td_orange" onclick="appContent(this)">=</td>
</tr>
</table>
<script>
function appContent(td){
//找到显示字符串等式的td标签
var content = document.getElementById("content");
//找到显示结果的td标签
var result = document.getElementById("result");
//获取字符串的等式
var text = td.innerText;
//如果是删除键
if("del" == text){
if(content.innerText.length > 0){
//删除最后一个字符
content.innerText = content.innerText.substring(0,content.innerText.length-1);
}
//如果是全部删除
}else if("c" == text){
content.innerText = "";
//如果是按了等于号
}else if("=" == text){
var resultText = parse(content.innerText);
result.innerText = content.innerText + "=" + resultText;
content.innerText = "";
//除了上面三种情况,其他的都是尾加
}else{
content.innerText = content.innerText + text;
}
}

/**解析字符串的等式为一个正确的结果*/
function parse(content){
//寻找最后一个左括号
var index = content.lastIndexOf("(");
//如果等式中有左括号
if(index > -1){
//寻找右括号,从左括号的位置开始寻找
var endIndex = content.indexOf(")",index);
//如果等式中有右括号
if(endIndex > -1){
//调用自己算出括号中的结果
var result = parse(content.substring(index + 1,endIndex));
//然后继续调用自己,
//其实这里完成的工作就是"2+3+(2+3*2)"转化成了"2+3+8",也就是用括号中的结果替换括号所在位置
return parse(content.substring(0,index) + ("" + result) + content.substring(endIndex + 1))
}
}
index = content.indexOf("+");
if(index > -1){
return parse(content.substring(0,index)) + parse(content.substring(index + 1));
}
index = content.lastIndexOf("-");
if(index > -1){
return parse(content.substring(0,index)) - parse(content.substring(index + 1));
}
index = content.lastIndexOf("*");
if(index > -1){
return parse(content.substring(0,index)) * parse(content.substring(index + 1));
}
index = content.lastIndexOf("/");
if(index > -1){
return parse(content.substring(0,index)) / parse(content.substring(index + 1));
}
if("" == content){
return 0;
}else{
return content - 1 + 1;
}
}
</script>
<p>请输入原数字串：<input type="text" id="sendpay" onblur="checkSendpay()"/></p>
<p>
    将第<input type="text" id="loc" onblur="checkLoc(this);"/>位的值，替换为<input type="text" id="newVal" onblur="checkNewVal()"/>（位数从0开始数）
    <input type="button" value="替换" onclick="replace()">
    <p>替换后的结果为：</p>
    <pan id="result"></pan>
</p>
<p>
    获取第<input type="text" id="getLoc"  onblur="checkLoc(this);"/>位的值（位数从0开始数）<input type="button" value="获取" onclick="getNum()">
</p>
<p>
    版本信息：
    Ver0.4：去掉了异常输入校验，增加了对chrome的兼容性。
</p>
<script type="text/javascript">
    /* function checkSendpay(){
        var sendpay = document.getElementById("sendpay").value;
        var re = new RegExp("^\\d{200}$");
        if(sendpay.match(re)){
            return true;
        }else{
            alert("输入的sendpay不合法,sendpay是200位的数字");
            window.setTimeout(function(){document.getElementById('sendpay').focus()},0);
            return false;
        }
    } */
/*             function checkLoc(x){
        var loc = x.value;
        var re = new RegExp("^0$|^[1-9]\\d?$|^1[0-9][0-9]$");
        if(loc.match(re)){
            return true;
        }else{
            alert("位数中请输入0-199之间的整数");
            window.setTimeout(function(){x.focus()},0);
            return false;
        }
    } */
    /* function checkNewVal(){
        var newVal = document.getElementById("newVal").value;
        var re = new RegExp("^[0-9]$");
        if(newVal.match(re)){
            return true;
        }else{
            alert("替换的数字只能是0-9的整数");
            window.setTimeout(function(){document.getElementById('newVal').focus()},0);
            return false;
        }
    } */
    function replace(){
        //checkSendpay();
        //checkLoc(document.getElementById("loc"));
        //checkNewVal();
        //var checkSendpay = checkSendpay();
        //if(checkSendpay()&checkLoc(document.getElementById("loc"))&checkNewVal()){
            var sendpay = document.getElementById("sendpay").value;
            var loc = document.getElementById("loc").value;
            var newVal = document.getElementById("newVal").value;
            var str1 = sendpay.substring(0,loc);
            var str2 = sendpay.substring(loc*1+1,sendpay.length);
            //alert(str1+""+newVal+""+str2);
            document.getElementById("result").innerHTML = str1+""+newVal+""+str2;
        //}
    }
    function getNum(){
        //checkLoc(document.getElementById("getLoc"));
        var sendpay = document.getElementById("sendpay").value;
        var loc = document.getElementById("getLoc").value;
        alert(sendpay.charAt(loc));
    }
</script>
