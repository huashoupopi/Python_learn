# py中的一些常用包



## tqdm

### tqdm模块是python进度条库, 主要分为两种运行模式

#### 基于迭代对象运行:tqdm(iterator)from tqdm import tqdm,trange

```python
import time
#基于迭代对象运行: tqdm(iterator)
from tqdm import tqdm, trange
for i in tqdm(range(100),desc="progress"):
    time.sleep(0.05)
    
for j in trange(100):
    time.sleep(0.03)
    
dic = ['a','b','c','d','e']
pbar = tqdm(dic)
for i in pbar:
    pbar.set_description('Processing '+i)
    time.sleep(1)
```

#### 手动进行更新

```python
from tqdm import tqdm,trange
import time

with tqdm(total=200) as pbar:
    pbar.set_description("Processing")
    
    for i in range(20):
        time.sleep(0.1)
        pbar.update(10)
```

### tqdm参数说明

```python
class tqdm(object):
  """
  Decorate an iterable object, returning an iterator which acts exactly
  like the original iterable, but prints a dynamically updating
  progressbar every time a value is requested.
  """

  def __init__(self, iterable=None, desc=None, total=None, leave=False,
               file=sys.stderr, ncols=None, mininterval=0.1,
               maxinterval=10.0, miniters=None, ascii=None,
               disable=False, unit='it', unit_scale=False,
               dynamic_ncols=False, smoothing=0.3, nested=False,
               bar_format=None, initial=0, gui=False):
```

- iterable: 可迭代的对象, 在手动更新时不需要进行设置
- desc: 字符串, 左边进度条描述文字
- total: 总的项目数
- leave: bool值, 迭代完成后是否保留进度条
- file: 输出指向位置, 默认是终端, 一般不需要设置
- ncols: 调整进度条宽度, 默认是根据环境自动调节长度, 如果设置为0, 就没有进度条, 只有输出的信息
- unit: 描述处理项目的文字, 默认是'it', 例如: 100 it/s, 处理照片的话设置为'img' ,则为 100 img/s
- unit_scale: 自动根据国际标准进行项目处理速度单位的换算, 例如 100000 it/s >> 100k it/s

#### 展示

```python
import time
from tqdm import tqdm

# 发呆0.5s
def action():
    time.sleep(0.5)
with tqdm(total=100000, desc='Example', leave=True, ncols=100, unit='B', unit_scale=True) as pbar:
    for i in range(10):
        # 发呆0.5秒
        action()
        # 更新发呆进度
        pbar.update(10000)
```



## os

```python
import os
os.listdir("D:/test")		#列出路径下的内容
os.path.isdir("D:/test/a")	#判断指定路径是不是文件夹
os.path.exists("D:/test")	#判断指定路径是否存在
```

`os.makedirs()`  创建文件夹

`os.path.join()`

os.path.join()函数用于路径拼接文件路径，可以传入多个路径

```python
#如果不存在以‘’/’开始的参数，则函数会自动加上
import os
print(os.path.join('path','abc','yyy'))
path\abc\yyy
#存在以‘’/’’开始的参数，从最后一个以”/”开头的参数开始拼接，之前的参数全部丢弃。
>>> print('1',os.path.join('aaa','/bbb','ccc.txt'))
1 /bbb\ccc.txt
 
>>> print('1',os.path.join('/aaa','/bbb','ccc.txt'))
1 /bbb\ccc.txt
 
>>> print('1',os.path.join('/aaa','/bbb','/ccc.txt'))
1 /ccc.txt
 
>>> print('1',os.path.join('/aaa','bbb','ccc.txt'))
1 /aaa\bbb\ccc.txt
 
>>> print('1',os.path.join('/aaa','bbb','/ccc.txt'))
1 /ccc.txt
#同时存在以‘’./’与‘’/’’开始的参数，以‘’/’为主，从最后一个以”/”开头的参数开始拼接，之前的参数全部丢弃。
>>> print('2',os.path.join('/aaa','./bbb','ccc.txt'))
2 /aaa\./bbb\ccc.txt
>>> print('2',os.path.join('aaa','./bbb','/ccc.txt'))
2 /ccc.txt
#只存在以‘’./’开始的参数,会从”./”开头的参数的上一个参数开始拼接
>>> print('2',os.path.join('aaa','./bbb','ccc.txt'))
2 aaa\./bbb\ccc.txt
#注意
path='C:/yyy/yyy_data/'
>>> print(os.path.join(path,'/abc'))
C:/abc
>>> print(os.path.join(path,'abc'))
C:/yyy/yyy_data/abc
```



## warnings

在python中运行代码经常会遇到的情况是——代码可以正常运行但是会提示警告

那么如何来控制警告输出呢？其实很简单，python通过调用warnings模块中定义的warn()函数来发出警告。我们可以通过警告过滤器进行控制是否发出警告消息，

```python
import warnings
warnings.filterwarnings('ignore')
```

```py
warnings.filterwarnings(action, 
						message='', 
						category=Warning, 
						module='', 
						lineno=0, 
						append=False)
```

过滤警告，在 警告过滤器规则 列表中插入一个条目。默认情况下，条目插入在前面；如果 append 为真，则在末尾插入。它检查参数的类型，编译 message 和 module 的正则表达式，并将它们作为警告过滤器列表中的元组插入。如果多个地方都匹配特定的警告，那么更靠近列表前面的条目会覆盖列表中后面的条目，省略的参数默认为匹配一切的值。

action:

|    值     |                处理方式                 |
| :-------: | :-------------------------------------: |
|  "error"  |          将匹配警告转换为异常           |
| "ignore"  |             忽略匹配的警告              |
| "always"  |           始终输出匹配的警告            |
| "default" |  对于同样的警告只输出第一次出现的警告   |
| "module"  |   在一个模块中只输出第一次出现的警告    |
|  "once"   | 输出第一次出现的警告,而不考虑它们的位置 |

- `message` 是包含正则表达式的字符串，警告消息的开始必须匹配，不区分大小写
- `category` 是一个警告类型（必须是 Warning 的子类）
- `module` 是包含模块名称的正则表达式字符串，区分大小写
- `lineno` 是一个整数，警告发生的行号，为 0 则匹配所有行号
