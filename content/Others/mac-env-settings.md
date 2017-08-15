Title: Mac OS 环境配置
Date: 2016-05-14 21:23
Modified: 2016-05-14 21:23
Tags: mac, env
Slug: mac-env-settings
Authors: Henry Chen
Status: published

[TOC]

新入职，公司发了新mac, 开心, 但比较麻烦的环境配置, 不过总体来说还是挺开心的.  

这里只是对自己的环境配置做个记录, 下回再来个新mac就不用向这么多了。  


## Mac OS 系统配置

### 触摸板

#### 轻点来点按
系统便好设置 -> 触摸板 -> 光标与点按 -> 轻点来点按
![轻点来点按](/static/images/mac-env/touchpad1.jpg)

#### 三指拖移
系统便好设置 -> 辅助功能 -> 鼠标与触摸板 -> 触控板选项 -> 启用拖移 -> 三指拖移
![三指拖移](/static/images/mac-env/touchpad2.jpg)

### ssh远程登录
新的系统只能通过ssh登录到其他机器, 无法从其他机器ssh到自己的机器, 需要允许这个操作  
系统便好设置 -> 共享 -> 远程登录
![ssh远程登录](/static/images/mac-env/ssh.jpg)


## 开发环境配置

### homebrew
``` bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
[参考](http://brew.sh/)  
brew的bin会安装到/usr/local/bin/下, 个人推荐用brew管理mac上的包,
需要用什么包直接用brew装下, 比如python, git, 不要用mac自带的, 特别在Mac OS X 10.11.4 El Capitan之后  
之前可以用`brew versions pkg`查看可安装的包的版本, 但新的brew提供了这种方式,  
先要`brew tap homebrew/versions`, 然后用`brew search xxx`的时候就能看到不同版本的包, 直接`brew install xxx-v.x`就可以了


### terminal 颜色
[配置文件](/static/downloads/mac-env/Blackboard-sp.terminal)

### ls颜色
1. 通过Homebrew安装Coreutils  
brew install xz coreutils  
注：Coreutils并不依赖于xz，但它的源码是用xz格式压缩的，安装xz才能解压。  

2. 生成颜色定义文件  
`gdircolors --print-database > ~/.dir_colors`  
gdircolor的作用就是设置ls命令使用的环境变量LS_COLORS（BSD是LSCOLORS），我们可以修改~/.dir_colors自定义文件的颜色，此文件中的注释已经包含各种颜色取值的说明。

3. 在~/.bash_profile配置文件中加入以下代码
``` bash
brew list | grep coreutils > /dev/null ;
"$(brew --prefix coreutils)/libexec/gnubin:$PATH"
alias 'ls -F --show-control-chars --color=auto'
gdircolors -b $HOME/.dir_colors
```
[参考](http://blog.csdn.net/windows1989/article/details/8882642)

### grep颜色
在~/.bash_profile配置文件中加上alias定义。
``` bash
alias 'grep --color'
alias egrep'egrep --color'
alias fgrep'fgrep --color'
```
[参考](http://blog.csdn.net/windows1989/article/details/8882642)

### vim
我的python ide  
直接用clne[github](https://github.com/HenryChenV/vimrc)上的项目安装

### MySQL(后端开发少不了)
[下载地址](http://dev.mysql.com/downloads/mysql/)  
双击安装，安装后会给出root用户密码, 最好记住, 不然又得绕一圈重置密码  
[参考](http://blog.sina.com.cn/s/blog_9ea3a4b70101ihl3.html)

### git&&补全
``` bash
brew install bash 
brew install bash-completion
brew install git
```
先更新下bash, 然后安装不全, 然后用brew安装下git
~/.bash_profile中加入  
``` bash
if [ -f $(brew --prefix)/etc/bash_completion ]; then                               
. $(brew --prefix)/etc/bash_completion                                             
fi  ]
```

### virtualenv
``` bash
pip search virtualenv
sudo easy_install virtualenvwrapper 
mkdir $HOME/.virtualenvs
```
~/.bash_profile中添加  
``` bash
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```
[参考](http://liuzhijun.iteye.com/blog/1872241)

### python
我的系统为Mac OS X 10.11.4 El Capitan, 系统在安全上做了些改动, 导致pip无法安装软件, 因为系统为了安全, 防止pip在某些目录下新建目录
解决方法有2个, 一个是用上面的virtualenv, 
另一个就是用brew安装python2.7.10。  
但是brew直接安装的是python2.7.11, 对python2.7.10的动态库不支持,
没搞懂不支持为什么安装时候不自己重新编译个, 也许是少数吧,
我刚好碰到了。这事解决方法也有两个, 一个是自己去编译安装2.7.11,
也许能解决这个问题,
但我怕又会引起其他的版本问题，索性直接用brew装2.7.10算了,但是brew不支持python的多版本,
用brew安装python2.7.10的方法如下:  
```
brew uninstall python
brew edit python
```
修改:
``` text
- url "https://www.python.org/ftp/python/2.7.11/Python-2.7.11.tgz"  
+ url "https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tgz"   
- sha256 "82929b96fd6afc8da838b149107078c02fa1744b7e60999a8babbc0d3fa86fc6"  
+ sha256 "eda8ce6eec03e74991abb5384170e7c65fcd7522e409b8e83d7e6372add0f12a"  
```
最后
``` bash
brew install python
```
如果在自己的库里面找不到，会去python官网找


## 工具

### vmware fusion
虚拟机必备

### MacVim
比linux上的vim更好用，目前看来是这样的

### haroopad
markdown编辑器  
[配置文件](/static/downloads/mac-env/Haroopad-2016-06-06-setting.json)
