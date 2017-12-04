Title: 记一次OOM问题排查
Date: 2017-12-04 21:04
Modified: 2017-12-04 21:04
Tags: system, OOM
Slug: oom-problem-diagnosis
Authors: Henry Chen
Status: published

在一个项目中使用了consumer接收消息, 若干个handler注册在了一个consumer中. 
启动时, 由一个主进程fork出8个子进程同时接收消息, 没有做子进程死往后自动重启的逻辑. 
刚上线时, 查看进程, 总共由9个(1个主进程+8个子进程), 
一个周末过后, 再次查看进程, 发现只有6个(1个主进程+5个子进程)了.


[TOC]


## 问题排查

### 缩小范围
因为是若干个handler注册到了一个consumer中, 所以不知道是哪个handler的锅.
第一次追踪这个问题时, 甚至在我眼前就消失了一个进程. 当时在运行的只有handler1,
怀疑是命中了使用的框架的OOM策略, 我做了两件事:

1. 询问框架的同学OOM策略是什么, 被告知框架本身的OOM策略并没有在consumer上应用,
   并建议我看下是否是系统的OOM所为;
2. 将若干的handler按业务拆分到多个consumer中去, 一来,
   减小handler自爆造成的影响, 二来缩小范围, 方便定位到是哪个handler

### 确定是OOM
拆分成多个consumer只后, 子进程自杀事件依然在继续. 先确定自杀的进程的PID是多少,
因为8个子进程生成时间很接近, 因此PID也是接近的, 这个case中甚至是连续的,
所以根据存活的进程的PID是可以推算出自杀的进程的PID的, 总共3个. 
然后用dmesg命令查看内核环形缓冲区信息(或者可以直接`grep PID /var/log/message`,
只是需要sudo权限, 所以选择了不用sudo权限的dmesg)

```
$ dmesg -T -d | grep 21797
...
[Mon Dec  4 15:13:47 2017 <    0.000002>] Out of memory: Kill process 21797 (/path/to/command) score 394 or sacrifice child
...
```

然后观察监控曲线, 在这个时间点附近确实有内存骤增的情况.
那这就可以确定为OOM所为了.

### 诊断原因
然后看了下这个PID在log中最后的记录, 和被kill的时间相差9个小时, 3个进程都是这样.
于是追踪这个handler的代码, 发现这个handler在处理前后分别由`start xxx`和`end
xxx`的日志, 而日志文件中只有`start xxx`的日志, 没有`end xxx`的日志.
于是可以断定这个handler没有跑完就被kill了.   
然后看下处理过程中有没有内存占用比较高的操作, 发现在处理后期有一个写文件的操作,
因为数据量比较大, 造成内存骤增, 从而OOM.


## 参考
1. [linux如何查看进程OOM killer](http://blog.csdn.net/daiyudong2020/article/details/51543664)
2. [Linux系统中‘dmesg’命令处理故障和收集系统信息的7种用法](https://linux.cn/article-3587-1.html)
