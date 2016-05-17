### 15.py open函数 read函数
#### 查了查open函数的用法，发现一些有趣的事：
1. `txt = open(filename)` does **NOT** return the **contents** of the file. It actually makes something called a `file object` like the DVD player is not the DVD the same way the file object is not the file's contents.
1. [Python open()函数文件打开、读、写操作详解](http://www.iplaypython.com/sys/open.html)  
2. [关于python中文件open后去调用read()时需要知道的事情：只需调用一次即可获得文件的全部内容](http://www.crifan.com/python_file_open_then_read_once_will_read_all_file_content/)
>调用read()时，如果不指定size参数，则会一直读，知道文件末尾（EOF）, 即，直接读取文件的全部内容了。  
  即，read()不是读单个字节，而是文件的所有的内容。 所以，此处，既然调用了一次read()了  已经获得了文件的全部的内容了。
  那么如果再次调用，必然是一个字节也读取不到：
  因为已经（文件指针都指）到文件末尾了，没有更多的内容（字节）供你读了。
  所以，必然返回空或-1等值了。

所以[使用open打开文件后一定要记得调用文件对象的close()](http://www.cnblogs.com/allenblogs/archive/2010/09/13/1824842.html)

#### 一些学习tip
1. `__doc__`的用法
  恕我直言，带__的都是辣鸡。
  当我使用help(open)的时候，有一句提示：  
`See file.__doc__ for further information.`  
图样的我见过doc，可是没见过这种格式的，简直蒙蔽，乱输一通不得解。后来才明白是：`open.__doc__`  
  但其实不需要，这样打开连换行符都是\n，太raw了。说的其实是open是file的一种，所以建议查阅file。

  这里面还有一点C指针的影子呢
2. 如果我不去查，我就不会知道read()只能调用一次。而讲到这个问题的博客里也提到：
>这种事情的发生，其实和你自己是否知道此python的read()这个api的详细功能，关系不是很大, 而和你是否掌握学习方法，关系很大。  
换句话说，如果你学习python,掌握了基本的学习方法后，你在使用read()这个函数之前，就会去查查Python的自带的Mannual。  
正常的写代码，学习的思路是：
尽量在写代码之前，通过各种办法，去搞懂你所用的api的含义
然后再动手写，任何事情，不确定的情况下，都不要按照固有的，原有的想法，理念，去理解一个东西，
即不要想当然，因为不同的语言，不同的api，都是不尽相同的。各有各的特点和用法。
必须搞懂你要用的api的真正含义，才能写出正确的，质量高的代码，真正又快又好的实现你要的功能。

可是啊，这样子的话，LPHW又有什么意义呢？不还是要去认真的学manual一样的书吗。我真是郁闷了。


#### 看完drills我发现这几点书里都讲到了。这下真是郁闷了。以后看书还是要！多！点！耐！心！
