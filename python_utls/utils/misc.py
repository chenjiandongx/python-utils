#!/usr/bin/env python
# coding=utf-8

import os


def format_cookies(path):
    """
    将 cookie 字符串转化为字典

    :param path: cookies 文件路径
    :return: cookies 字典
    """
    with open(path, 'r') as f:
        _cookies = {}
        for row in f.read().split(';'):
            k, v = row.strip().split('=', 1)
            _cookies[k] = v
        return _cookies


def delete_empty_dir(directory):
    """
    删除空目录

    :param directory: 目录路径
    """
    if os.path.exists(directory):
        if os.path.isdir(directory):
            for d in os.listdir(directory):
                path = os.path.join(directory, d)
                if os.path.isdir(path):
                    delete_empty_dir(path)

        if not os.listdir(directory):
            os.rmdir(directory)
            print("Remove the empty directory: " + directory)
    else:
        print("The directory is not exist!")
