Title: MySQL的TPS, QPS计算
Date: 2018-01-30 15:39
Modified: 2018-01-30 15:39
Tags: mysql, tps, qps
Slug: mysql-tps-qps
Authors: Henry Chen
Status: draft
Summary: MySQL中对于TPS和QPS的定义及计算方式

[TOC]

## 定义

MySQL的吞吐量一般用TPS和QPS表示:  

*  *QPS(Query Per Second):* 每秒查询量
*  *TPS(Transaction Per Second):* 每秒事务量  


## 计算

MySQL会对各种命令进行统计, 放在status中, 用com_xxx的格式表示, 查看方式如下所示:
``` sql
mysql> show global status like "com_up%" ;
+------------------+----------+
| Variable_name    | Value    |
|------------------+----------|
| Com_update       | 54708386 |
| Com_update_multi | 43       |
+------------------+----------+
2 rows in set
Time: 0.021s
```

不加global默认是当前session的.

可以取这些指标的增量除以统计时间, 或者直接除以uptime.  下面说下怎么QPS和TPS分别取哪些指标.

### QPS
QPS涉及到2个指标: Queries, Questions, com_select
#### [com_select](https://dev.mysql.com/doc/refman/5.6/en/server-status-variables.html#statvar_Com_xxx)
查询次数
``` sql
mysql> show global status like "com_select" ;
+-----------------+-------------+
| Variable_name   | Value       |
|-----------------+-------------|
| Com_select      | 10847054449 |
+-----------------+-------------+
1 row in set
Time: 0.021s
```

####  [Queries](https://dev.mysql.com/doc/refman/5.6/en/server-status-variables.html#statvar_Queries) 
统计语句的执行次数, session和global的查询结果一致, 统计不包含 `COM_PING`, `COM_STATISTICS`, `COM_STMT_PREPARE`, `COM_STMT_CLOSE`, `COM_STMT_RESET`;
``` sql
mysql> show status like "queries" ;
+-----------------+-------------+
| Variable_name   | Value       |
|-----------------+-------------|
| Queries         | 19514571669 |
+-----------------+-------------+
1 row in set
Time: 0.019s
mysql> show global status like "queries" ;
+-----------------+-------------+
| Variable_name   | Value       |
|-----------------+-------------|
| Queries         | 19514590104 |
+-----------------+-------------+
1 row in set
Time: 0.022s
```

####[ Questions](https://dev.mysql.com/doc/refman/5.6/en/server-status-variables.html#statvar_Queries) 
和Queries类似, 不过session中查和global查不一样, 默认(不加global)情况下查的是session内的统计, 统计不包含 `COM_PING`, `COM_STATISTICS`, `COM_STMT_PREPARE`, `COM_STMT_CLOSE`, `COM_STMT_RESET`.
``` sql
mysql> show status like "questions" ;
+-----------------+---------+
| Variable_name   | Value   |
|-----------------+---------|
| Questions       | 24      |
+-----------------+---------+
1 row in set
Time: 0.015s
mysql> show global status like "questions" ;
+-----------------+-------------+
| Variable_name   | Value       |
|-----------------+-------------|
| Questions       | 19497681640 |
+-----------------+-------------+
1 row in set
Time: 0.019s
```

一般选择`com_select`.

### TPS
为了和QPS有区分, 一般取`Com_insert` + `Com_update` + `Com_delete` 三个统计项的和


## 参考
1. [MySQL 5.6 Reference Manual-com_xxx](https://dev.mysql.com/doc/refman/5.6/en/server-status-variables.html#statvar_Com_xxx)
2. [MySQL 5.6 Reference Manual-Queries](https://dev.mysql.com/doc/refman/5.6/en/server-status-variables.html#statvar_Queries)
3. [MySQL 5.6 Reference Manual-Questions](https://dev.mysql.com/doc/refman/5.6/en/server-status-variables.html#statvar_Queries)
4. [MySQL 监控指标](https://jin-yang.github.io/post/mysql-monitor.html)
5. [How MySQL ‘queries’ and ‘questions’ are measured](https://www.percona.com/blog/2014/05/29/how-mysql-queries-and-questions-are-measured/)
