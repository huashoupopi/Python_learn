# python

## python的输出

### 格式化输出

print()方法用于打印输出，是python常用的一个函数

该函数的语法如下

`print(*objects,sep='',end='\n',files=sys.stdout)`

- objects --表示输出的对象。输出多个对象时，需要用 , （逗号）分隔。

- sep -- 用来间隔多个对象。

- end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符。

- file -- 要写入的文件对象。

```python

print("www", "snh48", "com", sep=".")  # 设置间隔符
'''
运行结果如下：
www.snh48.com

```

在C语言中，我们可以使用printf("%-.4f",a)之类的形式，实现数据的的格式化输出。

python

```python
s = "imut666"
x=len(s)
print("The length of %s is %d" %(s,x))
"""
The length of Duan Yixuan is 11
"""
```

```py
PI=3.1415926
print('%010.3f'%PI) #字段宽度为10，精度为3，不足处用0填充空白
#000003.142   0表示转换值若位数不够则用0填充
```

```python
for x in range(0, 5):
    print(x, end=' ')
#0 1 2 3 4 
```

### format的用法

format()功能很强大，他把字符串当作一个模板，通过传入的参数进行格式化，并且使用"{}"作为特殊字符取代'%'

使用方法有两种：b.format(a)和format(a,b)。

#### 基本用法

1. 不带编号,即"{}"
2. 带数字编号，可调换顺序，即"{1}","{2}"
3. 带关键字，即"{a}","{tom}"

```python
print("{} {}".format("imut","666"))
print("{0} {1}".format("imut","666"))
print("{0} {1} {0}".format("imut","666"))
print('{a} {b} {a}'.format(a='imut',b='666'))  # 带关键字
"""
imut 666
imut 666
imut 666 imut
imut 666 imut
"""
```

####  进阶用法

1. < （默认）左对齐、> 右对齐、^ 中间对齐、= （只用于数字）在小数点后进行补齐
2. 取位数“{:4s}”、"{:.2f}"等

```python
print("{:10s} and {:>10s}".format("imut","666")) 		#取10位左对齐 10位右对齐
print("{:^10s} and {:^10s}".format("imut","666"))		#取10位中间对齐
print("{} is {:.2f}".format(1.123,1.123))			    #取2位小数
"""
imut       and        666
   imut    and    666    
1.123 is 1.12
"""
print("{0} is {0:>10.2f}".format(1.123))	#取2位小数，右对齐，取10位
"""
"""
```

```python
'b' - 二进制。将数字以2为基数进行输出。
>>> print('{0:b}'.format(3))
11

'c' - 字符。在打印之前将整数转换成对应的Unicode字符串。
>>> print('{:c}'.format(20))
4

'd' - 十进制整数。将数字以10为基数进行输出。
>>> print('{:d}'.format(20))
20

'o' - 八进制。将数字以8为基数进行输出。
>>> print('{:o}'.format(20))
24

'x' - 十六进制。将数字以16为基数进行输出，9以上的位数用小写字母。
>>> print('{:x}'.format(20))
14

'e' - 幂符号。用科学计数法打印数字。用'e'表示幂。
>>> print('{:e}'.format(20))
2.000000e+01

'g' - 一般格式。将数值以fixed-point格式输出。当数值特别大的时候，用幂形式打印。
>>> print('{:g}'.format(20.1))
20.1

'n' - 数字。当值为整数时和'd'相同，值为浮点数时和'g'相同。不同的是它会根据区域设置插入数字分隔符。
>>> print('{:f}'.format(20))
20.000000
>>> print('{:n}'.format(20))
20

'%' - 百分数。将数值乘以100然后以fixed-point('f')格式打印，值后面会有一个百分号。

>>> print('{:%}'.format(20))
2000.000000%
```

可在字符串前加f以达到格式化的目的，在{}里加入对象，此为format的另一种形式：

```python
name  = "imut"
age = 20
sex = "man"
job = "IT"
salary = 9999.99
print(f"ma name is {name.capitalize()}")
print(f"I am {age:*^10} years old.")
print(f"I am a {sex}")
print(f"My salary is {salary:10.3f}")
"""
ma name is Imut
I am ****20**** years old.
I am a man
My salary is   9999.990
"""
```

### 字符串

#### 字符串方法

```python
str = "Hello world!"		
len(str1)		# 通过内置函数len计算字符串的长度
str.capitalize()	#获得字符串首字母大写的拷贝
str.title()         #获得字符串每个单词首字母大写的拷贝
str.upper()			#获得字符串变大写后的拷贝
str.center(50,"*")   #将字符串以指定的宽度居中 并在两侧填充指定的字符
str.rjust(50,'') 	 #将字符串以指定的宽度靠右放置左侧填充指定的字符
str.strip()			#获得字符串修剪左右两侧空格之后的拷贝
```

### 列表操作

- 查找某元素的下标 ：如果找不到，报错ValueError

语法：`列表.index(元素)`

- 插入元素

语法:`列表.insert(下标，元素)`，在指定下标的位置，插入指定的元素 前插

```python
list = [1,3,4]
list.insert(1,2)
print(list)
"""
[1,2,3,4]
"""
```

- 尾插元素

语法：`列表.append(元素)将指定元素 追加到列表的尾部`

- 追加元素方法2

语法：`列表.extend(其他数据元素) 将其他数据容器的内容取出 依次追加到列表尾部`

```python
list = [1,3,4]
list.insert(1,2)
print(f"插入元素后列表变成{list}")
list.append(3)
list.append([4,5,6])
print(f"尾插后的列表变为{list}")
"""
插入元素后列表变成[1, 2, 3, 4]
尾插后的列表变为[1, 2, 3, 4, 3, [4, 5, 6]]
"""
list_2=[1,2,3]
list_2.extend([4,5,6])
print(list_2)
"""
[1, 2, 3, 4, 5, 6]
"""
```

- 删除元素

  - 语法1：del列表[下标]
  - 语法2：列表.pop(下标) 返回被删除的元素

  - 语法3：列表.remove(元素)

  ```python
  list = [1,2,3,2,3]
  list.remove(2)
  print(list)
  """
  [1,3,2,3]
  """
  ```

  - 清空列表

  语法：列表.clear()

  - 统计元素在列表内的数量

  语法：列表.count(元素)

  ```python
  list = [1,1,1,2,3]
  print(list.count(1)) # 3
  ```

  #### 获取列表长度

  语法：len(列表)

  #### 补充

  ```python
  for index,elem in enumerate(list1):
      print(index,elem)
  #通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
  ```
  
  #### 列表的排序操作
  
  ```python
  list1 = ['orange','apple','zoo','internationalization','blueberry']
  list2 = sorted(list1)
  """
  sorted 函数返回列表排序后的拷贝，而不是修改传入的列表
  """
  list3 = sorted(list1, reverse=True)
  # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
  list4 = sorted(list1, key=len)
  print(list1)
  print(list2)
  print(list3)
  print(list4)
  # 给列表对象发出排序消息直接在列表对象上进行排序
  list1.sort(reverse=True)
  print(list1)
  ```
  
   列表.sort(key = 选择排序依据的函数，reverse=True|False)
  
  ### 元组
  
  <mark>元组一旦定义完成就不可修改</mark>
  
  - 定义空元组
  
    `变量名称 = tuple()`
  
  元组内只有一个元素时要加逗号  不然类型就不是元组了
  
  #### 方法或函数
  
  1. index():查找某个元素，如果数据存在则返回对应的下标 否则报错
  2. count(): 统计某个数据在当前元组出现的次数
  3. len(元组)：统计元组内元素的个数
  
  ### 字符串
  
  字符串也可以使用下标操作
  
  <mark>同元组一样，字符串是一个无法修改的数据容器</mark>
  
  #### 方法和函数
  
  - 查找指定字符串的下标索引值
  
  语法：字符串.index(字符串)
  
  ```python
  str = "imut xinxi 666"
  print(str.index("xinxi")) #5
  ```
  
  - 字符串的替换：
  
  语法：字符串.replace(字符串1，字符串2)
  
  功能：将字符串内的全部：字符串1 替换为 字符串2
  
  注意：不是修改字符串本身 而是得到了一个新的字符串

```python
str = "imut xinxi 666"
new_str = str.replace("i","66")
print(f"字符串{str}替换后为{new_str}")
"""
字符串imut xinxi 666替换后为66mut x66nx66 666
"""
```

