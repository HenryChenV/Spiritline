Title: 你的分布式锁靠谱吗
Date: 2020-02-16 22:51
Modified: 2020-02-16 22:51
Tags: 分布式, 架构
Slug: distrivuted-lock
Authors: Henry Chen
Summary:
Status: draft

[TOC]


分布式锁对大家来说并不陌生，可你在用的分布式锁真的靠谱吗？


## 你真的需要分布式锁吗?
分布式锁的目的


## 一个简单的分布式锁实现
### 怎么实现的
本文的重点不在说明分布式锁怎么实现,是基于已有的被广泛认可的实现捣乱的.
所以直接show code, 以下是很常见的基于Redis实现的分布式锁

**加锁**
``` java
public static boolean tryLock(String key, String uniqueId, int seconds) {
    return "OK".equals(jedis.set(key, uniqueId, "NX", "EX", seconds));
}
```

**解锁**
``` java
public static boolean releaseLock(String key, String uniqueId) {
    String luaScript = "if redis.call('get', KEYS[1]) == ARGV[1] then " +
            "return redis.call('del', KEYS[1]) else return 0 end";
    return jedis.eval(
        luaScript, 
        Collections.singletonList(key), 
        Collections.singletonList(uniqueId)
    ).equals(1L);
}
```


基于Redis的简单实现，当然Mysql也一样，这里主要讲思想
讲下需要注意的几个点
1. 加锁和解锁操作必须是针对同一个锁的.
2. 如果持有锁的节点挂了，不能让锁无法释放.

## 靠谱吗?
1. 单点问题
2. 续租问题


## Redlock算法
### 算法细节
翻译下https://redis.io/topics/distlock
### 靠谱吗?
两位大佬的博客整理下


## 其他实现
### Redisson
### Zookeeper


## 参考
