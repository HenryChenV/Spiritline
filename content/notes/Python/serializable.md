Title: [笔记] python 序列化
Date: 2016-02-21 16:06
Modified: 2016-02-21 16:06
Tags: python, reading-notes
Slug: serializable
Authors: Henry Chen
Status: draft

[TOC]


### pickle

1. 序列化对象
2. cPickle效率很高


### json

1. 各语言通用
2. 不可序列化对象，除非拓展 JSONEncoder
3. dump中有indent参数，可以在存文件后让值显示得更加漂亮


#### json 自定义encoder
``` python
import json
import datetime


class DateTimeEncoder(json.JSONEncoder):

    def default(self, obj):

        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        return json.JSONEncoder.default(self, obj)


if __name__ == '__main__':

    d = datetime.datetime.now()
    d_dumps = json.dumps(d, cls=DateTimeEncoder)
    print d_dumps
    d2 = datetime.datetime.now().date()
    d2_dumps = json.dumps(d2, cls=DateTimeEncoder)
    print d2_dumps
````