- 字符串的分割

  - 语法：字符串.split()
  - 功能：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
  - 注意：字符串本身不变，而是得到了一个列表对象

  ```python
  str = "Hello python imut IT"
  list = str.split(" ")
  print(f"将字符串{str}进行分割后得到:{list} 类型是{type(list)}")
  """
  将字符串Hello python imut IT进行分割后得到:['Hello', 'python', 'imut', 'IT'] 类型是<class 'list'>
  """
  ```

  - 字符串的规整操作

    - 去掉前后空格 语法：字符串.strip()

    ```python
    str = "   imut 666 xinxi   "
    print(str.strip())   #结果："imut 666 xinxi"
    ```

    - 取出前后指定字符串 语法：字符串.strip(字符串)

    ```python
    str = "12imut 666 xinxi21"
    print(str.strip("12"))
    """
    注意，传入的是"12" 其实就是"1" 和 "2" 都会移除 是按照单个字符
    结果： "imut 666 xinxi"
    """
    ```

- 统计字符串中某字符出现的次数 

语法：count = str.count("字符串")

- 统计字符串的长度

语法: num = len(str)

### 序列和切片

<mark>对序列进行切片操作并不会影响到序列本身，而是会得到一个新的序列</mark>

[起始:结尾(不包括):步长]

```python
list = [1,2,3,4,5]
result = list[:4]
print(result)

str = "imut 666 xinxi"
result = str[::-1][6:9]
print(f"结果{result}")

```

### 集合

不支持元素的重复，并且内容无序

#### 集合的定义

- {}
- 变量名称 = {元素，元素，元素}
- 定义空集合： 变量名称 = set()

#### 集合的常用操作

- 修改：集合是无序的所以不支持下标索引访问但是可以修改
  - 添加新元素 语法：集合.add(元素)
  - 移除元素 语法：集合.remove(元素) 将指定元素从集合内移除
  - 随机取出一个元素  语法：集合.pop() 功能，从集合中随机取出一个元素 会得到一个元素的结果 同时集合本身被修改，元素被移除
  - 集合清空 语法：集合.clear()  功能：集合清空
  - 取两个集合的差集 语法：集合1.difference(集合2), 功能：取出集合1和集合2的差集(集合1有集合2没有的) 结果：得到一个新集合，集合1和集合2不变
  - 消除差集： 语法：集合1.difference_update(集合2) 功能：对比集合1和集合2，在集合1内，删除和集合2相同的元素 结果：集合1被修改，集合2不变
  - 两个集合合并： 语法：集合1.union(集合2) 功能：将集合1和集合2组合成新集合 结果：得到新集合，集合1和集合2不变
  - 集合长度 len(集合)

```python
# set = {num for num in range(1,100) if num%3 == 0 or num%5 == 0}
# print(set)
set = {1,3,2}
set.add(4)
set.add(5)
print(set)
set.update([11,12])
print(set)
set.discard(5)
print(set)
"""
{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5, 11, 12}
{1, 2, 3, 4, 11, 12}
"""
```

```python
# 集合的交集、并集、差集、对称差运算
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))
```



### 字典

#### 字典的常用操作

- 新增元素 语法：字典[key] = Value 结果：字典被修改，新增了元素

- 更新元素 语法：字典[key] = Value 结果：字典被修改，元素被更新

  <mark>字典key不可以重复 随意对已存在的Key值执行上述操作 就是更新Value值</mark>

- 删除元素 语法：字典.pop(Key) 结果：获得指定Key的Value 同时字典被修改 指定Key的数据被删除

- 清除 语法：字典.clear()  

- 获取全部的Key 语法：字典.keys() 结果：得到字典中的全部Key

```python
# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('麦当当', 100))
```

#### 遍历字典

```python
dict ={"许善强":18,
       "麦当当":20,
       "刘备": 20,
       "张飞":28
       }
for key in dict:
    print(f"键值为{key} value为{dict[key]}")
key_2 = dict.keys()
for key in key_2:
    print(f"键为{key} value为{dict[key]}")
   
for key,value in dict.items():
    print(f"{key} {value}")
    
for key in dict.keys():
    print(f"{key}")

for value in dict.values():
    print(f"{value}")
```

### 容器的一些通用操作

- max()
- min()
- len()

#### 通用转换功能

- list(容器) ：将给定容器转换为列表
- str(容器)：将给定容器转换为字符串
- tuple(容器)：将给定容器转换为元组
- set(容器)：将给定容器转换为集合

#### 通用排序功能

sorted(容器,（加上后面这句会反向）[reverse=True])  将给定容器进行排序 默认从小到大

<mark>排完序的结果都变成了列表对象</mark>



### 函数

#### 多个返回值

```python
def  test_retuen:
    return 1,2
x, y = test_return()
print(x)	#结果1
print(y)	#结果2
```

#### 函数参数类型

- 位置参数

- 关键字参数

- 缺省参数：缺省参数也叫默认参数

- 不定长参数：也叫可变参数，用于不确定调用的时候会传递多少个参数(不传参也可以)的场景， 作用：当调用函数时不确定参数个数时，可以使用不定长参数

  - 位置传递的不定长参数

  ```python
  def user_info(*args):
      print(args)
      
  # ("TOM",)
  user_info("TOM")
  # ("TOM",18)
  user_info("TOM",18)
  ```

  <mark>传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组(tuple),args是元组类型，这就是位置传递</mark>

  - 关键字传递的不定长参数

```python
def user_info(**kwargs):
    print(kwargs)
#{"name":"TOM","age":18,"id":110}
user_info(name = "TOM",age = 18,id = 110)
```

<mark>参数是"键=值"形式的形式的情况下，所有的"键=值"都会被kwargs接受，同时会根据"键=值"组成字典</mark>

#### 匿名函数

##### 函数作为参数传递

```python
def test_func(compute):
    result = compute(1,2)
    print(result)
    
def compute(x,y):
    return x+y
```

##### lambda匿名函数

函数的定义中：

- def关键字，可以定义**带有名称**的函数
- lambda关键字，可以定义匿名函数(无名称)

有名称的函数，可以基于名称**重复使用**。

无名称的匿名函数，只可**临时使用一次**

匿名函数定义语法：

lambda 传入参数:函数体(一行代码)

- lambda是关键字，表示定义匿名函数
- 传入参数表示匿名函数的形式参数，如:x,y表示接受2个形式参数
- 函数体，就是函数的执行逻辑，要注意:只能写一行，无法写多行代码

```python
def test_func(compute):
    result = compute(1,2)
    print(result)
    
test_func(lambda x,y:x+y)  #结果：3
#使用def和lambda，定义的函数功能完全一致，只是lambda观念子定义的函数是匿名的，无法二次使用
def test_func(compute):
    result = compute(1,4)
    print(result)

test_func(lambda x,y:x+y)

func_a = lambda x,y:x*y
print(func_a(2,2))
```

### 生成器

```python
def counter():
    i = 0
    while i <= 5:
        yield i
        i += 1

for i in counter():
    print(i)

c = counter()
for i in range(6):
    print(next(c))
```

## 文件

打开、关闭、读、写

### open打开文件

可以打开一个文件，或者创建一个新文件，语法如下

`open(name,mode,encoding)`

- name:是要打开的目标文件名的字符串(可以包含文件所在的具体路径)
- mode:设置打开文件的模式：只读、写入、追加
- encoding:编码格式(推荐使用UTF-8)  encoding顺序不是第三位 所以要用关键字参数直接指定

