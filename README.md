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
```


## LICENSE

MIT [@chenjiandongx](https://github.com/chenjiandongx)
