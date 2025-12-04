python中的函数和方法

1. enumerate()

emmumerate()函数用于返回一个枚举对象，他的功能就是将可迭代对象中的每个元素及从0开始的序号共同构成一个二元组的列表。

```python
list1 = ["Spring","Summer","Fall","Winter"]
print(list(enumerate(list1)))
print(list(enumerate(list1,10)))
"""
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
[(10, 'Spring'), (11, 'Summer'), (12, 'Fall'), (13, 'Winter')]
"""
```

2. zip

zip()函数用于创建一个聚合多个可迭代对象的迭代器。它会将最为参数传入的每个可迭代对象的每个元素依次组合成元组,即第i个元组包含来自每个参数的第i个元素

```python
x = [1,2,3]
y = [4,5,6]
zipped = zip(x,y)
print(list(zipped))
z = [7,8,9]
zipped = zip(x,y,z)
print(list(zipped))
z = "mai dang dang"
zipped = zip(x,y,z)
print(list(zipped))
import itertools
zipped = itertools.zip_longest(x,y,z)
print(list(zipped))
"""
[(1, 4), (2, 5), (3, 6)]
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
[(1, 4, 'm'), (2, 5, 'a'), (3, 6, 'i')]
[(1, 4, 'm'), (2, 5, 'a'), (3, 6, 'i'), (None, None, ' '), (None, None, 'd'), (None, None, 'a'), (None, None, 'n'), (None, None, 'g'), (None, None, ' '), (None, None, 'd'), (None, None, 'a'), (None, None, 'n'), (None, None, 'g')]
"""
```

3. map()

map()函数会根据提供的函数对可指定的可迭代对象的每个元素进行运算，并将返回运算结果的迭代器。

```python
mapped = map(ord,"mdh")
print(list(mapped))
mapped_1 = map(pow, [2,3,10], [2,3,5])
print(list(mapped_1))
"""
[109, 100, 104]
[4, 27, 100000]
"""
```

4. filter()

filter()函数会根据提供的函数对指定的可迭代对象的每个元素进行运算，并将运算结果为真的元素，以迭代器的形式返回。

```python
print(list(filter(str.islower,"Mdh")))
"""
['d', 'h']
"""
```

<mark>迭代器是一次性的，可迭代对象是可重复的</mark>

```python
mapped = map(ord,"MdhandPig")
for each in mapped:
    print(each)

print(list(mapped))
"""
77
100
104
97
110
100
80
105
103
[]
"""
```

5 . iter()

```python
x = [1,2,3,4,5]
y = iter(x)
print(type(x),type(y))
for i in range(6):
    print(next(y))
    """
    <class 'list'> <class 'list_iterator'>
1
2
3
4
5
Traceback (most recent call last):
  File "D:\python\PyCharm 2022.3.3\plugins\python\helpers\pydev\pydevconsole.py", line 364, in runcode
    coro = func()
  File "<input>", line 1, in <module>
  File "D:\python\PyCharm 2022.3.3\plugins\python\helpers\pydev\_pydev_bundle\pydev_umd.py", line 198, in runfile
    pydev_imports.execfile(filename, global_vars, local_vars)  # execute the script
  File "D:\python\PyCharm 2022.3.3\plugins\python\helpers\pydev\_pydev_imps\_pydev_execfile.py", line 18, in execfile
    exec(compile(contents+"\n", file, 'exec'), glob, loc)
  File "F:\py\project\demo4\demo24.py", line 5, in <module>
    print(next(y))
StopIteration
    """
    
z = iter(x)
for i in range(6):
    print(next(y,"没啦，被你掏空了~"))
    """
    1
	2
	3
	4
	5
没啦，被你掏空了~
    """
```

6. reduce

```python
import functools
c = functools.reduce(lambda x,y:x*y, range(1,11))
print(c)
a = functools.reduce(lambda x,y:x+y,[i for i in range(6)])
print(a)
```

7. `__getitem__()`

如果在类中定义了`__getitem__()`方法，那么他的实例对象（假设为P）就可以这样P[key]取值。当实例对象做P[key]运算时，就会调用类中的`__getitem__()`方法。

```python
# -*- coding:utf-8 -*-
class DataTest:
    def __init__(self,id,address):
        self.id=id
        self.address=address
        self.d={self.id:1,
                self.address:"192.168.1.1"
                }
        
    def __getitem__(self,key):
        return "hello"
    
 
data=DataTest(1,"192.168.2.11")
print data[2]
"""
hello
"""
```

在这我认为实例对象的key不管是否存在都会调用类中的`__getitem__()`方法。而且返回值就是`__getitem__()`方法中规定的return值。

8. `__len__`
