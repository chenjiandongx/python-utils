#!/usr/bin/env python
# coding=utf-8

from cProfile import Profile
from pstats import Stats
from functools import wraps


def profileit(field='cumulative'):
    """
    测试函数耗时

    :param field: 输出内容排序方式。
        可选参数为 "stdname", "calls", "time", "cumulative"
    """
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            pro = Profile()
            pro.runcall(func, *args, **kwargs)
            stats = Stats(pro)
            stats.strip_dirs()
            stats.sort_stats(field)
            stats.print_stats()
            stats.print_callers()
        return inner
    return wrapper
