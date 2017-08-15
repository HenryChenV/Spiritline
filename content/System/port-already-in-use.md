Title: 查看哪个程序占用了端口
Date: 2016-04-14 11:43
Modified: 2016-04-14 11:43
Tags: system, port
Slug: port-already-in-use
Authors: Henry Chen
Status: published

[TOC]

``` bash
netstat -ntlp|grep 8000
lsof -i:8000 
ps -ef |grep `netstat -ntlp|grep 8000|awk '{print $7}'|awk -F/ '{print $1}'`
```
