Title: 简单聊聊with ... as ...
Date: 2016-02-08 22:58
Modified: 2016-02-08 22:58
Tags: reading-notes, python, with
Slug: python-with-as
Authors: Henry Chen
Status: published

[TOC]

简单聊聊with as都干了些什么.

```
with expr1 as e1, expr2 as e2
```
等价与
```python
with expr1 as e1:
    with expr2 as e2:
```

with语句执行过程:  

1. 执行expr, 返回一个context manager对象  
2. 加载context manager 的__exit__以后备用  
3. 加载context manager 的__enter__方法  
4. 如果设置了目标对象，则将__enter__()的返回值赋给这个对象  
5. 执行with下面的代码块  
6. 如果步骤5代码正常结束,调用__exit__方法,其返回值会被忽略  
7. 如果步骤5代码发生异常,调用context manager 的__exit__方法，并传入异常类型,值和traceback， 如果__exit__()的返回值为false，异常会被重新抛出，如果为true，异常挂起，程序继续执行  


使用with as有三种方式:  

1. 使用类似于open这种会反悔context manager的方法直接获得__enter__和__exit__  
2. 自己写一个class实现__enter__和__exit__  
3. 使用contextlib.contextmanager装饰起装饰一个generator,比较恶心的是这个generator只能yield一个值，不能超过1个，比如很好用的那个用生成器写fibonacci,具体参考文档,再吐槽一次,好恶心  


可以用下面的代码折腾下上面的理论:
```python
import contextlib


class MyContextManger(object):

    def __enter__(self):
        print "entering ..."
        return "Im return from __enter__"
#        return self

    def __exit__(self, exception_type, exception_value, traceback):
#        return False  #  with中的代码块正确时,直接返回False也不会抛错
        print "leaving ..."
        print exception_type, exception_value, traceback
        if exception_type is None:
            print "no exceptions!"
            return False
        elif exception_type is ValueError:
            print "value error !!!"
            return True
        else:
            print "other error"
            return True


@contextlib.contextmanager
def nothing(n):
    print "sth befor yield"
    yield n
    print "sth after yield"


def play_with_mycontextmanager():
    with MyContextManger() as mcm:
        print "mcm: ", mcm
        print "Do sth ..."
        raise ValueError("just for test")


def play_with_open():
    with open("/tmp/tmp.txt", "w") as fp:
        fp.write("nothing to write")
        print "do sth ..."
        pass


def play_with_contextlib():
    with nothing(2) as fl:
        print fl


if __name__ == "__main__":
    print "open file and write"
    play_with_open()
    print

    print "MyContextManger"
    play_with_mycontextmanager()
    print

    print "contexlib.contextmanager"
    play_with_contextlib()
    print
```

结果  
```text
$ python mycontextmanage.py
open file and write
do sth ...

MyContextManger
entering ...
mcm:  Im return from __enter__
Do sth ...
leaving ...
<type 'exceptions.ValueError'> just for test <traceback object at 0x109a16638>
value error !!!

contexlib.contextmanager
sth befor yield
2
sth after yield

```

我这种写法是不是有点懒。  
