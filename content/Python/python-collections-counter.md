Title: 用Counter计数
Date: 2016-02-11 22:37
Modified: 2016-02-11 22:37
Tags: reading-notes, python, collections, counter
Slug: python-collections-counter
Authors: Henry Chen
Status: published

[TOC]


如果想对一个list中的元素计数怎么办，  
比如: 统计[2332, 1232, 2332, 3321, 9921]中每个元素的个数  
今天不小心看到个不错的东西，记录下: 可以使用collections.Counter

``` python 
from collections import Counter
ss = [2332, 1232, 2332, 3321, 9921]
print Counter(ss)
```
<br/>
结果:
``` text
Counter({2332: 2, 1232: 1, 3321: 1, 9921: 1})
```

- - -

常用的几个方法:

+ Counter(some_data).elements(): 查看key值
+ Counter(some_data).most_common(2): 查看频率最高的2个
+ Counter(some_data).update(some_data2): 就是将some_data和some_data2合并了
+ Counter(some_data).subtract(some_data2): 统计some_data-some_data2的值

- - -

文档也很详细:

``` python
Dict subclass for counting hashable items.  Sometimes called a bag
or multiset.  Elements are stored as dictionary keys and their counts
are stored as dictionary values.

>>> c = Counter('abcdeabcdabcaba')  # count elements from a string

>>> c.most_common(3)                # three most common elements
[('a', 5), ('b', 4), ('c', 3)]
>>> sorted(c)                       # list all unique elements
['a', 'b', 'c', 'd', 'e']
>>> ''.join(sorted(c.elements()))   # list elements with repetitions
'aaaaabbbbcccdde'
>>> sum(c.values())                 # total of all counts
15

>>> c['a']                          # count of letter 'a'
5
>>> for elem in 'shazam':           # update counts from an iterable
...     c[elem] += 1                # by adding 1 to each element's count
>>> c['a']                          # now there are seven 'a'
7
>>> del c['b']                      # remove all 'b'
>>> c['b']                          # now there are zero 'b'
0

>>> d = Counter('simsalabim')       # make another counter
>>> c.update(d)                     # add in the second counter
>>> c['a']                          # now there are nine 'a'
9

>>> c.clear()                       # empty the counter
>>> c
Counter()

Note:  If a count is set to zero or reduced to zero, it will remain
in the counter until the entry is deleted or the counter is cleared:

>>> c = Counter('aaabbc')
>>> c['b'] -= 2                     # reduce the count of 'b' by two
>>> c.most_common()                 # 'b' is still in, but its count is zero
[('a', 3), ('c', 1), ('b', 0)]
Init docstring:
Create a new, empty Counter object.  And if given, count elements
from an input iterable.  Or, initialize the count from another mapping
of elements to their counts.

>>> c = Counter()                           # a new, empty counter
>>> c = Counter('gallahad')                 # a new counter from an iterable
>>> c = Counter({'a': 4, 'b': 2})           # a new counter from a mapping
>>> c = Counter(a=4, b=2)                   # a new counter from keyword args
```
<br/>

感觉标准库应该会用什么高端算法搞定这事,结果很失望  
Counter继承了dict, 下面这段代码是对给定参数的计数,分别对上面
``` python
>>> c = Counter('gallahad')                 # a new counter from an iterable
>>> c = Counter({'a': 4, 'b': 2})           # a new counter from a mapping
>>> c = Counter(a=4, b=2)                   # a new counter from keyword args
```
三种情况作了处理
``` python
if iterable is not None:
    if isinstance(iterable, Mapping):
        if self:
            self_get = self.get
            for elem, count in iterable.iteritems():
                self[elem] = self_get(elem, 0) + count
        else:
            super(Counter, self).update(iterable) # fast path when counter is empty
    else:
        self_get = self.get
        for elem in iterable:
            self[elem] = self_get(elem, 0) + 1
if kwds:
    self.update(kwds)
```
这样的话，简单情况下我完全可以直接用代码中的
``` python
self_get = self.get
for elem in iterable:
    self[elem] = self_get(elem, 0) + 1
```
