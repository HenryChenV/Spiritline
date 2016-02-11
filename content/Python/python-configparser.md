Title: 用ConfigParser解析参数
Date: 2016-02-11 23:51
Modified: 2016-02-11 23:51
Tags: python, configparser
Slug: python-configparser
Authors: Henry Chen
Status: published


python提供了现成的配置文件解析标准库ConfigParser,  
使用方法不做详细介绍,只是记录下他的配置项查找规则,避免踩坑。

[TOC]

### 查找顺序
使用时得注意点他的参数查找顺序,特别提防构造函数中的defaults和get方法中的vars参数，  
配置项查找规则如下:

1. 找不到section，raise ConfigParser.NoSectionError
2. vars
3. 配置文件的对应section下
4. 配置文件[DEFAULT]下
5. 构造函数的defaults
6. raise ConfigParser.NoOptionError


### 测试代码
值得一提的事，配置项支持占位符的方式  
配置文件format.conf:  
``` text
[DEFAULT]
conn_str = %(dbn)s://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s
dbn = mysql
user = root
host = localhost
port = 3306

[db1]
user = aaa
pw = ppp
db = example

[db2]
host = 192.168.7.110
pw = www
db = example
```
<br/>

测试代码:

``` python
# coding=utf-8

import ConfigParser


def read_conf():
    defaults = {
        'dbn': 'test',
        'user': 'admin',
        'host': '127.0.0.1',
        'port': 3306,
    }

    vars = {
        'dbn': 'test_vars',
        'user': 'admin_vars',
        'host': '127.0.1.1',
        'port': 3306,
    }

    conf = ConfigParser.ConfigParser(defaults=defaults)
    conf.read('format.conf')
    print conf.get('db1', 'conn_str', vars=vars)
    print conf.get('db2', 'conn_str', vars=vars)


if __name__ == '__main__':
    read_conf()
```
