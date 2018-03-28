## [memoryit.py](https://github.com/chenjiandongx/python-utils/blob/master/utils/memoryit.py)

> 用于追踪代码内存消耗情况

### memoryit_func
> memoryit_func(group_by='lineno', limit=10)

*追踪函数内存消耗情况*

* group_by: 统计分组，有 'filename', 'lineno', 'traceback' 可选
* limit: 限制输出行数

用法
```python
@memoryit_func()
def test():
    for i in range(100000):
        i += 1
test()
```

输出
```shell
TraceMalloc for test()
C:\Users\chenjiandongx\Anaconda3\lib\tracemalloc.py:387: size=536 B (+536 B), count=3 (+3), average=179 B
D:/Python/python-utils/utils/memoryit.py:34: size=440 B (+440 B), count=1 (+1), average=440 B
C:\Users\chenjiandongx\Anaconda3\lib\tracemalloc.py:524: size=56 B (+56 B), count=1 (+1), average=56 B
C:\Users\chenjiandongx\Anaconda3\lib\tracemalloc.py:281: size=40 B (+40 B), count=1 (+1), average=40 B
```


### memoryit_block
> memoryit_block(group_by='lineno', limit=10, label='code block')

*追踪代码块内存消耗情况*

* group_by: 统计分组，有 'filename', 'lineno', 'traceback' 可选
* limit: 限制输出行数
* label: 代码块标签

用法
```python
with memoryit_block():
    for i in range(100000):
        i += 1
```

输出
```shell
TraceMalloc for code block
C:\Users\chenjiandongx\Anaconda3\lib\tracemalloc.py:387: size=608 B (+608 B), count=4 (+4), average=152 B
D:/Python/python-utils/utils/memoryit.py:63: size=604 B (+604 B), count=2 (+2), average=302 B
C:\Users\chenjiandongx\Anaconda3\lib\tracemalloc.py:524: size=504 B (+504 B), count=2 (+2), average=252 B
C:\Users\chenjiandongx\Anaconda3\lib\tracemalloc.py:281: size=40 B (+40 B), count=1 (+1), average=40 B
```
