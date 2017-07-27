Title: Celery 源码笔记
Date: 2017-07-03 10:53
Modified: 2017-07-03 10:53
Tags: python, celery
Slug: python-celery-worker
Authors: Henry Chen
Status: draft

[TOC]

## 执行流程

### 启动顺序

#### Worker

```
Timer, Hub, Queues (intra), Pool, Autoreloader, Autoscaler, Beat, StateDB, Consumer

```

#### Consumer

```
onnection, Events, Mingle, Gossip, Tasks, Control, Heart, Agent, event loop
```


## 模块

### loader

### trace

### worker

#### timer


## Tips

#### 指定执行的worker
[CELERY_WORKER_DIRECT](http://docs.celeryproject.org/en/3.1/configuration.html#celery-worker-direct)


## Questions
1. Celery 中的loader是什么, 干了什么事
2. trace 模块在干什么事


## 还需继续研究

1. billiard: 封装了multiprocess
2. inspect: 获取python对象的信息, 比如func的参数等等
