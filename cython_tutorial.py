"""使用 Python 和另一种语言混编的好处
至少有以下四个原因：
Best of both worlds - 结合两种语言的优点：已经优化和测试过的代码库 + Python 的灵活
Python as glue - Python 作为连接的桥梁，将很多其他语言的模块结合到一个大型程序中
Speed up Python - 使用一个更快的语言帮助加速 Python
Division of labor - 各司其职，让各个语言做各自更擅长的事情"""

# Cython 的好处在于，我们使用了 Python 的语法，又有 C/C++ 的效率，
# 同时省去了之前直接编译成扩展模块的麻烦，并且提供了原生的 Numpy 支持。

import cython



