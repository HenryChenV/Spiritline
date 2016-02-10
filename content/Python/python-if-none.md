Title: python中判断一个实例是否为空
Date: 2016-02-10 19:43
Modified: 2016-02-10 19:43
Tags: python, build-in-function
Slug: python-if-none
Authors: Henry Chen
Status: published

[TOC]

在python中，通过如下代码判断一个对象是否为空时

``` python
a = A()
if a:
    print "not empty"
else:
    print "empty"
```
- - - 

如果A实现了__nonzero__会调用__nonzero__方法,

``` python
class A(object):

    def __nonzero__(self):
        print "testing nonzero"
        return True

    def __len__(self):
        print "testing len"
        return False


if __name__ == "__main__":

    a = A()
    if a:
        print "not empty"
    else:
        print "empty"
```

<br/>
结果:

``` bash
$ python main.py 
testing nonzero
not empty
```

- - - 
否则调用__len__(),

``` python
class A(object):

    def __len__(self):
        print "testing len"
        return False


if __name__ == "__main__":

    a = A()
    if a:
        print "not empty"
    else:
        print "empty"
```
<br/>
结果:

``` bash
$ python main.py 
testing nonzero
empty
```

- - - 
否则，直接返回True

``` python
class A(object):
    pass


if __name__ == "__main__":

    a = A()
    if a:
        print "not empty"
    else:
        print "empty"
```

<br/>
结果:

``` bash
$ python main.py 
testing nonzero
not empty
```
