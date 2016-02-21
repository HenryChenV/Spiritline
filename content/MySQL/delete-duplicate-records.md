Title: 删除重复数据
Date: 2016-02-18 11:54
Modified: 2016-02-18 11:54
Tags: mysql, work
Slug: delete-duplicate-records
Authors: Henry Chen
Status: published

[TOC]

删除重复数据  
image_info表中每个ImgUrl应该只对应一条记录,删除多余记录

``` sql
delete from image_info 
where Type=3010 
and id not in (
        select id from (
            select a.id from image_info a group by a.ImgUrl
            ) as a
        );
```
