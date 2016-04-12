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

### 8.py