| 访问模式 |                             说明                             |
| :------: | :----------------------------------------------------------: |
|    r     | 以只读的方式打开文件。文件的指针将会放在文件的开头。如果文件不存在则报错。**这是默认模式** |
|    w     | 打开一个文件只用于写入，如果该文件存在则将其覆盖。如果文件不存在，创建新文件 |
|    a     | 打开一个文件用于追加，如果该文件已存在，文件指针将会放在文件的结尾。如果文件不存在，创建新文件写入 |
|    r+    |      打开⼀个⽂件⽤于读写。⽂件指针将会放在⽂件的开头。      |
|    w+    | 打开⼀个⽂件⽤于读写。如果该⽂件已存在则打开⽂件，并从开头开始编辑，即原有内容会被删除。如果该⽂件不存在，创建新⽂件。 |
|    a+    | 打开⼀个⽂件⽤于读写。如果该⽂件已存在，⽂件指针将会放在⽂件的结尾。⽂件打开时会是追加模式。如果该⽂件不存在，创建新⽂件⽤于读写。 |
|    rb    | 以⼆进制格式打开⼀个⽂件⽤于只读。⽂件指针将会放在⽂件的开头。 |
|    wb    | 以⼆进制格式打开⼀个⽂件只⽤于写⼊。如果该⽂件已存在则打开⽂件，并从开头开始编辑，即原有内容会被删除。如果该⽂件不存在，创建新⽂件。 |
|    ab    | 以⼆进制格式打开⼀个⽂件⽤于追加。如果该⽂件已存在，⽂件指针将会放在⽂件的结尾。也就是说，新的内容将会被写⼊到已有内容之后。如果该⽂件不存在，创建新⽂件进⾏写⼊。 |
|   rb+    | 以⼆进制格式打开⼀个⽂件⽤于读写。⽂件指针将会放在⽂件的开头。 |
|   wb+    | 以⼆进制格式打开⼀个⽂件⽤于读写。如果该⽂件已存在则打开⽂件，并从开头开始编辑，即原有内容会被删除。如果该⽂件不存在，创建新⽂件。 |
|   ab+    | ⼆进制格式打开⼀个⽂件⽤于追加。如果该⽂件已存在，⽂件指针将会放在⽂件的结尾。如果该⽂件不存在，创建新⽂件⽤于读写。 |

```python
fp = open("test.txt","r")
#默认情况下 read是一个字节一个字节的读效率比较低
content = fp.read()
print(content)
#readline()是一行一行的读但只能读一行
content = fp.readline()
print(content)
#readlines()是按照行来读取，但是会将所有数据都读到，并且以一个列表的形式返回
#而列表的元素是一行一行的数据
content = fp.readlines()
print(content) 
```

### for循环读取文件行

```python
for line in open("python.txt","r"):
    print(line)
```

### 文件关闭操作

- close()关闭文件对象
- 关闭对文件的占用 如果不调用close()， 同时程序没有停止运行，那么这个文件将一直被Python程序占用

### with open语法

```python
with open("python.txt","r") as f:
    f.readlines()
```

- 可以在操作完成后自动close文件 避免忘记close

### 文件的写入

```python
with open("test.txt","w") as f:
    f.write("hello world")
   #f.flush()    内容刷新
```

- 直接调用write()，内容并未真正写入文件，而是会积攒在程序的内存中，称之为缓冲区
- 当调用flush()的时候，内容会真正写入文件
- 这样做是为了避免频繁的操作硬盘，导致效率下降(攒一堆没一次性写磁盘)



## 异常模块 包

#### assert

`assert`是Python中的一个关键字，用于判断一个条件是否成立，如果不成立则会抛出`AssertionError`异常。其语法格式为：

`assert expression [, arguments]`

其中`expression`是一个要被判断的条件，如果`expression`为`True`，那么程序将继续执行；否则，程序将抛出`AssertionError`异常。

`arguments`是一个可选参数，通常是一个字符串，用于在抛出异常时提示信息。

`assert`语句通常用于调试和测试，用于检查代码中的某个条件是否满足。如果该条件不满足，那么程序的行为可能是不可预测的，因此在开发和测试过程中使用`assert`语句可以提高程序的健壮性和可靠性。

```python
def divide(x, y):
    assert y != 0, "division by zero"
    return x / y
```

上述代码中，`assert y != 0`用于判断分母`y`是否为0，如果为0则抛出异常并提示"division by zero"。这样可以避免程序因为分母为0而导致异常或错误的发生

### 捕获异常

```python
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
```

### 捕获指定异常

```python
try:
    print(name)
except NameError as e:
    print("name变量名称维持定义错误")
    #可以print(e)
```

### 捕获多个异常

当捕获多个异常时，可以把要捕获的异常类型的名字，放到except后，并使用元组的方式进行书写

```python
try:
    print(1/0)
except(NameError,ZeroDivisionError):
    print("ZeroDivision错误...")
```

### 捕获所有异常

```python
try:
    print(name)
except Exception as e:
    print("出现异常了")
```

### 异常的else和finally语法

```python
try:
    print(1)
except Exception as e:
    print(e)
else:
    print("我是else，是没有异常的时候执行的代码")
```

finally表示的是无论是否异常都要执行的代码，例如关闭文件

```python
try:
    f = open("test.txt","r")
except Exception as e:
    f = open("test.txt","w")
else:
    print("很开心没有异常")
finally:
    f.close()
```

### 异常的传递

异常是具有传递性的

当函数func01中发生异常，并且没有捕获处理这个异常的时候，异常会传递到函数func02，当func02也没有捕获这个异常的时候，main函数就会捕获这个异常，这就是异常的传递性

<mark>当所有函数都没有被捕获异常的时候，程序就会报错</mark>

```python
def func01():
    print("这是func01的开始")
    num = 1/0
    print("这是func01结束")
    
def func02():
    print("这是func02开始")
    func01()
    print("这是func02结束")
    
def main():
    try:
        func02()
    except Exception as e:
        print(e)
```

### raise的用法

raise 语句的基本语法格式为：

`raise [exceptionName [(reason)]]`

其中，用 [] 括起来的为可选参数，其作用是指定抛出的异常名称，以及异常信息的相关描述。如果可选参数全部省略，则 raise 会把当前错误原样抛出；如果仅省略 (reason)，则在抛出异常时，将不附带任何的异常描述信息。

也就是说，raise 语句有如下三种常用的用法：

1. raise：单独一个 raise。该语句引发当前上下文中捕获的异常（比如在 except 块中），或默认引发 RuntimeError 异常。
2. raise 异常类名称：raise 后带一个异常类名称，表示引发执行类型的异常。
3. raise 异常类名称(描述信息)：在引发指定类型的异常的同时，附带异常的描述信息。

```python
try:
    a = input()
    if(not a.isdigit()):
        raise ValueError("a必须是数字")
except ValueError as e:
    print("引发异常",e)
    """
    i
引发异常 a必须是数字
    """
```

可以看到，当用户输入的不是数字时，程序会进入 if 判断语句，并执行 raise 引发 ValueError 异常。但由于其位于 try 块中，因为 raise 抛出的异常会被 try 捕获，并由 except 块进行处理。

因此，虽然程序中使用了 raise 语句引发异常，但程序的执行是正常的，手动抛出的异常并不会导致程序崩溃。

```python
try:
    a = input("输入一个数：")
    if(not a.isdigit()):
        raise ValueError("a 必须是数字")
except ValueError as e:
    print("引发异常：",repr(e))
    raise
"""
输入一个数：i
引发异常： ValueError('a 必须是数字')
Traceback (most recent call last):
  File "f:/py/project/demo4/lianxi3.py", line 10, in <module>
    raise ValueError("a 必须是数字")
ValueError: a 必须是数字
"""
```

这里重点关注位于 except 块中的 raise，由于在其之前我们已经手动引发了 ValueError 异常，因此这里当再使用 raise 语句时，它会再次引发一次。

当在没有引发过异常的程序使用无参的 raise 语句时，它默认引发的是 RuntimeError 异常。例如：

```python
try:
    a = input("输入一个数：")
    if(not a.isdigit()):
        raise
except RuntimeError as e:
    print("引发异常：",repr(e))
"""
输入一个数：a
引发异常： RuntimeError('No active exception to reraise',)
"""
```



### 模块

模块的导入方式

`[from 模块名] import [模块|类|变量|函数|*] [as 别名]`

```python
import time
print("你好")
time.sleep(5)
peint("你好")

from time import sleep
print("你好")
sleep(5)
print("你好")

from time import *
print("nihao")
sleep(5)
print("nihao")
```

### 自定义模块

`__main__变量`：......导入时不会执行测试部分

`__all__变量`：

![py1](/home/lcx/Documents/markdown/工具学习/py1.png)

### 文件的序列化和反序列化

如果是一个对象**列如列表、元组、字典等**，就无法直接写入到文件中，需要进行序列化
<mark>python中提供了JSON模块实现序列化和反序列化</mark>

#### 序列化的两种方式

- dumps()

