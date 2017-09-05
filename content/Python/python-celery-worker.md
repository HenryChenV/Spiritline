Title: Celery 源码笔记
Date: 2017-07-03 10:53
Modified: 2017-07-03 10:53
Tags: celery, python
Slug: python-celery-worker
Summary: celery源码阅读笔记
Authors: Henry Chen
Status: draft


[TOC]

# 模块

## Worker

启动顺序:
```
Timer, Hub, Queues (intra), Pool, Autoreloader, Autoscaler, Beat, StateDB, Consumer

```

在Blueprint.apply中会先实例化这些类, 然后调用每个的include方法初始化到parent(此处为worker)上

### Timer
Step  
初始化worker.timer, gevent环境下使用`celery.concurrency.gevent.Timer`

### Hub
StartStopStep  
event loop object, gevent环境下不会初始化这个对象, 目测是用了gevent的hub  
看看gevent的hub什么鬼  
event loop 是什么意思, 跟task有关的吗  

### Queues
Step  
根据是否使用信号量确定worker.process_task用worker._process_task
还是worker._process_task_sem,
其实_process_task_sem也就是在_process_task外面包了层acquire  

### Pool
StartStopStep  
实例化worker.pool_cls(gevent环境下是`celery.concurrency.gevent.TaskPool`,
其实用的是`gevent.pool.Pool`,
只是把`gevent.pool.Pool`的接口换了个名字在`TaskPool`里面用而已)  
有个task_join_will_block参数不知道是干嘛的  

### Autoreloader
追踪变化, 然后reaload, 字面意思, 默认不reload, 先不管  

### Autoscaler
自动增加减少process, 好厉害的功能  
有空打开下玩玩, `--autoscale`  

### Beat
这个可以写个专题了, 跳过  

### StateDB
存储worker的task状态的, 算本地缓存, flower里面看有用过, 当时写文件的   

### Consumer
有自己的blueprint  
初始化worker.consumer  
其实是`celery.worker.consumer:Consumer`  

启动顺序
```
connection, Events, Mingle, Gossip, Tasks, Control, Heart, Agent, event loop

```

include到steps中的StartStopStep(也就是需要看下start时候做了什么):
```
[<step: Connection>, <step: Events>, <step: Tasks>, <step: Control>, <step: Heart>, <step: event loop>]
```

#### Connection
在start的时候会初始化consumer.connection(实际上使用的是`kombu.connection:Connection`)  
用于连接broker  

#### Events
在start中会初始化consumer.event_dispatcher(from `celery.events:EventDispatcher`)  
每次初始化都会先close掉之前的dispatch和dispatch.connection  
用于dispatch event messages, 注释中特别注明这个是需要close的  

#### Mingle
暂未用到, 看了下, 没看懂具体干的什么事, 猜测多个节点的配合有关  
查了下文档中的`--witout-mingle`选项: Do not synchronize with other workers at startup.  
参考: [--without-mingle](http://docs.celeryproject.org/en/3.1/reference/celery.bin.worker.html?highlight=without_minglecmdoption-celery-worker-without-mingle)

#### Gossip
暂时未用, 跳过  
回头得看看, 竟然还有election  
参考: [gossip protocol](  https://en.wikipedia.org/wiki/Gossip_protocol)  

#### Tasks
初始化consumer.task_consumer(`:class:celery.app.amqp.AMQP.consumer_cls`,   
默认是 `:class:celery.app.amqp.TaskConsumer`)和consumer.qos(`kombu.common.QoS`)  
在此之前还做了点跟strategy相关的事情, self.strategies是个dict,  
存储本地的task_name到task_message_handler(`:meth:celery.worker.strategy.default`)的映射  

##### TODO
1. handler的执行过程  
2. Request干了什么  
3. consumer.task_consumer干了什么  
4. consumer.qos干了什么  

#### Control

#### Heart

#### Agent

#### Events

#### loop


### Consumer

```
connection, Events, Mingle, Gossip, Tasks, Control, Heart, Agent, event loop

```



# 模块

## loader


## trace


## worker


## Timer

没找到在哪里start的


## Hub



# Tips

### 指定执行的worker
[CELERY_WORKER_DIREC](http://docs.celeryproject.org/en/3.1/configuration.htmlcelery-worker-direct)



# Questions
1. Celery 中的loader是什么, 干了什么事
2. trace 模块在干什么事



# 还需继续研究

1. billiard: 封装了multiprocess
2. inspect: 获取python对象的信息, 比如func的参数等等



# 宝藏

## warnings模块
用于打印需要警告用户, 但不足以抛异常的情况, 竟然还能这样  
具体参考[warnings模块](https://docs.python.org/2/library/warnings.html)



# 参考
1. [BROKER_HEARTBEAT](http://docs.celeryproject.org/en/3.1/configuration.html?highlight=rate_limitbroker-heartbeat)

# 附录

## 名词解释

### ETA
Estimated time of arrival 估计到达时间
