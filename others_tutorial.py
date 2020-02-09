import sys

choose = 5

# 迭代器
if choose == 1:
    # Python3 range() 函数返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表。
    x1 = range(10)  # range(0, 10)
    # Python3 list() 函数是对象迭代器，可以把range()返回的可迭代对象转为一个列表，返回的变量类型为列表。
    x2 = list(x1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    x3 = list(range(1, 10))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # \反斜杠，在windows系统中用来表示目录，在Unix系统中表示转义字符
    print(x1, "\n", x2, "\n", x3)

    # iter()：用来生成迭代器，输入为支持迭代的集合对象，输出为迭代器对象
    x4 = iter(x1)
    # next()：输出迭代器的下一个元素
    x5 = next(x4)
    x6 = next(x4)
    print(x4, "\n", x5, "\n", x6)

    # # 迭代器
    # x = [2, 4, 6]
    # y = enumerate(x)
    #
    # for n in x:
    #     print(n)
    #
    # # 每次次迭代都会返回一组 (index, value) 组成的元组
    # for (i, n) in y:
    #     print('pos', i, 'is', n)
    #
    # # 迭代器对象必须实现 __iter__ 方法
    # i = x.__iter__()
    # # __iter__() 返回的对象支持 next 方法，返回迭代器中的下一个元素
    # print(next(i))
    # print(next(i))

# 生成器
elif choose == 2:
    """使用了 yield 的函数被称为生成器。
    生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
    函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
    在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值，
    并在下一次执行 next() 方法时从当上次返回的yield语句处继续执行。"""

    def fibonacci(n):  # 生成器函数 - 斐波那契
        a, b, counter = 0, 1, 0
        while True:
            if counter > n:
                return
            yield a
            a, b = b, a + b
            counter += 1


    f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
    while True:
        try:
            print(next(f), end=" ")
        except StopIteration:
            sys.exit()

# 断言
elif choose == 3:
    """Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
    断言可以在条件不满足程序运行的情况下直接返回错误，而不必等待程序运行后出现崩溃的情况，
    例如我们的代码只能在 Linux 系统下运行，可以先判断当前系统是否符合条件。"""
    assert True
    assert 1 == 2, '1 不等于 2'

# 异常
elif choose == 4:
    try:
        # 尝试执行的代码
        pass
    except 错误类型1:
        # 针对错误类型1，对应的代码处理
        pass
    except 错误类型2:
        # 针对错误类型2，对应的代码处理
        pass
    except (错误类型3, 错误类型4):
        # 针对错误类型3 和 4，对应的代码处理
        pass
    except Exception as result:
        # 打印错误信息
        print(result)
    else:
        # 没有异常才会执行的代码
        pass
    finally:
        # 无论是否有异常，都会执行的代码
        print("无论是否有异常，都会执行的代码")

# 抛出异常
elif choose == 5:

    def input_password():
        # 1. 提示用户输入密码
        pwd = input("请输入密码：")
        # 2. 判断密码长度，如果长度 >= 8，返回用户输入的密码
        if len(pwd) >= 8:
            return pwd
        # 3. 密码长度不够，需要抛出异常
        # 1> 创建异常对象 - 使用异常的错误信息字符串作为参数
        ex = Exception("密码长度不够")
        # 2> 抛出异常对象
        raise ex


    try:
        user_pwd = input_password()
        print(user_pwd)
    except Exception as result:
        print("发现错误：%s" % result)
