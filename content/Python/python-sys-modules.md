Title: 有趣的 sys.modules
Date: 2016-02-06 02:24
Modified: 2016-02-06 02:24
Tags: python, fun
Slug: python-sys-modules
Authors: Henry Chen
Status: published

[TOC]

在某本给了91条python建议的树上看到了一段奇怪的代码，愿意是希望将常亮防到一个文件中，
看到这代码，大概意思也能猜到，怎么用也能猜到，但其中对于sys.modules的用法让人觉得很有意思。

常量文件constant.py 代码:  
```python
#-*- coding=utf-8 -*-

print 'import constant'

class _const:
    class ConstError(TypeError): pass
    class ConstCaseError(ConstError): pass

    def __init__(self):
        print 'new _const'

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "Can't change const. %s" % name
        if not name.isupper():
            raise self.ConstCaseError, \
                    'const name "%s" is not all uppercase' % name
        self.__dict__[name] = value

import sys
sys.modules[__name__] = _const()

import constant
constant.MY_FIRST_CONSTANT = 1
constant.MY_SECOND_CONSTANT = 2
constant.MY_THIRD_CONSTANT = 'a'
constant.MY_FORTH_CONSTANT = 'b'
```
             
测试代码 test.py:  
```python
#-*- coding=utf-8 -*-

import constant

import ipdb; ipdb.set_trace() ### XXX BREAKPOINT
print constant.MY_SECOND_CONSTANT
print constant.MY_THIRD_CONSTANT * 2
print constant.MY_FORTH_CONSTANT + '5'
```

test1.py中可以顺利调用constant.py中的常量，如果在test1.py中想修改常亮也会报错，
为什么会有这种效果。

文章肯定在constant.py的:  
```python
import sys
sys.modules[__name__] = _const()

import constant
```  

原因在于, __name__表示的是这个module的名称，可能是__main__或者文件名去掉后缀(这点不展开), sys.modules是一个已知模块的模块名称到模块的映射，如果要找的模块的名称在sys.modules中，那么回按照sys.modules去找，否则sys.path中找，在constant.py中用sys.modules[module_name] = module 的方式改变了constant.py这个模块的指向，在constant.py中再次import constant时，因为constant这个名称在sys.modules中已有，所以会按照sys.modules的映射找出这个模块，而在import 前已经将指向改成了_const()，所以再次import 后，constant就等同于_const()了。

个人觉得这个用法笔记有趣，特此记录，无他意。
