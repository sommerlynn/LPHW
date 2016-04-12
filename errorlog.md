### 5.py

```python
#错误的多变量引用
print "i've got %s eyes and %s hair." (% my_eyes, % my_hair)

#应该在%之后用括号把变量括起来
print "i've got %s eyes and %s hair." % (my_eyes, my_hair)
```

### 6.py

```python
hilarious = False
joke_evaluation = "Isn't that joke so funny? %r"
print joke_evaluation % hilarious
```
这里字符串中包含了字符串变量，最后的`print`中**要加上引用的变量**

### 7.py
1. print语句逗号（comma）表示不换行
2. 重复print语句的表示
```python
print "." * 10
```

### 8.py 关于 % 和字符串
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


### 9.py
