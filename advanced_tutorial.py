#! /usr/bin/env	python3
#encoding=UTF-8
# from __future__ import print_function

import sys
import os
import csv
import re
import datetime as dt

choose = 6

# sys模块
if choose == 1:
    # 显示传入的参数
    print(sys.argv)
    # 表示 Python 搜索模块的路径和查找顺序
    print(sys.path)
    # 显示当前操作系统信息
    print(sys.platform)
    # 显示 python 版本
    print(sys.version)

    try:
        x = 1 / 0
    # 可以显示 Exception 的信息，返回一个 (type, value, traceback) 组成的三元组
    except Exception:
        print(sys.exc_info())

# os模块
elif choose == 2:
    # 当前目录
    print(os.getcwd())
    # 当前目录下的文件
    print(os.listdir(os.curdir))

    # 产生文件
    f = open("test.file", "w")
    f.close()
    print("test.file" in os.listdir(os.curdir))

    # 重命名文件
    os.rename("test.file", "test.new.file")
    print("test.file" in os.listdir(os.curdir))
    print("test.new.file" in os.listdir(os.curdir))

    # 删除文件
    os.remove("test.new.file")

# csv模块
elif choose == 3:
    # 打开这个文件，并产生一个文件 reader
    fp = open("data.csv")
    r = csv.reader(fp)

    # 可以按行迭代数据
    for row in r:
        print(row)

    fp.close()

    # 写csv文件
    data = [('one', 1, 1.5), ('two', 2, 8.0)]
    with open('out.csv', 'w') as fp:
        w = csv.writer(fp)
        w.writerows(data)

# re模块
elif choose == 4:
    string = 'hello world'
    pattern = 'hello (\w+)'

    # 成功则返回一个 match 对象，不成功则返回 None
    match = re.match(pattern, string)
    print(match)

    # 一旦找到了符合条件的部分，我们便可以使用 group 方法查看匹配的部分
    # 通常，match.group(0) 匹配整个返回的内容，之后的 1,2,3,... 返回规则中每个括号（按照括号的位置排序）匹配的部分。
    if match is not None:
        print(match.group(0))
        print(match.group(1))

# datetime模块
elif choose == 5:
    # 可以使用 date(year, month, day) 产生一个 date 对象
    d1 = dt.date(2007, 9, 25)
    d2 = dt.date(2008, 9, 25)
    # 可以格式化 date 对象的输出
    print(d1)
    print(d1.strftime('%A, %m/%d/%y'))
    print(d1.strftime('%a, %m-%d-%Y'))
    # 可以看两个日期相差多久
    dch = d2 - d1
    print(dch)

# 迭代器
elif choose == 6:
    x = [2, 4, 6]
    y = enumerate(x)

    for n in x:
        print(n)

    # 每次次迭代都会返回一组 (index, value) 组成的元组
    for (i, n) in y:
        print('pos', i, 'is', n)

    # 迭代器对象必须实现 __iter__ 方法
    i = x.__iter__()
    # __iter__() 返回的对象支持 next 方法，返回迭代器中的下一个元素
    print(next(i))
    print(next(i))