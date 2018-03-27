# Python 实用工具函数

此项目的目的是为了将平时用到的一些工具函数集合起来，方便使用

### timeit.py
> 用于测试代码运行时间

#### 函数

**timeit_block(unit='s', label="")**
```
测试代码块时间

:param unit: 时间单位，有 's','m','h' 可选（秒，分，时）
:param label: 代码块标签

> 用法

with timeit_block():
    for i in range(100000):
        i += 1
```

**timeit_func(unit='s')**
```
测试函数耗时

:param unit: 时间单位，有 's','m','h' 可选（秒，分，时）

> 用法
@timeit_func()
def test():
    for i in range(100000):
        i += 1
```


未完待续....

## LICENSE

MIT [@chenjiandongx](https://github.com/chenjiandongx)
