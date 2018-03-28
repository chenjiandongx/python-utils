
## [timeit.py](https://github.com/chenjiandongx/python-utils/blob/master/utils/timeit.py)

> 用于测试代码运行时间


### timeit_block

> timeit_block(unit='s', label="")

*测试代码块时间*

* unit: 时间单位，有 's','m','h' 可选（seconds，minutes，hours）
* label: 代码块标签

用法
```python
with timeit_block():
    for i in range(100000):
        i += 1
```

输出
```shell
Total time running : 0.008527040481567383 seconds
```

### timeit_func

> timeit_func(unit='s')

*测试函数耗时*

* unit: 时间单位，有 's','m','h' 可选（seconds，minutes，hours）

用法
```python
@timeit_func()
def test():
    for i in range(100000):
        i += 1
test()
```

输出
```shell
Total time running : 0.008527040481567383 seconds
```
