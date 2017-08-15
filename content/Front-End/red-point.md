Title: 图标右上角显示红点
Date: 2016-04-14 20:29
Modified: 2016-04-14 20:29
Tags: front-end
Slug: red-point
Authors: Henry Chen
Status: published

[TOC]

其实我是想做后端的，其实我是得工作的，来吧，搞前端.  
在一个图标上显示个红点，红点里现实数字

``` html
<div class="wrap">
  <div class="img"></div>
  <div class="notice">1</div>
</div>

<div class="wrap">
  <div class="img"></div>
  <div class="notice">12</div>
</div>

<div class="wrap">
  <div class="img"></div>
  <div class="notice">13</div>
</div>
<style>
  .wrap {
    width:50px;
    margin-bottom:10px;
    position:relative;
  }
  .img {
    width:50px;
    height:50px;
    border:1px solid #000;
  }
  .notice {
    width:20px;
    height:20px;
    line-height:20px;
    font-size:10px;
    color:#fff;
    text-align:center;
    background-color:#f00;
    border-radius:50%;
    position:absolute;
    right:-10px;
    top:-10px;
  }
</style>
```

效果：
<div class="wrap">
  <div class="img"></div>
  <div class="notice">1</div>
</div>

<div class="wrap">
  <div class="img"></div>
  <div class="notice">12</div>
</div>

<div class="wrap">
  <div class="img"></div>
  <div class="notice">13</div>
</div>
<style>
  .wrap {
    width:50px;
    margin-bottom:10px;
    position:relative;
  }
  .img {
    width:50px;
    height:50px;
    border:1px solid #000;
  }
  .notice {
    width:20px;
    height:20px;
    line-height:20px;
    font-size:10px;
    color:#fff;
    text-align:center;
    background-color:#f00;
    border-radius:50%;
    position:absolute;
    right:-10px;
    top:-10px;
  }
</style>
