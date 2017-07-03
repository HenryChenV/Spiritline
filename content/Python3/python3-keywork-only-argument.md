Title: Keyword-only argument
Date: 2017-03-12 16:27
Modified: 2017-03-12 16:27
Tags: python, python3
Slug: keywork-only-argument
Authors: Henry Chen
Status: published

[TOC]

### 只允许关键字参数 
#### 简介
Python 3 已经更改了函数参数分配给parameter
slot的方式，可以在传递参数时使用单独的星号(*)，表示在这之后不接受变长度的参数。
kwargs必须在*之后, 具体参考 [PEP 3102 -- Keyword-Only Arguments](https://www.python.org/dev/peps/pep-3102/)

#### Code
**expmple.py**
``` python
# -*- coding=utf-8 -*-


def hello(x, a=1, *, b=2, **kwargs):
    return (x, a, b, kwargs)


print(hello('world'))
```
**run**
``` bash
$ python example.py
('world', 1, 2, {})
```

#### References
[PEP 3102 -- Keyword-Only Arguments](https://www.python.org/dev/peps/pep-3102/)
