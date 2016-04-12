## 5.py `%`符号的位置

```python
#错误的多变量引用
print "i've got %s eyes and %s hair." (% my_eyes, % my_hair)

#应该在%之后用括号把变量括起来
print "i've got %s eyes and %s hair." % (my_eyes, my_hair)
```

## 6.py 字符串里用`%r`套用字符串

```python
hilarious = False
joke_evaluation = "Isn't that joke so funny? %r"
print joke_evaluation % hilarious
```
这里字符串中包含了字符串变量，最后的`print`中**要加上引用的变量**

## 7.py `,`表示不换行
1. print语句逗号（comma）表示不换行
2. 重复print语句的表示
```python
print "." * 10
```

## 8.py `“%r”`带来的引号
```python
formatter = "%r %r %r %r"

print formatter % (1, 2, "3", '4')
print formatter % ("one", "two", 'three', 'four')

print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "i had this thing.",
    "that you could type up right.",
    "but it didn't sing",
    "so i said goodnight"       # not a good lyric
)
```
结果：
```python
1 2 '3' '4'
'one' 'two' 'three' 'four'
True False False True
'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
'i had this thing.' 'that you could type up right.' "but it didn't sing" 'so i said goodnight'
```
>%r表示用repr函数转换字符串后，然后再替换掉%r的位置  
repr函数会自动给字符串加上引号,当字符串含有单引号时，比如"don't"，repr函数会加上双引号而不是单引号, 而且在print语句中输出了单引号，单引号应该还保留，只不过后面多了个双引号，而不是只输出了双引号  

所以其实是两个问题：
1. 写的是双引号：表示变量是字符串，和单引号一样；  
输出有单引号：因为变量是字符串，repr函数处理后会自动加引号。对比输出数字的第一句就能发现变量不是字符串时没有引号。
2. 对比输出数字的第一句就能发现变量不是字符串时没有引号。  
所以作者说%r是调试bug用的，它会输出变量的存储方式
3. 更多字符串见：[【循序渐进学Python】3. Python中的序列——字符串](http://www.cnblogs.com/IPrograming/p/Python_string.html)


## 9.py 用`%r`不加`,`
```Python
print "Here are the months: ", months
print "print months with %%r %r" % months
```
注意有没有逗号的区别

## 10.py `\r`和`,`的妙用解释
Escape Sequences
```python
while True:
    for i in ["/", "—", "|", "\\", "|"]:
        print "%s\r" % i,
```
这个在atom里跑不了，我试着删掉了最后的逗号，于是就进入无限while循环了，悲剧的是不知道atom里怎么结束。从git shell里打开就能看到**/在旋转**，很可爱。必须有`,`才可以。这让我对`\r`和`\n`产生了疑惑，上网查了下：

>### \r
[wiki的解释](https://www.baidu.com/link?url=TXVTJmFpk-eSr85f5jnRqce3GZPLJBjpE_XJFj3A5pjY31ZMldy8t_YVdUpLCKDAdXgVKhB_dGC_0Vva-x7oCK&wd=&eqid=917b93330000bfb000000002570ca735, "carriage return")  
[百度百科的解释:](http://baike.baidu.com/link?url=4MMtxm-rVFTtJfrtJWfneURT8hG2shBzvlnO8z8okLRZ0Jy2P6PZXVLs1AKanZXgQrBS_5uMSYvTkyaHkNqflq)  
```
最早，在打字机上的打字位置是固定的，归位兼换行的扳手用于将承载装纸滚筒的机架（carriage）移到最右边，以便令印字位置对准一行的开头，同时顺便转动滚筒，换至下一行。后来，当打字机的滚筒不再横向移动，改由承载印字头的字车（印字头 carriage）移回到本行的起始位置。  
Carriage Return “归位”这术语是电传打印机（TTY）所使用的 Baudot 码（Baudot Code）的一个控制字符，代表回到一行字的起头，但不代表换行（或称进列）。
归位键第一次由1960年在Smith Corona公司的电动打字机出现。 此键一般被标为 “Carriage Return” 或 “Return”。 为了帮助不说英语的用户学习打字，之后出版的打字机经常被标“↵”符号。[1]
关于“回车键”的来历，还得从机械英文打字机说起。在机械英文打字机上，有一个部件叫“字车”，每打一个字符（原为单词，但是个人觉得这里应该是字符），“字车”就前进一格。当打满一行字符后，打字者就得推动“字车”到起始位置，这时打字机会有两个动作响应：一是“字车”被归位，二是滚筒上卷一行，以便开始输入下一行，这个推动“字车”的动作叫“回车”。后来，在电动英文打字机上，人们增加了一个直接起“回车”作用的键。这个新增的键就被称为“回车键”。
在电脑键盘上，“回车键”上曾经使用过“CR”、“RETURN”的字样，后来才统一确定为“Enter”。
```
最丧病的是竟然不同系统标准不一样：
>Unix系统里，每行结尾只有“<换行>”，即“\n”；Windows系统里面，每行结尾是“<换行><回车>”，即“\n\r”；Mac系统里，每行结尾是“<回车>”。一个直接后果是，Unix/Mac系统下的文件在Windows里打开的话，所有文字会变成一行；而Windows里的文件在Unix/Mac下打开的话，在每行的结尾可能会多出一个^M符号。  

难怪在atom里跑不动。
