Title: 论坛搭建全记录 
Date: 2015-12-28 20:00
Modified: 2016-01-30 01:53 
Tags: centos7, nginx, uwsgi, mysql, python
Slug: note-for-build-website
Authors: Henry Chen
Summary: 搭建论坛的简单记录,搭了个论坛玩。以下文字时写给自己看的，首要目的是记录，其次才是得瑟。会有些啰嗦，因为不想写那种从头到位都很顺利跟说明书似的帖子。
Status: published

[TOC]

> 搭了个论坛玩。
> 以下文字时写给自己看的，首要目的是记录，其次才是得瑟。会有些啰嗦，因为不想写那种从头到位都很顺利跟说明书似的帖子。

## 概况
基本思路是LNMP:

+ L: CentiOS7
  为什么用7，没什么特别的原因，喜欢7这个数字，CentOS7刚出来的时候就装了个，只是当时电脑配置差，玩得不爽，耿耿于怀，这次顺便了了这个结，当然坑也会有的。为什么不用ubuntu，就ubuntu默认防火墙关闭，CentOS默认防火墙打开这一点就让我不打算用ubuntu了。

+ N: nginx
  没认真笔记多nginx喝apache，只知道大家现在更偏向于用nginx跑python项目，nginx也有虚拟主机，反向代理的玩法，可以很方便的在一台服务器上搭建多个网站。

+ M: MySQL
  被oracle搞去了，因为担心被闭源，所以CentOS7用了由社区维护的MySQL的一个分支，MariaDB，但起起来

+ P: python
  用的django框架，论坛直接用的开源软件misago

## 搭建

### CentOS7

#### **系统安装**
直接用的阿里的ECS，创建虚拟机的时候选的CentOS7的镜像。 我觉得用root用户直接搭建环境不好，于是创建了一个管理员账号，以我自己命名，命令:`adduser henry -c "Henry Chen"`用户henry在用sudo的时候不需要输入密码，命令:`visudo`，会打开一个文件，找到这两行:
``` bash
## Same thing without a password
%wheel  ALL=(ALL)       NOPASSWD: ALL
```
去掉第二行前面的注释(这里已经去掉了),记下wheel这个组，只要在这个组里面的用户，使用sudo都不用输入密码。
将henry加入到这个组中:`usermod -a -G henry wheel`。
安装必要的软件: git, etc

#### **安装必需的依赖包**
``` bash
sudo yum install libjpeg-turbo-devel zlib-devel python-devel libfreehand-devel python-imgcreate
```

#### **防火墙**
这个镜像用起来跟本地不一样，本地安装的CentOS7种，防火墙会阻止几乎全部端口，而ECS中只要你用到了哪个端口，它会帮你自动打开这个端口，不用自己操作防火墙。本地做实验的时候需要操作防火墙，需要以下命令:
``` bash
firewall-cmd —list-port
firewall-cmd --zone=dmz --add-port=80/tcp
firewall-cmd --zone=dmz --add-port=3306/tcp
```
若要永久生效方法在后面加上`--permanent`

这是我遇到的第一个坑，装上mysql，添加好用户和权限后却不能登录，google出来的方向都是让我去改iptables，但CentOS7中将iptables换成了firewall，有网友建议卸载firewall，安装iptables，但我觉得人家用了firewall总是有他的道理的，于是决定用firewall。

### MySQL

#### **安装**
因为觉得数据库能用就行，没必要源码编译，于是想直接用源里面的，但CentOS7的源中并没有自带mysql，而是MariaDB，这是由社区维护的一个MySQL的分支，但据说启动后查看进程看到的是mariadb不是mysql，有点怪怪的，于是我去官方找了个源，然后安装。
``` bash
wget http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm
sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm
sudo yum install mysql-community-server
```
在安装完成后会看到replaced mariadb的信息，这个有意思。

+ 初次安装mysql，root用户没有密码，为了安全起见，最好设置下密码  
           `set password for 'root'@'localhost' =password('password');`

#### **新建用户&权限管理**
``` bash
create user 'username'@'%' identified by 'password';
create user 'username'@'localhost' identified by 'password';
grant all privileges on database.* to username@'%'identified by 'password';
grant all privileges on database.* to username@'%'identified by 'password';
```

#### **修改编码配置**
在`/etc/my.cnf`中加上如下配置:
``` text
[mysql]
default-character-set =utf8
```

