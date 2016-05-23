>首先我是使用了Github for Windows创建了一个仓库 LPHW，想着用来记录学习《笨办法学python》的代码。参考了编程指南的每日一题，给每个习题创建了一个分支。然而写了几个习题后发现每个习题其实只有一个文件，没必要弄分支。那我就合并吧？

>然而windows版的本地仓库**没有合并选项**。这。就。很。尴。尬。了！

>我删了整个仓库。幸好前面的代码很无聊。

但是不能删了完事啊！于是学习用git shell操作分支，顺便也学了用markdown来记录  
依旧是*边试边看，边改边理解*的errorlog

所以这篇log里有：

    建分支
    分支对比————要add和commit
    合并分支

    Markdown使用感受

    学习时用到的网址

----
### 新建一个分支version1
建完仓库后会有一个主支（master），但是新建的分支都是**当前目录**的派生

    D:\Github\LPHW [master]> git branch version1`
    D:\Github\LPHW [master]> git checkout version1`
    Switched to branch 'version1'`
    D:\Github\LPHW [version1]

这里创建一个version1.txt，可以看见添加了3行，且branch后面出现红色的数字

    D:\Github\LPHW [version1 +1 ~0 -0 !]> cat version1.txt
    version1 edit:
    create
    add

* [version1 +1 ~0 -0 !]

  +表示增加，~表示修改，-表示删除

  这里表示的是一个缓存的状态，就像是*一张独立的草稿纸*

  `git add`后branch的数字变成绿色
  `git commit`之后数字消失，**到这里缓存才算放进分支**

version1最终回：

    Mode                LastWriteTime     Length Name
    ----                -------------     ------ ----
    -a---         2016/4/10     15:39        395 .gitattributes
    -a---         2016/4/11      1:29         26 version1.txt

### 再分支ver1-1
在version1下新建分支并切换，能发现是继承（不是复制）了version1

    D:\Github\LPHW [version1]> git checkout -b ver1-1
    Switched to a new branch 'ver1-1'
    D:\Github\LPHW [ver1-1]> ls

        目录: D:\Github\LPHW
    Mode                LastWriteTime     Length Name
    ----                -------------     ------ ----
    -a---         2016/4/10     15:39        395 .gitattributes
    -a---         2016/4/11      1:29         29 version1.txt

和version1的区分：修改txt，加个md文件

### 两个分支对比
所以ver1-1看起来是这样（未add和commit）

    D:\Github\LPHW [ver1-1 +1 ~1 -0 !]> ls

        目录: D:\Github\LPHW
    Mode                LastWriteTime     Length Name
    ----                -------------     ------ ----
    -a---         2016/4/10     15:39        395 .gitattributes
    -a---         2016/4/11      1:34          0 1-1.md
    -a---         2016/4/11      1:34         60 version1.txt
***WARNING:*** 如果**不add和commit，所有变更都会切换到别的分支**，就像你把手头上的草稿纸拿到别的地方

保存后切换回version1，没有ver1-1的变动

    Mode                LastWriteTime     Length Name
    ----                -------------     ------ ----
    -a---         2016/4/10     15:39        395 .gitattributes
    -a---         2016/4/11      1:52         29 version1.txt  

### 合并分支`git merge`
默认**合并到当前分支**，这里我想把ver1-1合并到version1

* 错误示范：


    D:\Github\LPHW [master1]> **git merge version1 ver1-1**
    Updating f759f41..3ab46c6
    Fast-forward
    1-1.md       | 0
    version1.txt | 7 +++++++
    2 files changed, 7 insertions(+)
    create mode 100644 1-1.md
    create mode 100644 version1.txt

  1. 我把version1和ver1-1都合并到master1里了
  2. merge 不是合并前后两个分支，而是把命令后的分支都合并到当前分支


* 正确操作：
切换到version1分支再操作


    D:\Github\LPHW [ver1-1]> git checkout version1
    Switched to branch 'version1'
    D:\Github\LPHW [version1]> git merge ver1-1
    Updating 32de473..3ab46c6
    Fast-forward
    1-1.md       | 0
    version1.txt | 4 ++++
    2 files changed, 4 insertions(+)
    create mode 100644 1-1.md
    D:\Github\LPHW [version1]> ls

    Mode                LastWriteTime     Length Name
    ----                -------------     ------ ----
    -a---         2016/4/10     15:39        395 .gitattributes
    -a---         2016/4/11      2:28          0 1-1.md
    -a---         2016/4/11      2:28         67 version1.txt

## DONE！
---
### Markdown使用感受
第一篇Markdown试水作。起因是在onenote里记录branch的学习笔记时，不知道怎么记代码，于是我想到了代码编辑器atom，可喜可贺支持Markdown！摸索了一会上手写，很赞！终于有代替txt的生产工具了！

发表到博客时 copy as HTML ，感觉比用wp的插件方便。

我会把Markdown看成一把大锤子，哐哐哐的把HTML的困难敲碎，有些需求细节就顾不上了（比如当我需要代码行号的时候）。

但是onenote更像一本笔记，所以下一步要想个办法导回去。

----
* Git branch:
  <http://blog.chinaunix.net/uid-26185912-id-3332628.html> 讲到了缓存的commit

* Markdown:
  <http://www.cnblogs.com/itech/p/3800982.html> 链接合集
  <http://www.ituring.com.cn/article/23> 图灵社区发帖的markdown语法
