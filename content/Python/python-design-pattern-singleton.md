Title: 实现 Python 单例模式的几种方式
Date: 2016-03-13 11:40
Modified: 2016-03-13 11:40
Tags: python, design-pattern
Slug: python-design-pattern-singleton
Authors: Henry Chen
Status: published

[TOC]

### 利用模块只会导入一次的特性

在python中，多次导入某个模块，其实只会在第一次产生导入的动作
World.py:  
``` python
# coding=utf-8

"""
利用python模块只会导入一次的特性写单例模式
"""


class World(object):

    def __init__(self):
        self.population = 0

    def run(self):
        print 'the world is running.'


_world = World()
population = _world.population
run = _world.run
```

上面的_world, population, run只会在第一次导入模块的时候导入, 所以是单例


### 利用__metaclass__和__call__

metaclass 是产生类的的类，可以在某个类中设置__metaclass__🔝用哪个类产生这个类,
对于metaclass会先调用__new__产生类，然后调用metaclass的__new__初始化这个类(注意，初始化出来的是类，不是实例),metaclass中定义的方法都试类方法，只能通过类名调用(和用@classmethod生成的类方法不同，无法用实例调用)。
在metaclass中定义__call__方法，这个方法会在ClassName()时被调用，这个方法为类方法，因此可以用这个方法保证单例。

mysingleton.py
``` python
# -*- coding: utf-8 -*-


class SingletonMeta(type):

    def __init__(cls, name, bases, attrs):
        super(SingletonMeta, cls).__init__(name, bases, attrs)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        print cls.instance
        if cls.instance is None:
            print "create new instance."
            cls.instance = super(SingletonMeta, cls).__call__( *args, **kwargs)
        else:
            print "instance was already existed."
        return cls.instance


class MySingleton(object):

    __metaclass__ = SingletonMeta

    def __init__(self):
        """
        __init__ 只会执行一次
        """
        print "init mc"


if __name__ == '__main__':
    print "-------------------------"

    ms1 = MySingleton()
    ms2 = MySingleton()
    print ms1, id(ms1)
    print ms2, id(ms2)
```
结果:
```bash
$ python mysingleton.py 
-------------------------
None
create new instance.
init mc
<__main__.MySingleton object at 0x1052b9490>
instance was already existed.
<__main__.MySingleton object at 0x1052b9490> 4381709456
<__main__.MySingleton object at 0x1052b9490> 4381709456
````


### 利用 __metaclass__ 和 __new__

类似于利用__call__，只是没上面那么繁琐
MySingleton2.py

``` python
# -*- coding: utf-8 -*-


class SingletonMeta(type):

    def __new__(cls, *args, **kwargs):
        print cls, SingletonMeta, "__new__"

        if not hasattr(cls, "_instance"):
            cls._instance = super(SingletonMeta, cls).__new__(cls,
                                                              *args, **kwargs)
        return cls._instance

    def __init__(cls, *args, **kwargs):
        print "init", cls

print "SingletonMeta"


class Test(SingletonMeta):

    __metaclass__ = SingletonMeta

    def __init__(self):
        print "init test"


print "Test"


if __name__ == '__main__':
    print "------------------------------------"
    t1 = Test()
    t2 = Test()
    print t1, id(t1)
    print t2, id(t2)
```

结果:

``` bash
SingletonMeta
<class '__main__.SingletonMeta'> <class '__main__.SingletonMeta'> __new__
init <class '__main__.Test'>
Test
------------------------------------
<class '__main__.Test'> <class '__main__.SingletonMeta'> __new__
<class '__main__.Test'> <class '__main__.SingletonMeta'> __new__
<class '__main__.Test'> 140689093520960
<class '__main__.Test'> 140689093520960
```