```python
import json
fp = open("test.txt","w")
list_1 = ["zhangsan","lisi"]
name = json.dumps(list_1)
fp.write(name)
fp.close()
```

- dump()

```python
import json
fp = open("test.txt","w")
list_1 = ["zhangsan","lisi"]
json.dump(list_1,fp)
'''
相当于
name = json.dumps(list_1)
fp.write(name)
这两步
'''
fp.close()
```

#### 反序列化两种方法load loads()

- loads()

``` python
import json
fp = open("test.txt","r")
content = fp.read()
result = json.loads(content)
print(result)
print(type(result))
fp.close()
```

- load()

```python
import json
fp = open("test.txt","r")
result = json.load(fp)
fp.close()
```

- 中文的json

```python
import json
data = [{"name":"张大山","age":11},{"name":"王大锤","age":12},{"name":"赵小虎","age":16}]
json_str = json.dumps(data,ensure_ascii=False)
print(json_str)
"""
[{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 12}, {"name": "赵小虎", "age": 16}]
"""
```

### JSON进阶

Python的`dict`对象可以直接序列化为JSON的`{}`，不过，很多时候，我们更喜欢用`class`表示对象，比如定义`Student`类，然后序列化：

```plain
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s))
```



运行代码，毫不留情地得到一个`TypeError`：

```plain
Traceback (most recent call last):
  ...
TypeError: <__main__.Student object at 0x10603cc50> is not JSON serializable
```



错误的原因是`Student`对象不是一个可序列化为JSON的对象。

如果连`class`的实例对象都无法序列化为JSON，这肯定不合理！

别急，我们仔细看看`dumps()`方法的参数列表，可以发现，除了第一个必须的`obj`参数外，`dumps()`方法还提供了一大堆的可选参数：

https://docs.python.org/3/library/json.html#json.dumps

这些可选参数就是让我们来定制JSON序列化。前面的代码之所以无法把`Student`类实例序列化为JSON，是因为默认情况下，`dumps()`方法不知道如何将`Student`实例变为一个JSON的`{}`对象。

可选参数`default`就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为`Student`专门写一个转换函数，再把函数传进去即可：

```python
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
```



这样，`Student`实例首先被`student2dict()`函数转换成`dict`，然后再被顺利序列化为JSON：

```plain
>>> print(json.dumps(s, default=student2dict))
{"age": 20, "name": "Bob", "score": 88}
```



不过，下次如果遇到一个`Teacher`类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意`class`的实例变为`dict`：

```python
print(json.dumps(s, default=lambda obj: obj.__dict__))
```



因为通常`class`的实例都有一个`__dict__`属性，它就是一个`dict`，用来存储实例变量。也有少数例外，比如定义了`__slots__`的class。

同样的道理，如果我们要把JSON反序列化为一个`Student`对象实例，`loads()`方法首先转换出一个`dict`对象，然后，我们传入的`object_hook`函数负责把`dict`转换为`Student`实例：

```python
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
```



运行结果如下：

```plain
>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
>>> print(json.loads(json_str, object_hook=dict2student))
<__main__.Student object at 0x10cd3c190>
```



打印出的是反序列化的`Student`实例对象。

## pyecharts

### pyecharts有哪些配置选项

- pyecharts模块中有很多的配置选项，常用到的2个类别的选项

  - 全局配置选项
  - 系列配置选项

  

![py2](/home/lcx/Documents/markdown/工具学习/py2.png)

#### set_global_opts方法

```python
line.set_global_opts(
    title_opts = TitleOpts("测试",pos_left = "center",pos_bottom="%1"),
    legend_opts = LegendOpts(is_show=True),
    toolbox_opts = ToolboxOpes(is_show=True),
    visualmap_opts = VisualMapOpts(is_show = True),
    tooltip_opts = TooltipOpts(is_show=True),
)
```

### 数据处理

通过 json 对数据进行处理

...................................

### 地图可视化图表

#### 基础数据演示

```py
from pyecharts.charts import Map

map = Map()

data = [
    ("山东省",199),
    ("江苏省",299),
    ("内蒙古自治区",100),
    ("河北省",200),
    ("上海市",150),
]

map.add("测试地图",data,"china")

map.render()
```

#### 基础地图演示-视觉映射器

```python
#设置全局选项
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()

data = [
    ("山东省",499),
    ("江苏省",2),
    ("内蒙古自治区",100),
    ("河北省",20),
    ("上海市",15),
]
#设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":9,"label":"1-9","color":"#CCFFFF"},
            {"min":10,"max":99,"label":"10-99","color":"#FF6666"},
            {"min":100,"max":500,"label":"100-500","color":"#990033"},
            # {},
            # {},
            # {}
        ]
    )
)

map.add("测试地图",data,"china")

map.render()
```





### 柱状图

#### 柱状图

```python
from pyecharts.charts import Bar
from pyecharts.options import *
bar = Bar()

#添加x轴数据
bar.add_xaxis(["德州","呼和浩特","珠海"])
#添加y轴数据
bar.add_yaxis("人民素质",[30,20,10],label_opts=LabelOpts(position="right"))

# 反转x y轴
bar.reversal_axis()

#绘图
bar.render("基础柱状图.html")
```

#### 基础时间线柱状图的绘制

```python
from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
bar1 = Bar()
bar1.add_xaxis(["中国","美国","英国"])
bar1.add_yaxis("GDP",[30,30,20],label_opts = LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国","美国","英国"])
bar2.add_yaxis("GDP",[50,50,50],label_opts = LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国","美国","英国"])
bar3.add_yaxis("GDP",[70,60,60],label_opts = LabelOpts(position="right"))
bar3.reversal_axis()

tl = Timeline({"theme":ThemeType.INFOGRAPHIC})

tl.add(bar1,"点1")
tl.add(bar2,"点2")
tl.add(bar3,"点3")
#设置自动播放
tl.add_schema(
    play_interval = 1000,  #自动播放的时间间隔，单位毫秒
    is_timeline_show = True,#是否在自动播放的时候，显示时间线
    is_auto_play = True,    #是否自动播放
    is_loop_play = False     #是否循环自动播放
)
tl.render("基础时间线柱状图.html")

```

### 列表的sort方法

在前面我们学习过的sorted函数，可以对数据容器进行排序

在后面的数据处理中，我们需要对列表进行排序，并指定排序规则，sorted函数就无法完成了

使用方法：

列表.sort(key = 选择排序依据的函数，reverse=True|False)

- 参数key 是要求传入一个函数 表示将列表的每一个元素都传入函数中，返回排序的依据
- 参数reverse,是否反转排序结果，True表示降序，False表示升序

```python
 my_list = [["a",33],["b",55],["c",11]]

def choose_sort_key(element):
     return element[1]
 my_list.sort(key = choose_sort_key,reverse=True)
print(my_list)
```

```python
my_list = [["a",33],["b",55],["c",11]]
my_list.sort(key=lambda element : element[1],reverse = True)
print(my_list)
"""
结果：['b', 55], ['a', 33], ['c', 11]]
"""
```

### 类和对象

#### 魔术方法

- `__init__`:构造方法
- `__str__`:字符串方法
- `__It__`:大于、小于符号比较
- `__le__`:小于等于、大于等于符号比较
- `__eq__`:==符号比较

`__str__字符串方法`

```python
class Student:
    def __init__(self,age,name):
        self.age = age
        self.name = name

student = Student("周杰伦",11)
print(student)
print(str(student))
"""
结果：
<__main__.Student object at 0x000002585E37A848>
<__main__.Student object at 0x000002585E37A848>
"""
class Student:
    def __init__(self,age,name):
        self.age = age
        self.name = name
    def __str__(self):
        return f"student类对象,name = {self.name},age={self.age}"
student = Student("周杰伦",11)
print(student)
print(str(student))
"""
student类对象,name = 11,age=周杰伦
student类对象,name = 11,age=周杰伦
"""
```

`__It__小于符号比较方法`

```python
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __lt__(self,other):
        return self.age < other.age
stu1 = Student("许善强",28)
stu2 = Student("麦当当",48)
print(stu1<stu2)
print(stu1>stu2)
"""
True
False
"""
```

`__le__`小于等于比较符号

```python
class Student:
    def __init__(self,age,name):
        self.age = age
        self.name = name

    def __le__(self,other):
        return self.age <= other.age


stu1 = Student("许善强",28)
stu2 = Student("麦当当",28)

print(stu1<=stu2)
```

