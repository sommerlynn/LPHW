### 16.py 读写文件
#### Bash运行问题  
win7系统，用git bash运行练习16开头的语句：
```python
print """We're going to ERASE %r.
If you don't want that, hit CTRL -C (^C).
If you do want that, hit RETURN.""" %filename
raw_input("?")
```
bash竟然把这两句话的顺序颠倒了：我需要输入raw_input才能print上面的语句  

```text
LinYH@HL  /d/Github/lphw (master)
$ python 16.py test.txt

We're going to ERASE 'test.txt'.
If you don't want that, hit CTRL -C (^C).
If you do want that, hit RETURN.
?
LinYH@HL  /d/Github/lphw (master)
$
```
然后我切换到 powershell 就能正常运行。
在[cocode](http://cocode.cc/t/lphw-ex16-bash/6479/1)上发帖问了。


#### 附加题2 使用`read`和`argv`读取刚才新建的文件
错误：
```python
from sys import argv
script, filename = argv

txt = open(filename)
txt.read()
txt.close()
```
第二句应该是：`print txt.read()`
#### 附加题5 'w'之后还需要truncate吗
不需要。
[python的tutorial](https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files)说到：
* 'w' for only writing **(an existing file with the same name will be erased)**
但是'r+'（读写）的时候不会进行括号内的操作，所以这时truncate就有必要了

* If the end of the file has been reached, f.read() will return an empty string ("").

* f.write(): To write something other than a string, it needs to be converted to a string first
* tell() 和 seek(offset, from_what) 可以定位指针

* It is good practice to use the `with` keyword when dealing with file objects. This has the advantage that the file is properly closed after its suite finishes, even if an exception is raised on the way. It is also much shorter than writing equivalent `try-finally` blocks

中文的参数介绍：[Python：文件的读取、创建、追加、删除、清空](http://www.open-open.com/lib/view/open1413527388231.html)
