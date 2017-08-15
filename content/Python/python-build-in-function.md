Title: Python中的build-in function
Date: 2016-02-11 16:17
Modified: 2016-02-11 16:17
Tags: python, build-in-function
Slug: python-build-in-function
Authors: Henry Chen
Status: published 


python中build-in function的笔记，持续更新

[TOC]


## sorted

sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list  
cmp: 自定义比较函数,返回-1,0,1代表>=<,  
key: 自定义函数,用于取出iterable每个元素中用于比较的项  
reverse: 是否反序  

### 普通玩法

推荐用key，因为cmp每次都会调用一次，效率低

``` python
In [162]: persons
Out[162]: 
[{u'age': 18, u'name': u'conke'},
 {u'age': 20, u'name': u'henry'},
 {u'age': 24, u'name': u'henry'},
 {u'age': 33, u'name': u'sandy'},
 {u'age': 7, u'name': u'alex'}]

In [163]: sorted(persons, cmp=lambda x, y: cmp(x['name'], y['name']))
Out[163]: 
[{u'age': 7, u'name': u'alex'},
 {u'age': 18, u'name': u'conke'},
 {u'age': 20, u'name': u'henry'},
 {u'age': 24, u'name': u'henry'},
 {u'age': 33, u'name': u'sandy'}]

In [164]: sorted(persons, key=lambda x: (x['name'], -x['age']))
Out[164]: 
[{u'age': 7, u'name': u'alex'},
 {u'age': 18, u'name': u'conke'},
 {u'age': 24, u'name': u'henry'},
 {u'age': 20, u'name': u'henry'},
 {u'age': 33, u'name': u'sandy'}]
```

### 多维list
可以用operator.itemgetter指定列的先后
``` python
In [186]: gameresults
Out[186]: 
[[u'Bob', 95.0, u'A'],
 [u'Alan', 86.0, u'C'],
 [u'Mandy', 82.5, u'A'],
 [u'Mandy', 86, u'E']]

In [187]: from operator import itemgetter

In [188]: sorted(gameresults, key=itemgetter(2, 1))
Out[188]: 
[[u'Mandy', 82.5, u'A'],
 [u'Bob', 95.0, u'A'],
 [u'Alan', 86.0, u'C'],
 [u'Mandy', 86, u'E']]
```

### 字典中的list

``` python
In [199]: mydict
Out[199]: 
{u'Du': [u'C', 2],
 u'Li': [u'M', 7],
 u'Ma': [u'C', 9],
 u'Wang': [u'P', 3],
 u'Zhang': [u'E', 2],
 u'Zhe': [u'H', 7]}

In [200]: sorted(mydict.iteritems(), key=lambda (k,v): itemgetter(1)(v))
Out[200]: 
[(u'Zhang', [u'E', 2]),
 (u'Du', [u'C', 2]),
 (u'Wang', [u'P', 3]),
 (u'Li', [u'M', 7]),
 (u'Zhe', [u'H', 7]),
 (u'Ma', [u'C', 9])]

```

### List中的字典

``` python
In [213]: gameresults
Out[213]: 
[{u'losses': 3, u'name': u'Bob', u'rating': 75, u'wins': 10},
 {u'losses': 5, u'name': u'David', u'rating': 57, u'wins': 3},
 {u'losses': 5, u'name': u'Carol', u'rating': 57, u'wins': 4},
 {u'losses': 3, u'name': u'Patty', u'rating': 71.48, u'wins': 9}]

In [214]: sorted(gameresults, key=lambda x: itemgetter('rating', 'name'))
Out[214]: 
[{u'losses': 3, u'name': u'Bob', u'rating': 75, u'wins': 10},
 {u'losses': 5, u'name': u'David', u'rating': 57, u'wins': 3},
 {u'losses': 3, u'name': u'Patty', u'rating': 71.48, u'wins': 9},
 {u'losses': 5, u'name': u'Carol', u'rating': 57, u'wins': 4}]

```
- - -

## map
TO DO
- - -

## zip
TO DO
- - -

