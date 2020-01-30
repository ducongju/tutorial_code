#! /usr/bin/env	python3
#encoding=UTF-8
# from __future__ import print_function

import sys
import os
import csv
import re
import datetime as dt
import json
from pprint import pprint

try:
    import cPickle as pickle
except:
    import pickle

choose = 8

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

# pickle, cPickle 模块：序列化 Python 对象
elif choose == 6:
    """pickle 模块实现了一种算法，可以将任意一个 Python 对象转化为一系列的字节，也可以将这些字节重构为一个有相同特征的新对象。
    由于字节可以被传输或者存储，因此 pickle 事实上实现了传递或者保存 Python 对象的功能。
    cPickle 使用 C 而不是 Python 实现了相同的算法，因此速度上要比 pickle 快一些。但是它不允许用户从 pickle 派生子类。
    如果子类对你的使用来说无关紧要，那么 cPickle 是个更好的选择。"""
    data = [{'a': 'A', 'b': 2, 'c': 3.0}]
    data_string = pickle.dumps(data)
    data_from_string = pickle.loads(data_string)

    # 将对象存入文件
    with open("data.pkl", "wb") as f:
        pickle.dump(data, f)

    # 从文件中读取
    with open("data.pkl","rb") as f:
        data_from_file = pickle.load(f)
        print(data_from_file)

# pprint 模块：打印 Python 对象
elif choose == 7:
    """pprint 是 pretty printer 的缩写，用来打印 Python 数据结构，与 print 相比，它打印出来的结构更加整齐，便于阅读。"""
    data = (
        "this is a string",
        [1, 2, 3, 4],
        ("more tuples", 1.0, 2.3, 4.5),
        "this is yet another string"
    )
    print(data)
    pprint(data)


# json 模块：处理 JSON 数据
elif choose == 8:
    """JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式，易于人阅读和编写，同时也易于机器解析和生成。"""
    # 将 JSON 对象写入了一个字符串
    info_string = """
    {
        "name": "echo",
        "age": 24,
        "coding skills": ["python", "matlab", "java", "c", "c++", "ruby", "scala"],
        "ages for school": { 
            "primary school": 6,
            "middle school": 9,
            "high school": 15,
            "university": 18
        },
        "hobby": ["sports", "reading"],
        "married": false
    }
    """

    # 用 json.loads() (load string) 方法从字符串中读取 JSON 数据
    # 此时，我们将原来的 JSON 数据变成了一个 Python 对象，在我们的例子中这个对象是个字典（也可能是别的类型，比如列表）
    info = json.loads(info_string)
    # pprint(info_string)
    # pprint(info)
    # print(type(info))

    # 使用 json.dumps() 将一个 Python 对象变成 JSON 对象
    info_json = json.dumps(info)
    # pprint(info_json)

    # 与 pickle 类似，我们可以直接从文件中读取 JSON 数据，也可以将对象保存为 JSON 格式
    # 将对象保存为 JSON 格式的文件
    with open("info.json","w") as f:
        json.dump(info, f)

    # 从 JSON 文件中读取数据
    with open("info.json") as f:
        pprint(json.load(f))
