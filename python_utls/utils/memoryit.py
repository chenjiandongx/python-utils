#!/usr/bin/env python
# coding=utf-8

from functools import wraps
from contextlib import contextmanager

import tracemalloc


def _print(stats, limit, label):
    """
    控制输出量
    """
    print("TraceMalloc for {}".format(label))
    for index, stat in enumerate(stats):
        if index < limit:
            print(stat)
        else:
            break


def memoryit(group_by='lineno', limit=10):
    """
    追踪函数内存消耗情况

    :param group_by: 统计分组，有 'filename', 'lineno', 'traceback' 可选
    :param limit: 限制输出行数
    """
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            tracemalloc.start()
            _start = tracemalloc.take_snapshot()
            _result = func(*args, **kwargs)
            _end = tracemalloc.take_snapshot()
            stats = _end.compare_to(_start, group_by)
            _print(stats, limit, func.__name__ + '()')
            return _result
        return inner
    return wrapper


@contextmanager
def memoryit_block(group_by='lineno', limit=10, label='code block'):
    """
    追踪代码块内存消耗情况

    :param group_by: 统计分组，有 'filename', 'lineno', 'traceback' 可选
    :param limit: 限制输出行数
    :param label: 代码块标签
    """
    tracemalloc.start()
    _start = tracemalloc.take_snapshot()
    try:
        yield
    finally:
        _end = tracemalloc.take_snapshot()
        stats = _end.compare_to(_start, group_by)
        _print(stats, limit, label)
