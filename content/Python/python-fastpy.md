Title: fastpy 源码笔记
Date: 2016-03-12 20:22
Modified: 2016-03-12 20:22
Tags: python, web, notes
Slug: python-fastpy
Authors: Henry Chen
Status: draft

[TOC]


### 多进程进程数量

进程数一般等于cpu的核数


### 文件描述符fd

文件描述符（File
descriptor）是计算机科学中的一个术语，是一个用于表述指向文件的引用的抽象化概念。

文件描述符在形式上是一个非负整数。实际上，它是一个索引值，指向内核为每一个进程所维护的该进程打开文件的记录表。当程序打开一个现有文件或者创建一个新文件时，内核向进程返回一个文件描述符。在程序设计中，一些涉及底层的程序编写往往会围绕着文件描述符展开。但是文件描述符这一概念往往只适用于UNIX、Linux这样的操作系统。


### epoll

[Linux IO模式及 select、poll、epoll详解](https://segmentfault.com/a/1190000003063859)

[IO多路复用之epoll总结](http://www.cnblogs.com/Anker/p/3263780.html)

[epoll精髓](http://www.cnblogs.com/OnlyXP/archive/2007/08/10/851222.html)

[Linux IO模式及select、poll、epoll详解](https://segmentfault.com/a/1190000003063859#articleHeader21) (the best)

[epoll的各个事件触发条件测试](http://www.cppblog.com/yangsf5/archive/2009/03/12/76353.aspx)
>1、listen fd，有新连接请求，触发EPOLLIN。  
>2、对端发送普通数据，触发EPOLLIN。  
>3、带外数据，只触发EPOLLPRI。  
>4、对端正常关闭（程序里close()，shell下kill或ctr+c），触发EPOLLIN和EPOLLRDHUP，但是不触发EPOLLERR和EPOLLHUP。 关于这点，以前一直以为会触发EPOLLERR或者EPOLLHUP。 再man epoll_ctl看下后两个事件的说明，这两个应该是本端（server端）出错才触发的。  
>5、对端异常断开连接（只测了拔网线），没触发任何事件。  


### 协程 gevent

[gevent 廖雪峰的官方网站](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001407503089986d175822da68d4d6685fbe849a0e0ca35000)