`__eq__(),比较运算符的实现方法`

<mark>不实现__eq__方法，对象之间可以比较，但是是比较内存，也即是：不同对象==比较一定是False的结果</mark>

<mark>实现了eq方法，就可以按照自己的想法来决定2个对象是否相等了</mark>

```python
class Student:
    def __init__(self,name,age):
        self.age = age
        self.name = name
    def __eq__(self, other):
        return self.age == other.age

stu1 = Student("许善强",28)
stu2 = Student("麦当当",28)

print(stu1==stu2)
```

### 封装——私有成员

定义私有成员的方法非常简单，只需要：

- 私有成员变量：变量名以__开头(两个下划线)
- 私有成员方法：方法名以__开头(两个下划线)

```python
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        __current_voltage = None

    def speak(self):
        print(f"我是练习两年半的个人练习生{self.name}")

    def __eat(self):
        print("不好意思你不是真爱粉")

    def check(self):
        if self.age > 18:
            self.__eat()
        else:
            self.speak()

stu1 = Student("许善强",18)
stu1.check()

```

```python
class Phone:
    def __init__(self,__is_5g_enable):
        self.__is_5g_enable = __is_5g_enable
    def __check_5g(self):
        if self.__is_5g_enable == True:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

phone = Phone(False)
phone.call_by_5g()
```

![py6](/home/lcx/Documents/markdown/工具学习/py6.jpg)

### 继承

```python
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.odl = 10
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
    def read_odometer(self):
        print(f"This car has{self.odometer_reading}miles on it")
    def increment_odometer(self,miles):
        self.odometer_reading += miles
class ElectricCar(Car):
    def __init__(self,make,model,year,butter):
        super().__init__(make,model,year)
        self.butter = butter

    def describe_battery(self):
        print(f"This car has a {self.butter} -KWh battery")
my_tesla = ElectricCar("tesla","midel s",2016,"45%")
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

```

```python
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.step=0
    def get_name(self):
        long_name="This is my "+str(self.year)+" "+self.make+" "+self.model
        print(long_name.title())
    def read_step(self):
        print("It has "+str(self.step)+" on it!")
    def update(self,mileage):
        if mileage>self.step:
            self.step=mileage
        else:
            print("it can't roll back!")
    def add_step(self,miles):
        self.step+=miles

my_car =Car("aodi","a6",2016)
my_car.get_name()
my_car.read_step()
my_car.update(500)
my_car.update(400)
my_car.read_step()
my_car.add_step(20)
my_car.read_step()
#继承
class Buttery:
    def __init__(self,butter):
        self.butter=butter
    def get_bu(self):
        print("目前电量百分百")
class ElectricCar(Car,Buttery):
    def __init__(self,make,model,year,butter):
        Car.__init__(self,make,model,year)
        Buttery.__init__(self,butter)
My_telsa=ElectricCar("telsa","model_s",2022,70)
My_telsa.get_name()
```

#### 多继承注意事项

多个父类中，如果有同名的成员，那么<mark>默认</mark>以继承顺序(从左到右)，为优先级

即：先继承的保留，后继承的被覆盖

#### 调用父类同名成员

一旦复写父类，那么类对象调用成员的时候，就会调用复写后的新成员，如果需要使用被复写的父类成员，需要特殊的调用方式：

- 方式一

  - 调用父类成员

    使用成员变量：父类名.成员变量

    使用成员方法:父类名.成员方法(self)

- 方法2

  - 使用super()调用父类成员

    使用成员变量:super().成员变量

    使用成员方法:super().成员方法()


### 类型注解

支持：

- 变量的类型注解
- 函数(方法)的形参列表和返回值的类型注解

#### 类型注解语法

![py3](/home/lcx/Documents/markdown/工具学习/py3.png)

为变量设置类型注解

基础语法：变量：类型

```python
var1:int = 10
var2:float = 3.1415
var3:bool = True
var4:bool = "ITheima"
```

类对象注解：

```python
class Student:
    pass
stu:Student = Student()
```

除了使用  变量:类型 ，这种语法做注解外 也可以在注释中进行类型注解

语法：

```python
class Student:
    pass
var1 = random = random.randint(1,10) #type: int
var2 = json.loads(data)  #type: dict[str,int]
var = func()  #type: Student
```

#### 函数和方法的类型注解

##### 函数和方法的形参类型注解语法：

```python
def 函数方法名(形参名:类型,形参名:类型1......):
    pass
def add(x:int,y:int):
    return a+b
```

##### 函数(方法)的返回值注解

语法如下:

```python
def 函数方法名(形参:类型，形参:类型......)->返回值类型:
    pass
```

```python
def add(a:int,b:int)->int:
    return a+b

c:int = 10
d:int = 20
print(add(c,d))
```

### Union类型

使用Union[类型,.....,类型]

可以定义联合类型注解

```python
from typing import Union
my_list:list[Union[str,int]] = [1,2,"itheima","itcast"]
my_dict:dict[str,Union[str,int]] = {"name":"许善强","age":31}
```

```python
def func(data:Union[int,str]) -> Union[int,str]:
    pass
func()
```

### 多态

多态，指的是：多种状态，即完成某个行为时，使用不同的对象会得到不同的状态

![py4](/home/lcx/Documents/markdown/工具学习/py4.jpg)



#### 抽象类(接口)

```python
class Animal:
    def __init__(self):
        pass
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")
def make_noise(animal:Animal):
    animal.speak()

dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)
```

父类Animal的speak方法是空实现

这种设计的含义是：

- 父类用来确定有哪些方法
- 具体的方法实现，由子类自行决定

这种写法，就叫做抽象类(也可以称之为接口)

抽象类：含有抽象方法的类称之为抽象类

抽象方法：方法体是空实现的(pass)称之为抽象方法

## 面向对象进阶

### 闭包

![py5](/home/lcx/Documents/markdown/工具学习/py5.png)

在函数嵌套的前提下，内部函数使用了外部函数 的变量，并且外部函数返回了内部函数，我们把这个使用外部函数变量的内部函数称为闭包。

#### 简单闭包

```python
def outer(logo):
    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")

    return inner

fn1 = outer("有大病")  //outer 返回 inner  而fn1 接收返回
fn1("麦丁华")
fn1("麦丁华的哥哥麦顶针")

fn2 = outer("确实有病")
fn2("麦当当")


```

在闭包中修改外部函数变量的值

需要适用`nunlocal`关键字修饰外部函数的变量才可在内部函数中修改它

```python
def outer(num1):
    def inner(num2):
        nonlocal num1
        num1+=num2
        print(num1)

    return inner

fn1 = outer(100)
fn1(100)
```

```python
def account_create(initial_amount=0):
    def atm(num,deposit = True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存入：{num},余额为:{initial_amount}")
        else:
            initial_amount -= num
            print(f"取出:{num},余额为:{initial_amount}")

    return atm

atm = account_create()
atm(100)
atm(200)
atm(100,False)
```

### 装饰器

装饰器其实也是一种闭包，其功能就是在**不破坏目标函数原有的代码和功能的前提下，为目标函数增加新功能**‘

#### 装饰器的一般写法(闭包写法)

```python
def outer(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我起床了")
    return inner
"""
定义一个闭包函数，在闭包函数内部：
- 执行目标函数
- 并完成功能的添加
"""
def sleep():
    import random
    import time
    print("睡眠中.......")
    time.sleep(random.randint(1,5))
    
fn = outer(sleep)
fn()
```

#### 装饰器的快捷写法(语法糖)

```python
def outer(func):
    def inner():
        print("我睡觉了")
        func()
        print("我起床了")

    return inner

@outer
def sleep():
    import random
    import time
    print("睡眠中.....")
    time.sleep(random.randint(1,5))

sleep()
```

使用`@outer`

定义在目标函数sleep之上

#### 装饰器传递参数

```python
import time
def logger(msg):
    def time_master(func):
        def call_func():
            start = time.time()
            func()
            stop = time.time()
            print(f"[{msg}]一共耗费了{(stop-start):.2f}")
        return call_func
    return time_master
@logger(msg="A")
def funcA():
    time.sleep(1)
    print("正在调用funcA...")
@logger(msg="B")
def funcB():
    time.sleep(1)
    print("正在调用funcA...")

funcA()
funcB()
"""
正在调用funcA...
[A]一共耗费了1.02
正在调用funcA...
[B]一共耗费了1.01
"""
```



