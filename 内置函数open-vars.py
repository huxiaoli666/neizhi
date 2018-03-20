open() 函数
描述：python open() 函数用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写。
语法：open(name[, mode[, buffering]])
参数: name : 一个包含了你要访问的文件名称的字符串值。
	  mode : mode 决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。
	  		 这个参数是非强制的，默认文件访问模式为只读(r)。
	  buffering : 如果 buffering 的值被设为 0，就不会有寄存。
	  			  如果 buffering 的值取 1，访问文件时会寄存行。如果将 buffering 的值设为大于 1 的整数，
	  			  表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。
不同模式打开的文件列表
	r 		rb 		r+ 		rb+
	w 		wb 		w+ 		wb+
	a 		ab 		a+ 		ab+

file.read([size]) size未指定则返回整个文件,如果文件大小>2倍内存则有问题.f.read()读到文件尾时返回""(空字串)

file.readline() 返回一行

file.readlines([size]) 返回包含size行的列表,size 未指定则返回全部行

for line in f: print line #通过迭代器访问

f.write("hello\n") #如果要写入字符串以外的数据,先将他转换为字符串.

f.tell() 返回一个整数,表示当前文件指针的位置(就是到文件头的比特数).

f.seek(偏移量,[起始位置]) 用来移动文件指针.

偏移量:单位:比特,可正可负
起始位置:0-文件头,默认值;1-当前位置;2-文件尾
f.close() 关闭文件

# 案例：
>>>f = open('test.txt')
>>> f.read()
'RUNOOB1\nRUNOOB2\n'
**********************************************************************************************
str() 函数
描述：将对象转化为适于人阅读的形式。
语法：class str(object='')   参数：object -- 对象。
返回值：返回一个对象的string格式
# 案例：
>>>s = 'RUNOOB'
>>> str(s)
'RUNOOB'
>>> dict = {'runoob': 'runoob.com', 'google': 'google.com'};
>>> str(dict)
"{'google': 'google.com', 'runoob': 'runoob.com'}"
>>>
**********************************************************************************************
bool() 函数     是int的子类
描述：用于将给定参数转换为布尔类型，如果没有参数(0,1)，返回 False。
语法：class bool([x])   参数：x -- 要进行转换的参数。
返回值：返回 Ture 或 False。
# 案例：
>>>bool()
False
>>> bool(0)
False
>>> bool(1)
True
>>> bool(2)
True
>>> issubclass(bool, int)  # bool 是 int 子类
True
*******************************************************************************************
exec 函数
描述：执行储存在字符串或文件中的 Python 语句，相比于 eval，exec可以执行更复杂的 Python 代码。
语法：exec(object[, globals[, locals]])
参数：object：必选参数，表示需要被指定的Python代码。
	  globals：可选参数，表示全局命名空间（存放全局变量），如果被提供，则必须是一个字典对象。
	  locals：可选参数，表示当前局部命名空间（存放局部变量），如果被提供，可以是任何映射对象。
	  		  如果该参数被忽略，那么它将会取与globals相同的值。
返回值：exec 返回值永远为 None
# 案例：
x = 10
expr = """
z = 30
sum = x + y + z
print(sum)
"""
def func():
    y = 20
    exec(expr)
    exec(expr, {'x': 1, 'y': 2})
    exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})
    
func()
**************************************************************************************************
isinstance() 函数
描述：判断一个对象是否是一个已知的类型，类似 type()。
	isinstance() 与 type() 区别：
		type() 不会认为子类是一种父类类型，不考虑继承关系。
		isinstance() 会认为子类是一种父类类型，考虑继承关系。

如果要判断两个类型是否相同推荐使用 isinstance()。
语法：isinstance(object, classinfo)
参数：object -- 实例对象。
	  classinfo -- 可以是直接或间接类名、基本类型或者有它们组成的元组。
返回值：如果对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False。。
# 案例：
>>>a = 2
>>> isinstance (a,int)
True
>>> isinstance (a,str)
False
>>> isinstance (a,(str,int,list))    # 是元组中的一个返回 True
True

type() 与 isinstance()区别：
class A:
    pass
 
class B(A):
    pass
 
