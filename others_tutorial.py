import sys

choose = 1

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

