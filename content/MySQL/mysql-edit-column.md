Title: MySQL修改字段
Date: 2016-04-14 11:20
Modified: 2016-04-14 11:20
Tags: mysql
Slug: mysql-edit-column
Authors: Henry Chen
Status: published

[TOC]

mysql 修改字段三种方式:   
又忘记了，简单记录下

``` sql
alter table tablename 
1. alter alter column 字段名 drop default or alter column 字段名 set default 默认值;
2. modify column 字段名 类型 NOT NULL DEFAULT xx COMMENT 'xxxx'
3. change column 老字段名 新字段名 类型 NOT NULL DEFAULT xx COMMENT 'xxxx'
```

1. alter 只能修改默认值
2. modify 不能修改字段名称，只能改字段类型
3. change 字段名称和类型都能改