isinstance(A(), A)    # returns True
type(A()) == A        # returns True
isinstance(B(), A)    # returns True
type(B()) == A        # returns False   不会认为子类是一种父类类型，不考虑继承关系
******************************************************************************************
ord() 函数
描述：是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，
	  它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，
	  如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
语法：ord(c)   	参数：c -- 字符。
返回值:返回值是对应的十进制整数。
# 案例：
>>>ord('a')
97
>>> ord('b')
98
>>> ord('c')
99
*****************************************************************************************
sum() 函数 					求和
描述：对系列进行求和计算。
语法：sum(iterable[, start])   
参数：iterable -- 可迭代对象，如列表。
	  start -- 指定相加的参数，如果没有设置这个值，默认为0。
返回值：返回计算结果。
# 案例：
>>>sum([0,1,2])  
3  
>>> sum((2, 3, 4), 1)        # 元组计算总和后再加 1
10
>>> sum([0,1,2,3,4], 2)      # 列表计算总和后再加 2
12
****************************************************************************************
bytearray() 函数
描述：返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。
语法：class bytearray([source[, encoding[, errors]]])
参数：如果 source 为整数，则返回一个长度为 source 的初始化数组；
	  如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
	  如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
	  如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
	  如果没有输入任何参数，默认就是初始化数组为0个元素。
返回值：返回新字节数组。
# 案例：
>>>bytearray()
bytearray(b'')
>>> bytearray([1,2,3])
bytearray(b'\x01\x02\x03')
>>> bytearray('runoob', 'utf-8')
bytearray(b'runoob')
>>>
*********************************************************************************************
filter() 函数     过滤
描述：filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
	  该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，
	  然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
语法：filter(function, iterable)
参数：function -- 判断函数。
	  iterable -- 可迭代对象。
返回值：返回列表。
# 案例：
##过滤出1~100中平方根是整数的数：
import math
def is_sqr(x):
    return math.sqrt(x) % 1 == 0
 
newlist = filter(is_sqr, range(1, 101))
print(newlist)
*********************************************************************************************
issubclass() 函数      
描述：判断参数 class 是否是类型参数 classinfo 的子类。
语法：issubclass(class, classinfo)
参数：class -- 类。     classinfo -- 类。
返回值：如果 class 是 classinfo 的子类返回 True，否则返回 False。
# 案例：
class A:
    pass
class B(A):
    pass
    
print(issubclass(B,A))    # 返回 True
********************************************************************************************
pow() 函数      	幂
描述：返回 x**y（x的y次方） 的值。
语法：import math  
	  math.pow( x, y )
	  # 内置的 pow() 方法
	  pow(x, y[, z])
参数：x -- 数值表达式。
	  y -- 数值表达式。
	  z -- 数值表达式。
返回值：返回 xy（x的y次方） 的值。
# 案例：
import math   # 导入 math 模块

print ("math.pow(100, 2) : ", math.pow(100, 2))
# 使用内置，查看输出结果区别
print ("pow(100, 2) : ", pow(100, 2))
print ("math.pow(100, -2) : ", math.pow(100, -2))
print ("math.pow(2, 4) : ", math.pow(2, 4))
print ("math.pow(3, 0) : ", math.pow(3, 0))
********************************************************************************************
super() 函数
描述：super() 函数是用于调用父类(超类)的一个方法。
super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，
	  但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。
语法：super(type[, object-or-type])
参数：type -- 类。
	  object-or-type -- 类，一般是 self
Python3.x 和 Python2.x 的一个区别是: 
	Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx :
# 案例：
class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print ('Parent')
    
    def bar(self,message):
        print ("%s from Parent" % message)
 
class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
        super(FooChild,self).__init__()    
        print ('Child')
        
    def bar(self,message):
        super(FooChild, self).bar(message)
        print ('Child bar fuction')
        print (self.parent)
 
if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')
************************************************************************************************
bytes 函数
描述：返回一个新的 bytes 对象，该对象是一个 0 <= x < 256 区间内的整数不可变序列。
	  它是 bytearray 的不可变版本
语法：class bytes([source[, encoding[, errors]]])
参数：如果 source 为整数，则返回一个长度为 source 的初始化数组；
	  如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
	  如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
	  如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
	  如果没有输入任何参数，默认就是初始化数组为0个元素。