#### 进阶

```python
class Person:
    def __init__(self,name,age):
        self.__name  = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        self.__age = age
    def play(self):
        if self.__age<=16:
            print(f"{self.__name}正在玩飞行棋")
        else:
            print(f"{self.__name}正在玩斗地主")

if __name__ == "__main__":
    person = Person("麦当当",17)
    print(person.age)
    person.play()
    person.age = 12
    person.play()
```

@property 装饰器用于将一个**方法**转换为只读属性。当一个方法被 @property 装饰后，它会将该方法转换为一个只读属性，并将其返回值作为属性值。这意味着你可以通过直接访问这个属性来获取其返回值，而无需显式调用方法。

这个装饰器通常用于类中的 getter 方法。通过将 getter 方法转换为只读属性，它可以让代码更加清晰和易读，同时还可以提供更好的封装性，使得属性的值只能通过 getter 方法来获取，而无法在外部被直接修改。

举个例子，如果一个类有一个私有属性 _age，你可以定义一个名为 age 的 @property 方法来获取它的值。这样，当你通过实例对象访问该属性时，它会调用该方法来获取 _age 的值，并将其返回作为属性值。这样就可以有效地隐藏属性 _age 的实现细节，同时又可以让外部代码通过直接访问属性的方式来获取其值。

`@age.setter` 是一个装饰器，用于定义一个设置 `age` 属性的方法，使其可以通过类实例进行赋值操作。使用 `@property` 装饰器定义的属性默认是只读的，而不能直接进行赋值操作。如果想要对 `@property` 定义的属性进行赋值，则需要再定义一个与其同名的方法，并添加 `@<property_name>.setter` 装饰器，其中 `<property_name>` 是属性的名称，用于标识这个方法是用于设置这个属性的。

在给 `age` 属性添加 `@age.setter` 装饰器后，可以使用类实例的 `age` 属性进行赋值操作，如 `person.age = 22`，就会调用 `@age.setter` 装饰器所装饰的方法，将 `age` 属性的值设置为 22。

**常用于私有的内部属性**

#### 静态方法

之前，我们在类中定义的方法都是对象方法，也就是说这些方法都是发送给对象的消息。实际上，我们写在类中的方法并不需要都是对象方法，例如我们定义一个“三角形”类，通过传入三条边长来构造三角形，并提供计算周长和面积的方法，但是传入的三条边长未必能构造出三角形对象，因此我们可以先写一个方法来验证三条边长是否可以构成三角形，这个方法很显然就不是对象方法，因为在调用这个方法时三角形对象尚未创建出来（因为都不知道三条边能不能构成三角形），所以这个方法是属于三角形类而并不属于三角形对象的。我们可以使用静态方法来解决这类问题，代码如下所示。

```python
from math import sqrt
class Triangle:
    def __init__(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c

    @staticmethod
    def is_valid(a,b,c):
        return a+b>c and a+c>b and b+c>a

    def perimeter(self):
        return self.__a+self.__b+self.__c
    def area(self):
        half = self.perimeter()/2
        return sqrt(half*(half-self.__a)*(half-self.__b)*(half-self.__c))


if __name__ == "__main__":
    a,b,c = 3,4,5
    if Triangle.is_valid(a,b,c):
        t = Triangle(a,b,c)
        print(t.perimeter())
        print(t.area())
    else:
        print("无法构成三角形")
```

#### 三元表达式

```python
color,msg = ("red","hello world")\
        if flag else ("blue","Goodbye,world!")
```

这行代码使用了Python的三元表达式（ternary operator），可以简洁地表达一个条件语句。在这个例子中，三元表达式的判断条件是 `flag` 变量，如果 `flag` 为真，则 `color` 变量被赋值为 `"red"`，`msg` 变量被赋值为 `"hello world"`；否则 `color` 变量被赋值为 `"blue"`，`msg` 变量被赋值为 `"Goodbye,world!"`。该表达式的语法比较简单，可以理解为 `if` 和 `else` 语句的简略写法。在该行代码中，使用了反斜杠 `\` 对代码进行了换行，是为了使代码更加易读。

### 正则表达式

在编写处理字符串的程序或网页时，经常会有查找符合某些复杂规则的字符串的需要。**正则表达式**就是用于描述这些规则的工具。换句话说，正则表达式就是记录文本规则的代码。

很可能你使用过Windows/Dos下用于文件查找的**通配符(wildcard)**，也就是*和?。如果你想查找某个目录下的所有的Word文档的话，你会搜索*.doc。在这里，*会被解释成任意的字符串。和通配符类似，正则表达式也是用来进行文本匹配的工具，只不过比起通配符，它能更精确地描述你的需求——当然，代价就是更复杂——比如你可以编写一个正则表达式，用来查找所有以0开头，后面跟着2-3个数字，然后是一个连字号“-”，最后是7或8位数字的字符串(像*010-12345678*或*0376-7654321*)。

#### 正则的三个基础方法

- `re.match`:从头开始匹配，匹配第一个命中项
- `re.search`:全局匹配，匹配第一个命中项
- `re.findall`:全局匹配,匹配全部命中项

re.match(匹配规则,被匹配字符串)

![py7](/home/lcx/Documents/markdown/工具学习/py7.png)

![py8](/home/lcx/Documents/markdown/工具学习/py8.png)

![py9](/home/lcx/Documents/markdown/工具学习/py9.png)

#### 元字符匹配

单字符匹配：

| 字符 |                 功能                  |
| :--: | :-----------------------------------: |
|  .   | 匹配任意一个字符(除了\n),\.匹配点本身 |
|  []  |          匹配[]中列举的字符           |
|  \d  |             匹配数组即0-9             |
|  \D  |              匹配非数字               |
|  \s  |        匹配空白、即空格、tab键        |
|  \S  |              匹配非空白               |
|  \w  |    匹配单词字符即a-z、A-Z、0-9、_     |
|  \W  |            匹配非单词字符             |

```python
import re
s = "mai1dang2dang3 shi4 mai5dang7dang6"
result = re.findall(r"\d",s)   #字符串的r标记，表示当前字符串是原始字符串，即内部的转义字符无效而是普通字符
print(result)
```

#### 数量匹配

| 字符  | 功能                              |
| :---: | :-------------------------------- |
|   *   | 匹配前一个规则的字符出现0至无数次 |
|   +   | 匹配前一个规则的字符出现1至无数次 |
|  ？   | 匹配前期个规则的字符出现0次或1次  |
|  {m}  | 匹配前一个规则的字符出现m次       |
| {m,}  | 匹配前一个规则的字符出现最少m次   |
| {m,n} | 匹配前一个规则的字符出现m到n次    |

#### 边界匹配

| 字符 | 功能               |
| :--: | ------------------ |
|  ^   | 匹配字符串开头     |
|  $   | 匹配字符串结尾     |
|  \b  | 匹配一个单词的边界 |
|  \B  | 匹配非单词边界     |

#### 分组匹配

| 字符 | 功能                     |
| :--: | ------------------------ |
|  \|  | 匹配左右任意一个表达式   |
|  ()  | 将括号中字符作为一个分组 |

```python
import re

r = "^[0-9a-zA-Z]{6,10}$"
s = "maidangdan"
print(re.findall(r,s))

r = r"^[1-9][0-9]{4,10}$"
s = '1234565'
print(re.findall(r,s))

