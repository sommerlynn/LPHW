### 12.py `raw_input()`和`input()`的区别
1.
```python
>>> raw_input_B = raw_input("raw_input: ")
raw_input: 123
>>> type(raw_input_B)
<type 'str'>
>>> input_B = input("input: ")
input: 123
>>> type(input_B)
<type 'int'>
```
 `raw_input()`  
 * 用这个最好，
 * 输入全部变为 string

 `input()`  
 * 接收的是一个合法的 **python 表达式**
 * 输入 str 需要加引号
 * 可以计算：*input( 1 + 3 ) 会返回 int 型的 4 *


2. 今天学的新指令 `python -m pydoc raw_input`  pydoc是一个帮助文档