返回值：返回一个新的 bytes 对象。
# 案例：
>>>a = bytes([1,2,3,4])
>>> a
b'\x01\x02\x03\x04'
>>> type(a)
<class 'bytes'>
>>>
>>> a = bytes('hello','ascii')
>>>
>>> a
b'hello'
>>> type(a)
<class 'bytes'>
>>>
************************************************************************************
float() 函数
描述：用于将整数和字符串转换成浮点数。
语法：class float([x])
参数：x -- 整数或字符串
返回值：返回浮点数
案例：>>>float(1)
1.0
>>> float(112)
112.0
>>> float(-123.6)
-123.6
>>> float('123')     # 字符串
123.0
************************************************************************************
iter() 函数      
描述：用来生成迭代器
语法：iter(object[, sentinel])
参数：object -- 支持迭代的集合对象。
	  sentinel -- 如果传递了第二个参数，则参数 object 必须是一个可调用的对象（如，函数），
	  			  此时，iter 创建了一个迭代器对象，每次调用这个迭代器对象的__next__()方法时，
	  			  都会调用 object。
返回值：迭代器对象。
# 案例：
>>>lst = [1, 2, 3]
>>> for i in iter(lst):
...     print(i)
... 
1
2
3
***********************************************************************************
print() 函数
描述：用于打印输出，最常见的一个函数。
语法：print(*objects, sep=' ', end='\n', file=sys.stdout)
参数：objects -- 复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。
	  sep -- 用来间隔多个对象，默认值是一个空格。
	  end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串。
	  file -- 要写入的文件对象。
返回值：无
# 案例：
Python3 下测试
>>>print(1)  
1  
>>> print("Hello World")  
Hello World  
 
>>> a = 1
>>> b = 'runoob'
>>> print(a,b)
1 runoob
 
>>> print("aaa""bbb")
aaabbb
>>> print("aaa","bbb")
aaa bbb
>>> 
 
>>> print("www","runoob","com",sep=".")  # 设置间隔符
www.runoob.com
*******************************************************************************************
tuple 函数
描述：将列表转换为元组。。
语法：tuple( seq )   		参数：seq -- 要转换为元组的序列。
返回值：返回元组。
# 案例：
>>>list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
>>> tuple1=tuple(list1)
>>> tuple1
('Google', 'Taobao', 'Runoob', 'Baidu')
*****************************************************************************************
callable() 函数
描述：用于检查一个对象是否是可调用的。如果返回True，object仍然可能调用失败；
	  但如果返回False，调用对象ojbect绝对不会成功。

对于函数, 方法, lambda 函数, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。
语法：callable(object)
参数：object -- 对象
返回值：可调用返回 True，否则返回 False
# 案例：
>>>callable(0)
False
>>> callable("runoob")
False
 
>>> def add(a, b):
...     return a + b
... 
>>> callable(add)             # 函数返回 True
True
>>> class A:                  # 类
...     def method(self):
...             return 0
... 
>>> callable(A)               # 类返回 True
True
>>> a = A()
>>> callable(a)               # 没有实现 __call__, 返回 False
False
>>> class B:
...     def __call__(self):
...             return 0
... 
>>> callable(B)
True
>>> b = B()
>>> callable(b)               # 实现 __call__, 返回 True
True
*****************************************************************************************
format 格式化函数
描述：Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。

语法：是通过 {} 和 : 来代替以前的 % 。

format 函数可以接受不限个参数，位置可以不按顺序。
*****************************************************************************************
len()方法
描述：返回对象（字符、列表、元组等）长度或项目个数。
语法：len( s )   参数：s -- 对象。
返回值：返回对象长度。
# 案例：
>>>str = "runoob"
>>> len(str)             # 字符串长度
6
>>> l = [1,2,3,4,5]
>>> len(l)               # 列表元素个数
5
*****************************************************************************************
property() 函数
描述：是在新式类中返回属性值。
语法：class property([fget[, fset[, fdel[, doc]]]])
参数：fget -- 获取属性值的函数
	  fset -- 设置属性值的函数
	  fdel -- 删除属性值函数
	  doc -- 属性描述信息
