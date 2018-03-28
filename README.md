# Python 实用工具函数

此项目的目的是为了将平时用到的一些工具函数集合起来，方便使用

## timeit.py
> 用于测试代码运行时间

### 函数

**timeit_block(unit='s', label="")**
```
> 测试代码块时间

:param unit: 时间单位，有 's','m','h' 可选（seconds，minutes，hours）
:param label: 代码块标签

> 用法
with timeit_block():
    for i in range(100000):
        i += 1

> 输出
Total time running : 0.008527040481567383 seconds
```

**timeit_func(unit='s')**
```
> 测试函数耗时

:param unit: 时间单位，有 's','m','h' 可选（seconds，minutes，hours）

> 用法
@timeit_func()
def test():
    for i in range(100000):
        i += 1
test()

> 输出
Total time running : 0.008527040481567383 seconds
```


## profileit.py
> 用于测试函数运行消耗情况

### 函数

**profileit(field='cumulative')**
```
> 测试函数运行消耗情况

:param field: 输出内容排序方式。
    可选参数为 "stdname", "calls", "time", "cumulative"

> 用法
@profileit()
def test():
    for i in range(100000):
        i += 1
test()

> 输出
Profile info for test()
         2 function calls in 0.004 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.004    0.004    0.004    0.004 profileit.py:30(test)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


   Ordered by: cumulative time

Function                                          was called by...
profileit.py:30(test)                             <-
{method 'disable' of '_lsprof.Profiler' objects}  <-
```


## memoryit.py
> 用于追踪代码内存消耗情况

## 函数

**memoryit_func(group_by='lineno', limit=10)**
```
> 追踪函数内存消耗情况

:param group_by: 统计分组，有 'filename', 'lineno', 'traceback' 可选
:param limit: 限制输出行数

> 用法
@memoryit_func()
def test():
    for i in range(100000):
        i += 1
test()

> 输出
TraceMalloc for test()
C:\Users\chenjiandongx\Anaconda3\lib\tracemalloc.py:387: size=536 B (+536 B), count=3 (+3), average=179 B
D:/Python/python-utils/utils/memoryit.py:34: size=440 B (+440 B), count=1 (+1), average=440 B
C:\Users\chenjiandongx\Anaconda3\lib\tracemalloc.py:524: size=56 B (+56 B), count=1 (+1), average=56 B
C:\Users\chenjiandongx\Anaconda3\lib\tracemalloc.py:281: size=40 B (+40 B), count=1 (+1), average=40 B
```

**memoryit_block(group_by='lineno', limit=10, label='code block')**
```
> 追踪代码块内存消耗情况

:param group_by: 统计分组，有 'filename', 'lineno', 'traceback' 可选
:param limit: 限制输出行数
:param label: 代码块标签

> 用法
with memoryit_block():
    for i in range(100000):
        i += 1

> 输出
TraceMalloc for code block
C:\Users\chenjiandongx\Anaconda3\lib\tracemalloc.py:387: size=608 B (+608 B), count=4 (+4), average=152 B
D:/Python/python-utils/utils/memoryit.py:63: size=604 B (+604 B), count=2 (+2), average=302 B
C:\Users\chenjiandongx\Anaconda3\lib\tracemalloc.py:524: size=504 B (+504 B), count=2 (+2), average=252 B
C:\Users\chenjiandongx\Anaconda3\lib\tracemalloc.py:281: size=40 B (+40 B), count=1 (+1), average=40 B
```


## LICENSE

MIT [@chenjiandongx](https://github.com/chenjiandongx)
