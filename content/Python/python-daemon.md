Title: 后台程序管理
Date: 2017-03-27 10:55
Modified: 2017-03-27 10:55
Tags: daemon, python, signal
Slug: 
Authors: Henry Chen
Status: draft


[TOC]

## 概述
因为脑子几根筋不对，想在项目中用多进程。  
那么问题来了，如果不加处理的话，各个进程谁都不管谁，父进程挂了子进程跑得依然很欢，子进程挂了父进程也不知道。  
所以嘛，需要个东东管理下这堆不懂事的玩意儿，做到子进程挂了能重启，父进程挂了，儿子们处理下后事然后自杀。

## 依赖知识

### 信号

#### SIGCHLD
在一个进程终止或停止时，SIGCHLD信号被送给其父进程，按系统默认，将忽略次信号。  
如果父进程希望被告知其子进程的这种状态改变，则应捕捉此信号。  
信号捕捉函数中通常要调用一种wait函数以获得子进程ID和其终止状态。  

#### SIGTERM
这是由kill(1)命令发送的系统默认终止信号。由于该信号是由程序捕获的，  
使用SIGTERM可以让程序有机会在退出之前做好清理工作，从而优雅的终止(相对于SIGKILL而言，SIGKILL不能被捕捉或者忽略)

#### SIGKILL
这事两个不能被捕捉或忽略的信号中的一个(另一个是SIGSTOP)。它向系统挂你也提供了一种可以杀死任一进程的可靠方法。

#### WNOHANG
#### waitpid

### 进程

## 参考