这里的字符编码必须和`/usr/share/mysql/charsets/Index.xml`中一致。
创建数据库的时候也需要加上字符编码的选项: `create database xxx default character set utf8;`
参考: [centos7 mysql数据库安装和配置](http://www.cnblogs.com/starof/p/4680083.html)

### 虚拟环境

#### 安装步骤:
##### 安装virtualenv和virtualenvwrapper(源码或者pip)
##### 创建虚拟环境目录
`mkdir $HOME/.virtualenvs`
##### 将配置加入~/.bashrc
``` bash
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
source ~/.bashrc
```
##### 测试
`mkvirtualenv bookbbs`，没问题就ok

+ 参考:[Python 虚拟环境:Virtualenv](http://liuzhijun.iteye.com/blog/1872241)
   此时就可先在虚拟环境中安装好所需的依赖，然后把项目用sudo python manage.py runserver 0.0.0.0:80的形式跑起来了，我在做到这一步的时候是先把项目跑起来的，因为没在CentOS7上玩过，怕跑不起来，所以想先在这一步看看跑起来的效果如何。

### uwsgi

因为是所有项目都要用的，所以不该放在某个虚拟环境中，应该在虚拟环境外安装，如果不是root则需要sudo的权限。然后需要找一个uwsgi的配置文件，以及启动脚本，可以不用启动脚本，自己将启动命令加到开机启动的脚本中，但还是觉得启动脚本的方式方便管理些。

#### 安装: 无论源码还是pip都很顺利，没什么好说的

#### 单独测试是否安装成功
新建test.py文件，内容如下:
``` python
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return "Hello World"
```

然后在终端运行: `uwsgi --http :8001 --wsgi-file test.py`

在浏览器内输入:`http://127.0.0.1:8001`(视情况更改ip)，看是否有`“Hello World”`输出，若没有输出，检查安装过程。

#### 项目配置文件
``` text
[uwsgi]
socket = /path/to/socket
#socket = 127.0.0.1:8989
#plugin = python
wsgi-file = /path/to/project/wsgi.py
processes = 2
master = true
max-requests = 5000
daemonize = /path/to/log
logfile-chmod = 644
pidfile = /path/to/pid
limit-as = 1000
enable-threads = true
vacuum = true
log-maxsize = 40960000
threads = 2
virtualenv = /path/to/virtualenv
uid = 1000  # 运行的用户
```
#### 启动脚本
没在网上找到个满意的，所以改造了下，这个脚步目前只能启动uwsgi进程，但是没法杀进程。启动后，指定目录下的项目配置文件如果发生改变，会自动重启相应进程(uwsgi支持通过--emperor制定配置文件目录，如果配置文件发生改变，会自动重启相应进程).
以下是脚本:
``` bash
#!/bin/bash
# chkconfig:   - 90 15
#
# wsgI init Script
#
# processname: uwsgi
# description: Used to run python and wsgi web applciations.
# author: Miguel Clara (miguelmclara@gmail.com)
. /etc/rc.d/init.d/functions

# vars
###########################
prog=/path/to/uwsgi (which uwsgi)
desc=uWSGI
daemoN_OPTS="--emperor /path/to/uwsgi/configs " # Change this if needed!
lockfile=/path/to/uwsgi.lock

start () {
  echo -n "Starting $DESC: "
  daemon $PROG $DAEMON_OPTS
  retval=$?
  echo
  [ $retval -eq 0 ] && touch $lockfile
  return $retval
}

stop () {
  echo -n "Stopping $DESC: "
  killproc $PROG
  retval=$?
  echo
  [ $retval -eq 0 ] && rm -f $lockfile
  return $retval
}

reload () {
echo "Reloading $NAME"
  killproc $PROG -HUP
  retVAL=$?
  echo
}

restart () {
    stop
    start
}

rh_status () {
  status $PROG
}

rh_status_q() {
  rh_status >/dev/null 2>&1
}

case "$1" in
  start)
    if ! pidof $PROG >/dev/null; then
        rh_status_q && exit 0
        $1
    else
        echo -e "\n$DESC is already started...\n"
    fi
 ;;
  stop)
    if pidof $PROG >/dev/null; then
        rh_status_q || exit 0
        $1
    else
        echo -e "\n$DESC can not be stoped because its not running...\n"
    fi
    ;;
  restart|force-reload)
    $1
    ;;
  reload)
    rh_status_q || exit 7
    $1
    ;;
  status)
    rh_status
    ;;
  *)
    echo "Usage: $0 {start|stop|restart|reload|force-reload|status}" >&2
    exit 2
    ;;
esac
exit 0
```
#### 将脚本添加到系统
```bash
cp this_script /etc/init.d/uwsgi
sudo chkconfig —add uswgi
sudo chkconfig uwsgi on
```
#### 验证
重启服务器，查看进程是否存在。重启不仅是为了验证是否开机自启动，如果不重启可能会遇到很奇怪的问题，比如不知道什么东西启动了进程，杀业杀不完。

### nginx

#### 源码编译  
版本: nginx-1.8.0.tar.gz.
```bash
./configure --prefix=/home/henry/softwares/nginx \
    --user=henry \
    --group=henry \
    --with-pcre=/home/henry/packages/pcre-8.37 \
    --with-http_realip_module \
    --with-http_stub_status_module \
    --with-http_gzip_static_module \
    --with-http_stub_status_module \
    --with-http_ssl_module

make
make install
```

#### 启动脚本
init.d的脚本:

``` bash
#!/bin/sh
#
# nginx - this script starts and stops the nginx daemon
#
# chkconfig:   - 85 15
# description:  NGINX is an HTTP(S) server, HTTP(S) reverse \
#               proxy and IMAP/POP3 proxy server
# processname: nginx
# config:      /home/henry/softwares/nginx/conf/nginx.conf
# config:      /etc/sysconfig/nginx
# pidfile:     /home/henry/softwares/nginx/logs/nginx.pid

# Source function library.
. /etc/rc.d/init.d/functions

# Source networking configuration.
. /etc/sysconfig/network

# Check that networking is up.
[ "$NETWORKING" = "no" ] && exit 0

nginx="/home/henry/softwares/nginx/sbin/nginx"
prog=$(basename $nginx)

NGINX_CONF_FILE="/home/henry/softwares/nginx/conf/nginx.conf"

[ -f /etc/sysconfig/nginx ] && . /etc/sysconfig/nginx

lockfile="/home/henry/softwares/nginx/subsys/nginx.lock"

make_dirs() {
   # make required directories
   user=`$nginx -V 2>&1 | grep "configure arguments:" | sed 's/[^*]*--user=\([^ ]*\).*/\1/g' -`
   if [ -z "`grep $user /etc/passwd`" ]; then
       useradd -M -s /bin/nologin $user
   fi
   options=`$nginx -V 2>&1 | grep 'configure arguments:'`
   for opt in $options; do
       if [ `echo $opt | grep '.*-temp-path'` ]; then
           value=`echo $opt | cut -d "=" -f 2`
           if [ ! -d "$value" ]; then
               # echo "creating" $value
               mkdir -p $value && chown -R $user $value
           fi
       fi
   done
}

start() {
    [ -x $nginx ] || exit 5
    [ -f $NGINX_CONF_FILE ] || exit 6
    make_dirs
    echo -n $"Starting $prog: "
    daemon $nginx -c $NGINX_CONF_FILE
    retval=$?
    echo
    [ $retval -eq 0 ] && touch $lockfile
    return $retval
}

stop() {
    echo -n $"Stopping $prog: "
    killproc $prog -QUIT
    retval=$?
    echo
    [ $retval -eq 0 ] && rm -f $lockfile
    return $retval
}

restart() {
    configtest || return $?
    stop
    sleep 1
    start
}

reload() {
    configtest || return $?
    echo -n $"Reloading $prog: "
    killproc $nginx -HUP
    RETVAL=$?
    echo
}

force_reload() {
    restart
}

configtest() {
  $nginx -t -c $NGINX_CONF_FILE
}

rh_status() {
    status $prog
}

rh_status_q() {
    rh_status >/dev/null 2>&1
}

case "$1" in
    start)
        rh_status_q && exit 0
        $1
        ;;
    stop)
        rh_status_q || exit 0
        $1
        ;;
    restart|configtest)
        $1
        ;;
    reload)
        rh_status_q || exit 7
        $1
        ;;
    force-reload)
        force_reload
        ;;
    status)
        rh_status
        ;;
    condrestart|try-restart)
        rh_status_q || exit 0
            ;;
    *)
        echo $"Usage: $0 {start|stop|status|restart|condrestart|try-restart|reload|force-reload|configtest}"
        exit 2
esac
```

#### 添加脚本到系统
``` bash
sudo cp this_script /etc/init.d/nginx
sudo chkconfig —add nginx
sudo chkconfig nginx on
```
#### 验证
重启服务器,访问ip，看看是否能出现nginx成功的界面。
#### 网站配置
采用虚拟主机的方式，在主配置文件中指定虚拟主机配置文件目录，目录中给每个网站写一个配置文件:
##### 主配置文件nginx.conf:
``` text
user  henry;
worker_processes  1;

error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

pid        logs/nginx.pid;

events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    gzip  on;

    include conf.d/*.conf;
}
```

##### vhost 配置
在跟nginx.conf同级目录下`mkdir conf.d`,用于存放vhost配置文件
vhost文件: 例如:bookbbs.conf:

``` text
server {
   listen 80;
   server_name  192.168.30.154;

   charset utf-8;
   access_log  logs/bookbbs_access.log;

   location /static/ {
      alias /path/to/static/dir;
   }

   location /media/ {
      alias /path/to/media/dir;
   }

   location / {
       uwsgi_pass unix:///home/henry/softwares/nginx/logs/BookBBS.sock;
       include uwsgi_params;
       client_max_body_size    10m;
   }
}
```
要注意的是，配置文件中该加”/“的地方通通都得加上，否则会失败。
ps: 配置文件在git.oschin.net中能找到(私有仓库)
