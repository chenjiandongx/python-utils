
## profileit.py

> 用于测试函数运行消耗情况

### profileit
> profileit(field='cumulative')

*测试函数运行消耗情况*

* field: 输出内容排序方式。可选参数为 "stdname", "calls", "time", "cumulative"

用法
```python
@profileit()
def test():
    for i in range(100000):
        i += 1
test()
```

输出
```shell
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