#匹配邮箱地址，只允许qq、163、gmail这三种邮箱地址
r = r"(^[\w-]+(\.[\w-]+)*@(qq|163|gmail|imut)(\.[\w-]+)+$)"
s = "202210201013@imut.edu.cn"
print(re.findall(r,s))
```

### 进程和线程

#### 进程的创建步骤

1. 导入进程包 `import multiprocessing` 
2. 通过进程类创建进程对象 `进程对象 = multiprocessing.Process()`
3. 启动进程执行任务 `进程对象.start()`

进程对象 = multiprocessing.Process(target = 任务名)

| 参数名 | 说明                                       |
| ------ | ------------------------------------------ |
| target | 执行的目标任务名，这里指的是函数名(方法名) |
| name   | 进程名，一般不用设置                       |
| group  | 进程组，目前只能使用None                   |
| args   | 以元组的方式给执行任务传参                 |
| Kwargs | 以字典的方式给执行任务传参                 |



Python既支持多进程又支持多线程，因此使用Python实现并发编程主要有3种方式：多进程、多线程、多进程+多线程。

#### 获取进程编号

1. 获取当前进程编号 getpid()方法
2. 获取当前父进程编号  getppid() 方法

#### 进程间不共享全局变量

进程间不共享全局变量，实际上创建一个子进程就是把**主进程的资源进行拷贝产生了一个新的进程**，这里的主进程和子进程是相互独立的

我们在程序中创建进程的时候，子进程复制了父进程及其所有的数据结构，每个子进程有自己独立的内存空间，这也就意味着两个子进程中各有一个`counter`变量，所以结果也就可想而知了。要解决这个问题比较简单的办法是使用multiprocessing模块中的`Queue`类，它是可以被多个进程共享的队列，底层是通过管道和[信号量（semaphore）](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15)机制来实现的，

#### 主进程和子进程的结束顺序

主进程会等待所有子进程执行结束后再结束

1. 需要设置守护主程序

```python
import time
import multiprocessing

def work():
    for i in range(10):
        print("工作中")
        time.sleep(0.2)

if __name__ == "__main__":
        work_process = multiprocessing.Process(target=work())
        work_process.daemon = True
        work_process.start()

        time.sleep(1)
        print("主进程执行完成了")
```



2. 销毁子进程

```python
import time
from multiprocessing import Process

def work():
    for i in range(10):
        print("工作中...")
        time.sleep(0.2)

if __name__ == "__main__":
    work_process = Process(target=work())
    work_process.start()
    time.sleep(1)
    work_process.terminate()
    print("主进程执行完成了")
```



#### python中的多进程

Unix和Linux操作系统上提供了`fork()`系统调用来创建进程，调用`fork()`函数的是父进程，创建出的是子进程，子进程是父进程的一个拷贝，但是子进程拥有自己的PID。`fork()`函数非常特殊它会返回两次，父进程中可以通过`fork()`函数的返回值得到子进程的PID，而子进程中的返回值永远都是0。Python的os模块提供了`fork()`函数。由于Windows系统没有`fork()`调用，因此要实现跨平台的多进程编程，可以使用multiprocessing模块的`Process`类来创建子进程，而且该模块还提供了更高级的封装，例如批量启动进程的进程池（`Pool`）、用于进程间通信的队列（`Queue`）和管道（`Pipe`）等。

```python
from random import randint
from time import sleep,time

def download_task(filename):
    print(f"开始下载{filename}")
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print(f"{filename}下载完成，耗费了{time_to_download}秒")

def main():
    start = time()
    download_task("python从入门到住院.pdf")
    download_task("Peking Hot.avi")
    end = time()
    print(f"总共耗费了{end-start:.2f}")

if __name__ == "__main__":
    main()
"""
开始下载python从入门到住院.pdf
python从入门到住院.pdf下载完成，耗费了7秒
开始下载Peking Hot.avi
Peking Hot.avi下载完成，耗费了9秒
总共耗费了16.02
"""
```

从上面的例子可以看出，如果程序中的代码只能按顺序一点点的往下执行，那么即使执行两个毫不相关的下载任务，也需要先等待一个文件下载完成后才能开始下一个下载任务，很显然这并不合理也没有效率。接下来我们使用多进程的方式将两个下载任务放到不同的进程中，代码如下所示。

```python
from multiprocessing import Process
from time import time, sleep
from download import download_task

def main():
    start = time()
    p1 = Process(target=download_task,args=("python从入门到住院.pdf",))
    p1.start()
    p2 = Process(target=download_task,args=("Peking Hot.avi",))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print(f"总共耗费了{end-start:.2f}")

if __name__ == "__main__":
    main()
from random import randint
from time import time, sleep
from os import getpid

def download_task(filename):
    print(f"启动下载进程，进程号[{getpid()}]")
    print(f"开始下载{filename}")
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print(f"{filename}下载完成！耗费了{time_to_download}秒")
    
    
    """
   启动下载进程，进程号[29472]
开始下载Peking Hot.avi
启动下载进程，进程号[16708]
开始下载python从入门到住院.pdf
python从入门到住院.pdf下载完成！耗费了7秒
Peking Hot.avi下载完成！耗费了10秒
总共耗费了10.30
    """
```

### 线程

#### 线程的创建步骤

1. 导入线程模块 `import threading`
2. 通过线程类创建线程对象 `threading.Thread(target=任务名)`
3. 启动线程执行任务 `线程对象.start()`

线程对象 = threading.Thread(target=任务名)

| 参数名 | 说明                                   |
| ------ | -------------------------------------- |
| target | 执行的任务名，这里指的是函数名(方法名) |
| name   | 线程名，一般不用设置                   |
| group  | 线程组，目前只能使用None               |
| args   | 以元组的方式给执行任务传参             |
| kargs  | 以字典方式给执行任务传参               |

#### 主线程和子线程的结束顺序

主线程会等待所有的子线程执行结束后主线程再结束

想要主线程不等待子线程执行完成可以设置守护主线程

```python
#设置守护主线程方式1,daemon=True 守护主线程
work_thread = threading.Thread(target=work,daemon=True)
#设置守护主线程方式2
#work_whread.setDaemon(True)
work_thread.start()
#主线程延时1秒
time.sleep(1)
print("over")
```

#### 线程间的执行顺序

线程之间的执行是无序的 是由CPU调度决定某个线程先执行的。

##### 获取当前线程信息

```python
#通过current_thread方法获取线程对象
current_thread = threading.current_thread()
#通过current_thread对象可以知道线程的相关信息，例如被创建的顺序
print(current_thread)
```

#### 线程间共享全局变量

多个线程都是在同一个进程中的，多个线程使用的资源都是**同一个进程中的资源**，因此多线程间是共享全局变量

```python
import threading
import time
my_list = []

def write_data():
    for i in range(3):
        print("add:",i)
        my_list.append(i)
    print("write:",my_list)

def read_data():
    print("read:",my_list)

if __name__ == "__main__":
    write_thread = threading.Thread(target=write_data())
    read_thread = threading.Thread(target=read_data())

    write_thread.start()
    time.sleep(1)
    read_thread.start()
"""
add: 0
add: 1
add: 2
write: [0, 1, 2]
read: [0, 1, 2]
"""
```

#### 线程之间共享全局变量出现错误的问题

```python
import threading
g_num = 0

def sum_num1():
    for i in range(1000000):
        global g_num
        g_num += 1

    print(f"g_num1:{g_num}")

def sum_num2():
    for i in range(1000000):
        global g_num
        g_num += 1

    print(f"g_num2:{g_num}")

if __name__ == "__main__":
    sum1_thread = threading.Thread(target=sum_num1)
    sum2_thread = threading.Thread(target=sum_num2)

    sum1_thread.start()
    sum2_thread.start()
"""
g_num1:1296837
g_num2:1427881
"""
```

解决办法：

同步：就是协同步调，按预先的先后次序进行运行。好比现实生活的对讲机，你说完之后，我再说，不能大家一起说

使用线程同步：保证同一时刻只能有一个线程去操作全局变量

线程同步方式：互斥锁

#### 互斥锁

多共享数据进行锁定，保证同一时刻只有一个线程去操作

注意：

互斥锁是多个线程一起去抢，强盗所的线程先执行，没有抢到锁的线程进行等待，等锁使用完释放后，其它等待的线程再去抢这个锁

##### 如何使用

1. 互斥锁的创建：`mutex = threading.Lock()`
2. 上锁：`mutex.acquire()`
3. 释放锁：`mutex.release()`

```python
import threading

g_num = 0

def sum_num1():
    mutex.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1
    mutex.release()
    print(f"g_num1:{g_num}")

def sum_num2():
    mutex.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1
    mutex.release()
    print(f"g_num2:{g_num}")

if __name__ == "__main__":
    mutex = threading.Lock()
    sum1_thread = threading.Thread(target=sum_num1)
    sum2_thread = threading.Thread(target=sum_num2)

    sum1_thread.start()
    sum2_thread.start()
