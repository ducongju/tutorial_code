#! /usr/bin/env	python3
# encoding=UTF-8
# from __future__ import print_function

import sys
import os
import csv
import re
import datetime as dt
import pickle
import json
from pprint import pprint
import logging
import math

choose = 2

# sys模块: 程序与python解释器的交互
if choose == 1:
    """sys模块提供对解释器使用或维护的一些变量的访问，以及与解释器强烈交互的函数。"""
    # 显示传入的参数
    print(sys.argv)
    # 表示 Python 搜索模块的路径和查找顺序
    """
    python中import某个A模块时
    首先会从python的内置模块中查找是否含义该模块的定义，
    若未查询到会从sys.path对应的模块路径查询是否含有对应模块的定义，
    如果搜索完成依然没有对应A模块时则抛出import的异常。
    
    sys.path[0]是当前脚本的运行目录
    python xxx.py: sys.path[0]是存放需要运行的代码的路径。
    python -m xxx.py: sys.path[0]是空值字符串，它引导Python首先在当前目录中搜索模块。

    在实际开发中，默认包含了当前目录为搜索路径，所以，当前目录下的模块和子模块均可以正常访问。
    但是若一个模块需要import平级的不同目录的模块，或者上级目录里面的模块，就可以通过修改path来实现，修改path的两种方法:
    方法一：函数添加
    这是即时生效的方法，就是在模块里面修改sys.path值，这种方法修改的sys.path作用域只是当前进程，进程结束后就失效了。
    方法二：修改环境变量
    添加系统环境变量PYTHONPATH，在这个环境变量中输入相关的路径，不同的路径之间用逗号（英文的！)分开。路径会自动加入到sys.path中。
    """
    pprint(sys.path)
    # 显示当前操作系统信息
    print(sys.platform)
    # 显示 python 版本
    print(sys.version)

    try:
        x = 1 / 0
    # 可以显示 Exception 的信息，返回一个 (type, value, traceback) 组成的三元组
    except Exception:
        print(sys.exc_info())

# os模块: 程序与操作系统的交互
elif choose == 2:
    """提供了非常丰富的方法用来处理文件和目录"""
    # 当前目录
    print(os.getcwd())
    # 当前目录下的文件
    print(os.listdir(os.curdir))
    # 返回绝对路径
    print(os.path.abspath('tutorial_code'))

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

    # 去掉文件名，返回目录
    print(os.path.dirname('W:\Python_File\juan之购物车.py'))
    print(os.path.dirname('W:\Python_File'))

# csv模块
elif choose == 3:
    """CSV（逗号分隔符）文件是表格与数据库操作之中最常用的输入输出格式"""
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

# re模块: 正则表达式
elif choose == 4:
    """正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符、及这些特定字符的组合，组成一个“规则字符串”，
    这个“规则字符串”用来表达对字符串的一种过滤逻辑。"""
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

# datetime模块: 处理日期和时间
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

# pickle模块：序列化Python对象
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
    with open("data.pkl", "rb") as f:
        data_from_file = pickle.load(f)
        print(data_from_file)

# pprint模块：打印Python对象
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


# json模块: 处理JSON数据
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
    with open("info.json", "w") as f:
        json.dump(info, f)

    # 从 JSON 文件中读取数据
    with open("info.json") as f:
        pprint(json.load(f))

# logging模块: 输出运行日志
elif choose == 9:
    """日志是一种可以追踪某些软件运行时所发生事件的方法。软件开发人员可以向他们的代码中调用日志记录相关的方法来表明发生了某些事情。
    我们通过记录和分析日志可以了解一个系统或软件程序运行情况是否正常，也可以在应用程序出现故障时快速定位问题。"""
    # 用 logging.basicConfig()函数调整日志级别、输出格式等
    # 日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s %(name)s %(levelname)s %(message)s",
                        datefmt='%Y-%m-%d  %H:%M:%S %a'  # 注意月份和天数不要搞乱了，这里的格式化符与time模块相同
                        )
    logging.debug("debug_msg")
    logging.info("info_msg")
    logging.warning("warning_msg")
    logging.error("error_msg")
    logging.critical("critical_msg")

# math模块
elif choose == 10:
    pprint(dir(math))
    print(math.floor(1.3))  # 向下取整
    print(math.ceil(1.3))  # 向上取整
    print(round(1.3))  # 四舍五入
