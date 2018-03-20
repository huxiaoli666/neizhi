classmethod 修饰符
描述：classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，
	  但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等
语法:classmethod
参数：无
返回值：返回函数的类方法。
# 案例：
class A(object):
    bar = 1
    def func1(self):  
        print ('foo') 
    @classmethod
    def func2(cls):
        print ('func2')
        print (cls.bar)
        cls().func1()   # 调用 foo 方法
 
A.func2()               # 不需要实例化
*************************************************************************************************
getattr() 函数
描述：用于返回一个对象属性值。
语法：getattr(object, name[, default])
参数：object -- 对象。
	  name -- 字符串，对象属性。
	  default -- 默认返回值，如果不提供该参数，在没有对应属性时，将触发 AttributeError。
返回值：返回对象属性值。
# 案例：
>>>class A(object):
...     bar = 1
... 
>>> a = A()
>>> getattr(a, 'bar')        # 获取属性 bar 值
1
>>> getattr(a, 'bar2')       # 属性 bar2 不存在，触发异常
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'A' object has no attribute 'bar2'
>>> getattr(a, 'bar2', 3)    # 属性 bar2 不存在，但设置了默认值
3
>>>
***********************************************************************************************
locals() 函数
描述：locals() 函数会以字典类型返回当前位置的全部局部变量。
	  对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。
语法：locals()
参数：无
返回值：返回字典类型的局部变量。
# 案例：
>>>def runoob(arg):    # 两个局部变量：arg、z
...     z = 1
...     print (locals())
... 
>>> runoob(4)
{'z': 1, 'arg': 4}      # 返回一个名字/值对的字典
>>>
**********************************************************************************************
repr() 函数
描述：将对象转化为供解释器读取的形式。
语法：repr(object)
参数：object -- 对象。
返回值：返回一个对象的 string 格式。
# 案例：
>>>s = 'RUNOOB'
>>> repr(s)
"'RUNOOB'"
>>> dict = {'runoob': 'runoob.com', 'google': 'google.com'};
>>> repr(dict)
"{'google': 'google.com', 'runoob': 'runoob.com'}"
>>>
**********************************************************************************************
zip() 函数
描述：用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

	 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
语法：zip([iterable, ...])
参数：iterabl -- 一个或多个迭代器;
返回值：返回元组列表
# 案例：
>>>a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 打包为元组的列表
[(1, 4), (2, 5), (3, 6)]
>>> zip(a,c)              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
>>> zip(*zipped)          # 与 zip 相反，可理解为解压，返回二维矩阵式
[(1, 2, 3), (4, 5, 6)]
***********************************************************************************************
compile() 函数
描述：将一个字符串编译为字节代码。
语法：compile(source, filename, mode[, flags[, dont_inherit]])
参数：source -- 字符串或者AST（Abstract Syntax Trees）对象。。
	  filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
	  mode -- 指定编译代码的种类。可以指定为 exec, eval, single。
	  flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。。
	  flags和dont_inherit是用来控制编译源码时的标志
返回值：返回表达式执行结果。
# 案例：
>>>str = "for i in range(0,10): print(i)" 
>>> c = compile(str,'','exec')   # 编译为字节代码对象 
>>> c
<code object <module> at 0x10141e0b0, file "", line 1>
>>> exec(c)
0
1
2
3
4
5
6
7
8
9
>>> str = "3 * 4 + 5"
>>> a = compile(str,'','eval')
>>> eval(a)
17
*****************************************************************************************
globals() 函数
描述：会以字典类型返回当前位置的全部全局变量。
语法：globals()
参数：无
返回值：返回全局变量的字典。
# 案例：
>>>a='runoob'
>>> print(globals()) # globals 函数返回一个全局变量的字典，包括所有导入的变量。
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__',
 '__doc__': None, 'a': 'runoob', '__package__': None}
 ****************************************************************************************
map() 函数
描述：map() 会根据提供的函数对指定序列做映射。

第一个参数 function 以参数序列中的每一个元素调用 function 函数，
返回包含每次 function 函数返回值的新列表。
语法：map(function, iterable, ...)
参数：unction -- 函数，有两个参数
	  iterable -- 一个或多个序列
返回值：Python 2.x 返回列表。
	    Python 3.x 返回迭代器
# 案例：
>>>def square(x) :            # 计算平方数
...     return x ** 2
... 
>>> map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
[1, 4, 9, 16, 25]
>>> map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
[1, 4, 9, 16, 25]
 
# 提供了两个列表，对相同位置的列表数据进行相加
>>> map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
[3, 7, 11, 15, 19]
**************************************************************************************
reversed 函数
描述：返回一个反转的迭代器。
语法：reversed(seq)
参数：seq -- 要转换的序列，可以是 tuple, string, list 或 range。
返回值：返回一个反转的迭代器。
# 案例：
# 字符串
seqString = 'Runoob'
print(list(reversed(seqString)))
 
# 元组
seqTuple = ('R', 'u', 'n', 'o', 'o', 'b')
print(list(reversed(seqTuple)))
 
# range
seqRange = range(5, 9)
print(list(reversed(seqRange)))
 
# 列表
seqList = [1, 2, 4, 3, 5]
print(list(reversed(seqList)))

以上实例输出结果为：

['b', 'o', 'o', 'n', 'u', 'R']
['b', 'o', 'o', 'n', 'u', 'R']
[8, 7, 6, 5]
[5, 3, 4, 2, 1]
**************************************************************************************
__import__() 函数
描述：__import__() 函数用于动态加载类和函数 。

	  如果一个模块经常变化就可以使用 __import__() 来动态载入。
