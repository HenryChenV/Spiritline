Title: 软链接，硬链接
Date: 2016-01-30 02:20
Modified: 2016-01-31 18:57
Tags: system, hard link, soft link, symbolic link
Slug: soft-and-hard-link
Authors: Henry Chen
Summary: 从incode的角度解释软链接和硬链接的区别，联系
Status: published

[TOC]



# 概论
玩linux肯定得遇到hard link和soft(symbolic)link的问题，之前看的文章感觉不够深入，这次找到了篇好文。
详情点击[传送门](http://www.ibm.com/developerworks/cn/linux/l-cn-hardandsymb-links/index.html),以下仅为学习笔记.


# 笔记

## 知识点

### inode
> 我们知道文件都有文件名与数据，这在 Linux 上被分成两个部分：用户数据 (user data) 与元数据 (metadata)。用户数据，即文件数据块 (data block)，数据块是记录文件真实内容的地方；而元数据则是文件的附加属性，如文件大小、创建时间、所有者等信息。在 Linux 中，元数据中的 inode 号（inode 是文件元数据的一部分但其并不包含文件名，inode 号即索引节点号）才是文件的唯一标识而非文件名。文件名仅是为了方便人们的记忆和使用，系统或程序通过 inode 号寻找正确的文件数据块。
![通过文件名打开文件](/images/sysops/find-file-by-filename.jpg)

```bash 
# stat /home/harris/source/glibc-2.16.0.tar.xz 
File: /home/harris/source/glibc-2.16.0.tar.xz
Size: 9990512      Blocks: 19520      IO Block: 4096   regular file 
    Device: 807h/2055d      Inode: 2485677     Links: 1 
Access: (0600/-rw-------)  Uid: ( 1000/  harris)   Gid: ( 1000/  harris) 
    ... 
    ... 
# mv /home/harris/source/glibc-2.16.0.tar.xz /home/harris/Desktop/glibc.tar.xz 
# ls -i -F /home/harris/Desktop/glibc.tar.xz 
    2485677 /home/harris/Desktop/glibc.tar.xz ) )`
```  
  
### 创建hard link命令
```bash
link oldfile newfile 
ln oldfile newfile
```

### hard link 特性
hard link 是有着相同incode的不同名文件
+ 文件有相同的incode和data block；
+ 只能对已经存在的文件创建；
+ 不能交叉文件系统
+ 不能对目录创建，仅可对文件
+ 删除一个hard link文件不影响其他相同incode号文件

```bash
# ls -li 
total 0 

// 只能对已存在的文件创建硬连接
# link old.file hard.link 
link: cannot create link 'hard.link' to 'old.file': No such file or directory 

# echo "This is an original file" > old.file 
# cat old.file 
This is an original file 
# stat old.file 
File: 'old.file'
Size: 25           Blocks: 8          IO Block: 4096   regular file 
    Device: 807h/2055d      Inode: 660650      Links: 2 
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root) 
    ... 
// 文件有相同的 inode 号以及 data block 
# link old.file hard.link | ls -li 
    total 8 
    660650 -rw-r--r-- 2 root root 25 Sep  1 17:44 hard.link 
    660650 -rw-r--r-- 2 root root 25 Sep  1 17:44 old.file 

// 不能交叉文件系统
# ln /dev/input/event5 /root/bfile.txt 
    ln: failed to create hard link '/root/bfile.txt' => '/dev/input/event5': 
    Invalid cross-device link 
# df -i --print-type 
    Filesystem     Type       Inodes  IUsed    IFree IUse% Mounted on 
    /dev/sda7      ext4      3147760 283483  2864277   10% / 
    udev           devtmpfs   496088    553   495535    1% /dev 
    tmpfs          tmpfs      499006    491   498515    1% /run 
    none           tmpfs      499006      3   499003    1% /run/lock 
    none           tmpfs      499006     15   498991    1% /run/shm 
    /dev/sda6      fuseblk  74383900   4786 74379114    1% /media/DiskE 
    /dev/sda8      fuseblk  29524592  19939 29504653    1% /media/DiskF 

// 不能对目录进行创建硬连接
# mkdir -p old.dir/test 
# ln old.dir/ hardlink.dir 
    ln: 'old.dir/': hard link not allowed for directory 
# ls -iF 
    660650 hard.link  657948 old.dir/  660650 old.file
```

### 测试文件系统 inode 耗尽但仍有磁盘空间的情景
```bash
# dd if=/dev/zero of=mo.img bs=5120k count=1 
# ls -lh mo.img 
-rw-r--r-- 1 root root 5.0M Sep  1 17:54 mo.img 
# mkfs -t ext4  -F ./mo.img 
... 
    OS type: Linux 
    Block size=1024 (log=0) 
Fragment size=1024 (log=0) 
    Stride=0 blocks, Stripe width=0 blocks 
    1280 inodes, 5120 blocks 
    256 blocks (5.00%) reserved for the super user 
    ... 
    ... 
    Writing superblocks and filesystem accounting information: done 

# mount -o loop ./mo.img /mnt 
# cat /mnt/inode_test.sh 
#!/bin/bash 

    for ((i = 1; ; i++)) 
    do 
    if [ $? -eq 0 ]; then 
    echo  "This is file_$i" > file_$i 
    else 
    exit 0 
    fi 
    done 

# ./inode_test.sh 
    ./inode_test.sh: line 6: file_1269: No space left on device 

# df -iT /mnt/; du -sh /mnt/ 
    Filesystem     Type Inodes IUsed IFree IUse% Mounted on 
    /dev/loop0     ext4   1280  1280     0  100% /mnt 
    1.3M    /mnt/ ]
```

### soft link 特性
+ soft link有自己的文件属性及权限
+ 可以对不存在的文件或目录创建软链接
+ 可交叉文件系统
+ 可以对文件或目录创建
+ 删除soft link 不影响原文件，删除原文件soft link会变成死链

![链接访问](/images/sysops/visit-soft-link.jpg 链接访问)


### 使用命令 find 查找软链接与硬链接
```bash
// 查找在路径 /home 下的文件 data.txt 的软链接
# find /home -lname data.txt 
/home/harris/debug/test2/a 

// 查看路径 /home 有相同 inode 的所有硬链接
# find /home -samefile /home/harris/debug/test3/old.file 
/home/harris/debug/test3/hard.link 
/home/harris/debug/test3/old.file 

# find /home -inum 660650 
/home/harris/debug/test3/hard.link 
/home/harris/debug/test3/old.file 

// 列出路径 /home/harris/debug/ 下的所有软链接文件
# find /home/harris/debug/ -type l -ls 
656662 0 lrwxrwxrwx 1 harris harris 1 Sep 1 14:37 /home/harris/debug/test2/b -> a
656627 0 lrwxrwxrwx 1 harris harris 8 Sep 1 14:37 /home/harris/debug/test2/a -> 
data.txt
789467 0 lrwxrwxrwx 1 root root 8 Sep 1 18:00 /home/harris/debug/test/soft.link -> old.file 
789496    0 lrwxrwxrwx   1 root     root            7 Sep  1 18:01 
/home/harris/debug/test/soft.link.dir -> old.dir
```

## 问题
Q1. 对于作者提到的“若系统允许对目录创建硬链接，则会产生目录环。” 表示怀疑，
如果这是不能对目录创建硬链接的原因，那么对目录创建软链接也会存在这个问题，按你的意思，这种环只会在对目录创建硬链接(假设可以)的时候出现
