#!/usr/bin/env python
# coding=utf-8

import time
from contextlib import contextmanager
from functools import wraps


def _green(string):
    """
    将字体转变为绿色
    """
    return '\033[32m{}\033[0m'.format(string)


def _format(unit='s', end=None, label=None):
    _end, _unit = "", ""
    if unit == 's':
        _end, _unit = end, 'seconds'
    elif unit == 'm':
        _end, _unit = end / 60, 'minutes'
    elif unit == 'h':
        _end, _unit = end / 3600, 'hours'
    print(_green('Total time running {}: {} {}'.format(label, _end, _unit)))


@contextmanager
def timeit_block(unit='s', label=""):
    """
    测试代码块耗时

    :param unit: 时间单位，有 's','m','h' 可选（seconds，minutes，hours）
    :param label: 代码块标签
    """
    start = time.time()
    try:
        yield
    finally:
        _format(unit, time.time() - start, label)


def timeit(unit='s'):
    """
    测试函数耗时

    :param unit: 时间单位，有 's','m','h' 可选（seconds，minutes，hours）
    """
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            start = time.time()
            _result = func(*args, **kwargs)
            _format(unit, time.time() - start, func.__name__ + '()')
            return _result
        return inner
    return wrapper
