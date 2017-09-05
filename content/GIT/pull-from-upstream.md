Title: 从upstream拉代码
Date: 2016-06-11 22:59
Modified: 2016-06-11 22:59
Tags: git
Slug: pull-from-upstrea
Authors: Henry Chen
Status: published

[TOC]


从自定义的远程分支拉代码

```
git remote -v
git remote add upstream https://github.com/otheruser/repo.git
git fetch upstream
git checkout master
git merge upstream/master
```
