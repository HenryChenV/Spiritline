Title: python中的字符串连接效率
Date: 2016-05-08 20:44
Modified: 2016-05-08 20:44
Tags: python, string, concat
Slug: python-string-concat
Authors: Henry Chen
Status: published

[TOC]

之前有人跟我说，python中不要用+连接字符串，效率很低，但问到原因，没解释清楚，表示不服，于是自己亲测了下

``` python
# -*- coding=utf-8 -*-

"""
字符串性能测试
"""

from time import time


times = 10000000
s_list = ["Henry", "Chen"]
s1 = "Henry"
s2 = "Chen"
s3 = "Python"
s4 = "Linux"
s5 = "CentOS"
s6 = "ubuntu"
s7 = "virtualreality"
s8 = "tryagain"
s9 = "中文"
s10 = "中文2"
s11 = "呵呵了"
s12 = "我哭了"


t = time()
for i in xrange(times):
    new_s1 = ""
    new_s1 = "".join((s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12))
print "join", new_s1, time() - t


#format_str = "".join(["%s" for i in xrange(len(s_list))])
t = time()
for i in xrange(times):
    new_s2 = ""
    new_s2 = "%s%s%s%s%s%s%s%s%s%s%s%s" % (
        s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12
    )
print "%", new_s2, time() - t


t = time()
for i in xrange(times):
    new_s3 = ""
    new_s3 = reduce(lambda x, y: x + y,
                    (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12)
                    )
print "reduce", new_s3, time() - t


t = time()
for i in xrange(times):
    new_s4 = ""
#    for s in s_list:
#        new_s4 += s
#    new_s4 = s_list[0] + s_list[1]
    new_s4 = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10 + s11 + s12
print "+", new_s4, time() - t


#format_str = "".join(["{}" for i in xrange(len(s_list))])
t = time()
for i in xrange(times):
    new_s5 = ""
    new_s5 = "{}{}{}{}{}{}{}{}{}".format(
        s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12
    )
print "format", new_s5, time() - t


t = time()
for i in xrange(times):
    new_s5 = ""
    new_s5 = "{s1}{s2}{s3}{s4}{s5}{s6}{s7}{s8}{s9}{s10}{s11}{s12}".format(
        s1=s1,
        s2=s2,
        s3=s3,
        s4=s4,
        s5=s5,
        s6=s6,
        s7=s7,
        s8=s8,
        s9=s9,
        s10=s10,
        s11=s11,
        s12=s12,
    )
print "format", new_s5, time() - t
```
百度的观点基本是推荐用join，不要用+，但我用上吗的代码测试的时候，当连接的字符串数量到12个时，join在时间上才成功逆袭+，这是12个字符串连接的结果:
``` text
HenryMBP:optimization henry$ python test_str2.py 
join HenryChenPythonLinuxCentOSubuntuvirtualrealitytryagain中文中文2呵呵了我哭了 4.91322088242
% HenryChenPythonLinuxCentOSubuntuvirtualrealitytryagain中文中文2呵呵了我哭了 % 6.49611997604
reduce HenryChenPythonLinuxCentOSubuntuvirtualrealitytryagain中文中文2呵呵了我哭了 19.1923899651
+ HenryChenPythonLinuxCentOSubuntuvirtualrealitytryagain中文中文2呵呵了我哭了 5.50836706161
format HenryChenPythonLinuxCentOSubuntuvirtualrealitytryagain中文 10.0058710575
format HenryChenPythonLinuxCentOSubuntuvirtualrealitytryagain中文中文2呵呵了我哭了 22.9674911499
```
为什么要用逆袭这么尴尬的词呢，因为这是2个字符串连接时的结果:
``` test
join HenryChen 2.3251760006
% HenryChen 2.47228384018
reduce HenryChen 5.0010330677
+ HenryChen 1.3511390686
format HenryChen 3.7649769783
format HenryChen 6.41278791428
```
这么看来，随着数量的增加，join应该会迎头赶上，反倒是被认为最pythonic的format，时间一直垫底  
那么，对于join跟+比，优势在哪呢，
源码中+方式的处理函数如下:
``` c
static PyObject *
string_concat(register PyStringObject *a, register PyObject *bb)
{
    register Py_ssize_t size;
    register PyStringObject *op;
    if (!PyString_Check(bb)) {
#ifdef Py_USING_UNICODE
        if (PyUnicode_Check(bb))
            return PyUnicode_Concat((PyObject *)a, bb);
#endif
        if (PyByteArray_Check(bb))
            return PyByteArray_Concat((PyObject *)a, bb);
        PyErr_Format(PyExc_TypeError,
                     "cannot concatenate 'str' and '%.200s' objects",
                     Py_TYPE(bb)->tp_name);
        return NULL;
    }
#define b ((PyStringObject *)bb)
    /* Optimize cases with empty left or right operand */
    if ((Py_SIZE(a) == 0 || Py_SIZE(b) == 0) &&
        PyString_CheckExact(a) && PyString_CheckExact(b)) {
        if (Py_SIZE(a) == 0) {
            Py_INCREF(bb);
            return bb;
        }
        Py_INCREF(a);
        return (PyObject *)a;
    }
    size = Py_SIZE(a) + Py_SIZE(b);
    /* Check that string sizes are not negative, to prevent an
       overflow in cases where we are passed incorrectly-created
       strings with negative lengths (due to a bug in other code).
    */
    if (Py_SIZE(a) < 0 || Py_SIZE(b) < 0 ||
        Py_SIZE(a) > PY_SSIZE_T_MAX - Py_SIZE(b)) {
        PyErr_SetString(PyExc_OverflowError,
                        "strings are too large to concat");
        return NULL;
    }

    /* Inline PyObject_NewVar */
    if (size > PY_SSIZE_T_MAX - PyStringObject_SIZE) {
        PyErr_SetString(PyExc_OverflowError,
                        "strings are too large to concat");
        return NULL;
    }
    op = (PyStringObject *)PyObject_MALLOC(PyStringObject_SIZE + size);
    if (op == NULL)
        return PyErr_NoMemory();
    PyObject_INIT_VAR(op, &PyString_Type, size);
    op->ob_shash = -1;
    op->ob_sstate = SSTATE_NOT_INTERNED;
    Py_MEMCPY(op->ob_sval, a->ob_sval, Py_SIZE(a));
    Py_MEMCPY(op->ob_sval + Py_SIZE(a), b->ob_sval, Py_SIZE(b));
    op->ob_sval[size] = '\0';
    return (PyObject *) op;
#undef b
}
```
略去操作前的各种检查，主要逻辑只能处理2个字符串的拼接，多个字符串拼接需要多次调用此方法，每次拼接时，都是先分配一块2个字符串大小总和的区域，然后将两个字符串挨个拷贝进这块区域。   
再看下join的源码
```c
static PyObject *
string_join(PyStringObject *self, PyObject *orig)
{
    char *sep = PyString_AS_STRING(self);
    const Py_ssize_t seplen = PyString_GET_SIZE(self);
    PyObject *res = NULL;
    char *p;
    Py_ssize_t seqlen = 0;
    size_t sz = 0;
    Py_ssize_t i;
    PyObject *seq, *item;

    seq = PySequence_Fast(orig, "can only join an iterable");
    if (seq == NULL) {
        return NULL;
    }

    seqlen = PySequence_Size(seq);
    if (seqlen == 0) {
        Py_DECREF(seq);
        return PyString_FromString("");
    }
    if (seqlen == 1) {
        item = PySequence_Fast_GET_ITEM(seq, 0);
        if (PyString_CheckExact(item) || PyUnicode_CheckExact(item)) {
            Py_INCREF(item);
            Py_DECREF(seq);
            return item;
        }
    }

    /* There are at least two things to join, or else we have a subclass
     * of the builtin types in the sequence.
     * Do a pre-pass to figure out the total amount of space we'll
     * need (sz), see whether any argument is absurd, and defer to
     * the Unicode join if appropriate.
     */
    for (i = 0; i < seqlen; i++) {
        const size_t old_sz = sz;
        item = PySequence_Fast_GET_ITEM(seq, i);
        if (!PyString_Check(item)){
#ifdef Py_USING_UNICODE
            if (PyUnicode_Check(item)) {
                /* Defer to Unicode join.
                 * CAUTION:  There's no gurantee that the
                 * original sequence can be iterated over
                 * again, so we must pass seq here.
                 */
                PyObject *result;
                result = PyUnicode_Join((PyObject *)self, seq);
                Py_DECREF(seq);
                return result;
            }
#endif
            PyErr_Format(PyExc_TypeError,
                         "sequence item %zd: expected string,"
                         " %.80s found",
                         i, Py_TYPE(item)->tp_name);
            Py_DECREF(seq);
            return NULL;
        }
        sz += PyString_GET_SIZE(item);
        if (i != 0)
            sz += seplen;
        if (sz < old_sz || sz > PY_SSIZE_T_MAX) {
            PyErr_SetString(PyExc_OverflowError,
                "join() result is too long for a Python string");
            Py_DECREF(seq);
            return NULL;
        }
    }

    /* Allocate result space. */
    res = PyString_FromStringAndSize((char*)NULL, sz);
    if (res == NULL) {
        Py_DECREF(seq);
        return NULL;
    }

    /* Catenate everything. */
    p = PyString_AS_STRING(res);
    for (i = 0; i < seqlen; ++i) {
        size_t n;
        item = PySequence_Fast_GET_ITEM(seq, i);
        n = PyString_GET_SIZE(item);
        Py_MEMCPY(p, PyString_AS_STRING(item), n);
        p += n;
        if (i < seqlen - 1) {
            Py_MEMCPY(p, sep, seplen);
            p += seplen;
        }
    }

    Py_DECREF(seq);
    return res;
}
```
略去检查部分，主要逻辑中，可以处理多个字符串拼接，先计算出多个字符串拼接成的新字符串所需内存大小，然后挨个拷贝进去。  
在多个字符串拼接时，+无疑会耗费更多的内存。
*****
总结:  

1. 如果拼接字符串较少，可以用+，如果拼接字符串较多，无论从时间还是空间角度看，都得用join
2. 说join的效率高于+，其实说的是从内存角度说的，随着拼接字符串数量的上升，+会耗费更多的内存
