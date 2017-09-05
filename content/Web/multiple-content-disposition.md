Title: ERR_RESPONSE_HEADERS_MULTIPLE_CONTENT_DISPOSITION 
Date: 2017-09-05 21:56
Modified: 2017-09-05 21:56
Tags: web
Slug: err-response-headers-multiplue-content-disoposition
Summary: mutiple content disposition
Authors: Henry Chen
Status: published

[TOC]

## 背景
有个下载功能，一直好好的，今天点击下载突然这样了: 

![static/images/web/err-response-mutiple-content-disposition](/static/images/web/err-response-mutiple-content-disposition.jpeg)

页面上的错误code是: ERR_RESPONSE_HEADERS_MULTIPLE_CONTENT_DISPOSITION



## 原因

相应头中设置了

```

Content-Disposition: attachment; filename=filename.html
```

filename中包含逗号



## 解决

### 方案1

去掉filename中的逗号


### 方案2

给filename.html两边加引号, 就像这样: 

```

Content-Disposition: attachment; filename="filename.html"
```
