## [misc.py](https://github.com/chenjiandongx/python-utils/blob/master/utils/misc.py)

> 各种杂项工具函数

### format_cookies
> format_cookies(path)

*将 cookie 字符串转化为字典*

* path: cookies 文件路径，纯文本文件即可。
* return: cookies 字典

用法
```python
from python_utils import misc

misc.format_cookies()
```


### delete_empty_dir
> delete_empty_dir(directory)

*遍历删除空目录*

* directory: 目录路径

用法
```python
from python_utils import misc

misc.delete_empty_dir()
```