语法：__import__(name[, globals[, locals[, fromlist[, level]]]])
参数：name -- 模块名
返回值：返回元组列表。
# 案例：
##3a.py 文件代码：
 
import os  
 
print ('在 a.py 文件中 %s' % id(os))
###test.py 文件代码：
 
import sys  
__import__('a')        # 导入 a.py 模块
执行 test.py 文件，输出结果为：

在 a.py 文件中 4394716136
***************************************************************************************
complex() 函数
描述：用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。
	  如果第一个参数为字符串，则不需要指定第二个参数。。
语法：class complex([real[, imag]])
参数：real -- int, long, float或字符串；
	  imag -- int, long, float；
返回值：返回一个复数。
# 案例：
>>>complex(1, 2)
(1 + 2j)
 
>>> complex(1)    # 数字
(1 + 0j)
 
>>> complex("1")  # 当做字符串处理
(1 + 0j)
 
# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
>>> complex("1+2j")
(1 + 2j)
*****************************************************************************************
hasattr() 函数
描述：用于判断对象是否包含对应的属性。
语法：hasattr(object, name)
参数：object -- 对象。 			name -- 字符串，属性名。
返回值：如果对象有该属性返回 True，否则返回 False
# 案例：
class Coordinate:
    x = 10
    y = -5
    z = 0
 
point1 = Coordinate() 
print(hasattr(point1, 'x'))
print(hasattr(point1, 'y'))
print(hasattr(point1, 'z'))
print(hasattr(point1, 'no'))  # 没有该属性
输出结果：

True
True
True
False
****************************************************************************************
max() 函数
描述：返回给定参数的最大值，参数可以为序列。
语法：max( x, y, z, .... )
参数：x -- 数值表达式。			y -- 数值表达式。		z -- 数值表达式。
返回值：返回给定参数的最大值。
# 案例：
print ("max(80, 100, 1000) : ", max(80, 100, 1000))
print ("max(-20, 100, 400) : ", max(-20, 100, 400))
print ("max(-80, -20, -10) : ", max(-80, -20, -10))
print ("max(0, 100, -400) : ", max(0, 100, -400))
以上实例运行后输出结果为：

max(80, 100, 1000) :  1000
max(-20, 100, 400) :  400
max(-80, -20, -10) :  -10
max(0, 100, -400) :  100
****************************************************************************************
round() 函数
描述：返回浮点数x的四舍五入值。
语法：round( x [, n]  )
参数：x -- 数值表达式。			n -- 数值表达式。
返回值：返回浮点数x的四舍五入值。
# 案例：
print ("round(70.23456) : ", round(70.23456))
print ("round(56.659,1) : ", round(56.659,1))
print ("round(80.264, 2) : ", round(80.264, 2))
print ("round(100.000056, 3) : ", round(100.000056, 3))
print ("round(-100.000056, 3) : ", round(-100.000056, 3))
以上实例运行后输出结果为：

round(70.23456) :  70
round(56.659,1) :  56.7
round(80.264, 2) :  80.26
round(100.000056, 3) :  100.0
round(-100.000056, 3) :  -100.0
**************************************************************************************
delattr() 函数
描述：delattr 函数用于删除属性。
	  delattr(x, 'foobar') 相等于 del x.foobar。
语法：delattr(object, name)
参数：object -- 对象。		name -- 必须是对象的属性。
返回值：无
# 案例：
class Coordinate:
    x = 10
    y = -5
    z = 0
 
point1 = Coordinate() 
 
print('x = ',point1.x)
print('y = ',point1.y)
print('z = ',point1.z)
 
delattr(Coordinate, 'z')
 
print('--删除 z 属性后--')
print('x = ',point1.x)
print('y = ',point1.y)
 
# 触发错误
print('z = ',point1.z)
*************************************************************************************
hash() 函数
描述：用于获取取一个对象（字符串或者数值等）的哈希值。
语法：hash(object)
参数：object -- 对象；
返回值：返回对象的哈希值。
# 案例：
>>>hash('test')            # 字符串
2314058222102390712
>>> hash(1)                 # 数字
1
>>> hash(str([1,2,3]))      # 集合
1335416675971793195
>>> hash(str(sorted({'1':1}))) # 字典
7666464346782421378
>>>
*************************************************************************************
memoryview() 函数
描述：返回给定参数的内存查看对象(Momory view)。
	  所谓内存查看对象，是指对支持缓冲区协议的数据进行包装，
	  在不需要复制对象基础上允许Python代码访问。
语法：memoryview(obj)
参数：obj -- 对象
返回值：返回元组列表。
# 案例：
Python2.x 应用：
>>>v = memoryview('abcefg')
>>> v[1]
'b'
>>> v[-1]
'g'
>>> v[1:4]
<memory at 0x77ab28>
>>> v[1:4].tobytes()
'bce'
Python3.x 应用：
>>>v = memoryview(bytearray("abcefg", 'utf-8'))
>>> print(v[1])
98
>>> print(v[-1])
103
>>> print(v[1:4])
<memory at 0x10f543a08>
>>> print(v[1:4].tobytes())
b'bce'
>>>
***************************************************************************************
set() 函数
描述：创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
语法：class set([iterable])
参数：iterable -- 可迭代对象对象；
返回值：返回新的集合对象
# 案例：
>>>x = set('runoob')
>>> y = set('google')
>>> x, y
(set(['b', 'r', 'u', 'o', 'n']), set(['e', 'o', 'g', 'l']))   # 重复的被删除
>>> x & y         # 交集
set(['o'])
>>> x | y         # 并集
set(['b', 'e', 'g', 'l', 'o', 'n', 'r', 'u'])
>>> x - y         # 差集
set(['r', 'b', 'u', 'n'])
>>>