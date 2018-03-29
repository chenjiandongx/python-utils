#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages


__title__ = 'pyut'
__description__ = 'Python Utilities Methods'
__url__ = 'https://github.com/chenjiandongx/python-utils'
__author_email__ = 'chenjiandongx@qq.com'
__license__ = 'MIT'
__version__ = '0.0.1'

__requires__ = []
__keywords__ = ['python', 'utilities']

setup(
    name=__title__,
    version=__version__,
    description=__description__,
    url=__url__,
    author='__author__',
    author_email=__author_email__,
    license=__license__,
    packages=find_packages(exclude=('test',)),
    keywords=__keywords__,
    install_requires=__requires__,
    # zip_safe=False,
    # include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ]
)