"""
g_num1:1000000
g_num2:2000000
"""
```

#### 死锁

一直等待对方释放锁的情景就是死锁

死锁一旦产生就会造成应用程序的停止响应，应用程序无法再继续往下执行了。

#### 进程和线程的对比

##### 关系对比

1. 线程是依附在进程里面的，没有进程就没有线程
2. 一个进程默认提供一条线程，进程可以创建多个线程

##### 区别对比

1. 进程之间不共享全局变量
2. 线程之间共享全局变量，但是要注意资源竞争问题，解决办法：互斥锁或者线程同步
3. 创建进程的资源开销要比创建线程的资源开销更大
4. 进程是操作系统资源分配的基本单位，线程是CPU调度的基本单位
5. 线程不能够独立执行，必须依存在进程中

##### 优缺点对比

1. 进程优缺点

   - 优点：可以用多核
   - 缺点：资源开销大

2. 线程优缺点：

   - 优点：资源开销小
   - 缺点：不能使用多核

   我们可以直接使用threading模块的`Thread`类来创建线程，但是我们之前讲过一个非常重要的概念叫“继承”，我们可以从已有的类创建新类，因此也可以通过继承`Thread`类的方式来创建自定义的线程类，然后再创建线程对象并启动线程。代码如下所示。

```python
from random import randint
from threading import Thread
from time import time, sleep


class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))


def main():
    start = time()
    t1 = DownloadTask('Python从入门到住院.pdf')
    t1.start()
    t2 = DownloadTask('Peking Hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
```

## 异步io

```python
# 协程yield实现生产者消费者模式

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)

"""
yield r 的双重角色
作为产出：当执行到 yield r 时，生成器暂停，把 r 返回给外部调用者（此处是 produce）。
作为输入点：下一次外部调用 send(value) 恢复生成器时，yield 表达式的值就是 value。因此把 yield r 写成 n = yield r，就能捕获外部传来的值并赋给 n。
send(n) 为什么能给 n 赋值
首次 c.send(None) 只是预激活，生成器停在 yield r，并把初始 r 返回给外部。
之后每次 c.send(n)：
将 n 作为 yield 表达式的结果返回给生成器，所以 n = yield r 中的右侧 yield r 此刻等于传入的 n。
生成器继续往下执行，此时 n 就是外部传入的数字。
总结：n = yield r 让生成器既能“出”数据（r）又能“收”数据（n）；send(n) 恰好把值送回同一个挂起点，让 n 获得外部传来的内容。
"""
```

```python
import asyncio
import time


async def fake_io(name: str, delay: float) -> None:
    # 模拟一次耗时的异步任务
    print(f"开始 {name}")
    await asyncio.sleep(delay)
    print(f"结束 {name}")


async def run_sequential() -> None:
    # 顺序等待两个任务，演示串行耗时
    start = time.perf_counter()
    await fake_io("任务一", 1)
    await fake_io("任务二", 1)
    duration = time.perf_counter() - start
    print(f"串行完成耗时 {duration:.2f} 秒\n")


async def run_concurrent() -> None:
    # 并发等待两个任务，演示协程带来的速度提升
    start = time.perf_counter()
    await asyncio.gather(fake_io("任务一", 1), fake_io("任务二", 1))
    duration = time.perf_counter() - start
    print(f"并发完成耗时 {duration:.2f} 秒\n")


async def main() -> None:
    print("=== 串行等待演示 ===")
    await run_sequential()
    print("=== 并发等待演示 ===")
    await run_concurrent()


if __name__ == "__main__":
    asyncio.run(main())


"""
asyncio提供了完善的异步IO支持，用asyncio.run()调度一个coroutine；
在一个async函数内部，通过await可以调用另一个async函数，这个调用看起来是串行执行的，
但实际上是由asyncio内部的消息循环控制；
在一个async函数内部，通过await asyncio.gather()可以并发执行若干个async函数。
"""
```



## pathlib

核心操作对比 (一张表看懂)

假设我们现在的项目结构是：

```
project/
├── main.py
└── static/
    └── images/
        └── test.jpg
```

| **操作**             | **老写法 (os.path)**               | **新写法 (pathlib)**                         |
| -------------------- | ---------------------------------- | -------------------------------------------- |
| **引入**             | `import os`                        | `from pathlib import Path`                   |
| **当前路径**         | `os.getcwd()`                      | `Path.cwd()`                                 |
| **当前脚本所在目录** | `os.path.dirname(__file__)`        | `Path(__file__).parent`                      |
| **拼接路径**         | `os.path.join("static", "images")` | **`Path("static") / "images"`** (最爽的特性) |
| **检查存在**         | `os.path.exists(path)`             | `path.exists()`                              |
| **创建文件夹**       | `os.makedirs(path, exist_ok=True)` | `path.mkdir(parents=True, exist_ok=True)`    |
| **获取文件名**       | `os.path.basename(path)`           | `path.name`                                  |
| **获取后缀**         | `os.path.splitext(path)[1]`        | `path.suffix`                                |
| **获取不带后缀的名** | `os.path.splitext(path)[0]`        | `path.stem`                                  |

 第三部分：毕设场景实战 (跟着敲！)

在你的风电毕设中，你会有两个高频场景：

1. **加载模型**：找到项目根目录下的 `weights/best.pt`。
2. **保存上传**：把前端传来的图存到 `static/uploads`，如果目录不存在要自动创建。

请在 VS Code 中新建 `learn_pathlib.py`，手敲以下代码：

#### 场景 1：优雅地定位项目根目录

```python
from pathlib import Path

# 1. 获取当前脚本的绝对路径
# .resolve() 把相对路径变成绝对路径 (比如 C:\Projects\wind\...)
current_file = Path(__file__).resolve()
print(f"当前脚本: {current_file}")

# 2. 获取父目录 (即项目根目录)
# 以前要写 os.path.dirname(os.path.dirname(...))，很难看
project_root = current_file.parent
print(f"项目根目录: {project_root}")

# 3. 拼接模型路径 (使用 / 运算符)
# 不管你是 Windows (\\) 还是 Linux (/)，它自动适配
model_path = project_root / "weights" / "best.pt"
print(f"模型路径: {model_path}")

# 检查模型是否存在
if not model_path.exists():
    print("⚠️ 警告: 模型文件没找到，请检查路径！")
```

#### 场景 2：自动创建上传目录

这是你写 `/upload` 接口时的标准写法：

```python
# 定义上传目录
upload_dir = project_root / "static" / "uploads"

# 创建目录
# parents=True: 如果 static 不存在，也顺便创建 (类似 mkdir -p)
# exist_ok=True: 如果目录已经存在，不要报错，啥也不做
upload_dir.mkdir(parents=True, exist_ok=True)

print(f"✅ 上传目录已就绪: {upload_dir}")

# 模拟保存文件
file_path = upload_dir / "blade_01.jpg"
print(f"准备保存到: {file_path}")

# pathlib 可以直接打开文件 (替代 open(path, 'w'))
# write_text / write_bytes 是 pathlib 的快捷方法
file_path.write_text("模拟图片数据") 
print("写入成功！")
```

#### 场景 3：解析文件名 (YOLO 结果处理常用)

```python
# 假设这是上传的文件路径
p = Path("static/uploads/blade_2023_v1.jpg")

print(f"完整文件名: {p.name}")      # blade_2023_v1.jpg
print(f"文件后缀:   {p.suffix}")    # .jpg
print(f"纯文件名:   {p.stem}")      # blade_2023_v1 (没有后缀)
print(f"父级目录:   {p.parent}")    # static\uploads

# 换个后缀 (比如把 .jpg 换成 .json 用来存结果)
json_path = p.with_suffix(".json")
print(f"对应的JSON路径: {json_path}") # static\uploads\blade_2023_v1.json
```

 第四部分：进阶技巧 (Glob 文件搜索)

如果你想做**“批量检测”**，需要遍历文件夹下所有的图片，`pathlib` 比 `os.walk` 简单一万倍。

```python
# 遍历 static/uploads 目录下所有的 .jpg 图片
image_dir = Path("static/uploads")

# glob 方法支持通配符
# *.jpg 表示所有 jpg 文件
# **/*.jpg 表示递归查找所有子文件夹里的 jpg (非常强大)
print("\n--- 扫描图片 ---")
for img_file in image_dir.glob("*.jpg"):
    print(f"发现图片: {img_file.name}")
```