返回值：返回新式类属性。
# 案例：
定义一个可控属性值 x
class C(object):
    def __init__(self):
        self._x = None
 
    def getx(self):
        return self._x
 
    def setx(self, value):
        self._x = value
 
    def delx(self):
        del self._x
 
    x = property(getx, setx, delx, "I'm the 'x' property.")


将 property 函数用作装饰器可以很方便的创建只读属性：

class Parrot(object):
    def __init__(self):
        self._voltage = 100000
 
    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage


property 的 getter,setter 和 deleter 方法同样可以用作装饰器：

class C(object):
    def __init__(self):
        self._x = None
 
    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x
 
    @x.setter
    def x(self, value):
        self._x = value
 
    @x.deleter
    def x(self):
        del self._x
*************************************************************************************
type() 函数
描述:如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象。
语法:class type(name, bases, dict)
参数：name -- 类的名称。
	  bases -- 基类的元组。
	  dict -- 字典，类内定义的命名空间变量。
返回值：一个参数返回对象类型, 三个参数，返回新的类型对象。
# 案例：
# 一个参数实例
>>> type(1)
<type 'int'>
>>> type('runoob')
<type 'str'>
>>> type([2])
<type 'list'>
>>> type({0:'zero'})
<type 'dict'>
>>> x = 1          
>>> type( x ) == int    # 判断类型是否相等
True
 
# 三个参数
>>> class X(object):
...     a = 1
...
>>> X = type('X', (object,), dict(a=1))  # 产生一个新的类型 X
>>> X
<class '__main__.X'>
***************************************************************************************
chr() 函数
描述：用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
语法：chr(i)
参数：i -- 可以是10进制也可以是16进制的形式的数字。
返回值：返回值是当前整数对应的ascii字符。
# 案例：
>>>print chr(0x30), chr(0x31), chr(0x61)   # 十六进制
0 1 a
>>> print chr(48), chr(49), chr(97)         # 十进制
0 1 a
**************************************************************************************
frozenset() 函数
描述：返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
语法：class frozenset([iterable])
参数：iterable -- 可迭代的对象，比如列表、字典、元组等等。
返回值：返回新的 frozenset 对象，如果不提供任何参数，默认会生成空集合。
# 案例：
>>>a = frozenset(range(10))     # 生成一个新的不可变集合
>>> a
frozenset([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> b = frozenset('runoob') 
>>> b
frozenset(['b', 'r', 'u', 'o', 'n'])   # 创建不可变集合
>>>
*************************************************************************************
list()方法
描述：用于将元组转换为列表。
语法：list( seq )
参数：list -- 要转换为列表的元组
返回值：返回列表。
# 案例：
aTuple = (123, 'Google', 'Runoob', 'Taobao')
list1 = list(aTuple)
print ("列表元素 : ", list1)

str="Hello World"
list2=list(str)
print ("列表元素 : ", list2)
输出结果：
列表元素 :  [123, 'Google', 'Runoob', 'Taobao']
列表元素 :  ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
*************************************************************************************
range() 函数用法
描述：Python3 range() 函数返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表。
	  Python3 list() 函数是对象迭代器，可以把range()返回的可迭代对象转为一个列表，返回的变量类型为列表。
	  Python2 range() 函数返回的是列表。
语法：range(stop)
	  range(start, stop[, step])
参数：start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
	  stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
	  step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
返回值：无
# 案例：
>>>range(5)
range(0, 5)
>>> for i in range(5):
...     print(i)
... 
0
1
2
3
4
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list(range(0))
[]
>>>

>>>range(5)
range(0, 5)
>>> for i in range(5):
...     print(i)
... 
0
1
2
3
4
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list(range(0))
[]
>>>
*****************************************************************************************
vars() 函数
描述：返回对象object的属性和属性值的字典对象。
语法：vars([object])
参数：object -- 对象
返回值：返回对象object的属性和属性值的字典对象，
	    如果没有参数，就打印当前调用位置的属性和属性值 类似 locals()。
# 案例：
>>>print(vars())
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> class Runoob:
...     a = 1
... 
>>> print(vars(Runoob))
{'a': 1, '__module__': '__main__', '__doc__': None}
>>> runoob = Runoob()
>>> print(vars(runoob))
{}
*******************************************************************************************
