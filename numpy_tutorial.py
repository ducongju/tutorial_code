import numpy as np

choose = 1

# 数组方法
if choose == 1:
    # 使用列表生成一个一维数组
    # ndarray与Python列表的最大的不同就是列表可以存入不同数据类型的元素，而ndarray要求所有元素的数据类型必须一致。
    # Numpy会自动识别ndarray中的数据类型，如果数据类型不一致Numpy会将所有元素自动转换成一个合适的数据类型。
    data = [1+1j,
            2,
            3,
            4,
            5]
    # 列表list对象转换为n维数组ndarray对象
    x = np.array(data)

    print(x)            # [1.+1.j 2.+0.j 3.+0.j 4.+0.j 5.+0.j]
    # 查看数组中的数据类型
    print(x.dtype)      # complex128
    # 打印数据结构类型
    print(type(x))      # <class 'numpy.ndarray'>
    # 查看每个元素所占的字节
    print(x.itemsize)   # 16
    # 查看形状，会返回一个元组，每个元素代表这一维的元素数目
    print(x.shape)      # (5,)
    # 查看元素数目
    print(x.size)       # 5
    # 查看它的实部和虚部，复共轭
    print(x.real)       # [1. 2. 3. 4. 5.]
    print(x.imag)       # [1. 0. 0. 0. 0.]
    print(x.conj())     # [1.-1.j 2.-0.j 3.-0.j 4.-0.j 5.-0.j]
    # 切片中使用m:n的形式，表示[m, n)的半开半闭的范围。
    print(x[1:3])       # [2.+0.j 3.+0.j]

elif choose == 2:
    data = (1, 2, 3, 4, 5)
    x = np.array(data)
    print(x)
    print(x.dtype)
    print(type(x))

elif choose == 3:
    # 使用列表生成一个二维数组
    data = [[1, 2],
            [3, 4],
            [5, 6]]
    x = np.array(data)

    print(x)
    # 打印数组维度
    print(x.ndim)       # 2
    # 打印数组各个维度的长度
    print(x.shape)      # (3, 2)

# 数组生成
elif choose == 4:
    # 使用zeros创建一个长度为4， 元素为0的一维数组
    x1 = np.zeros(4)
    print(x1)            # [0. 0. 0. 0.]
    # 创建一个二维数组， 一维长度为2， 二维长度为3， 元素为0的数组
    x2 = np.zeros((2, 3))
    print(x2)            # [[0. 0. 0.] [0. 0. 0.]]
    # 使用ones创建一个二维数组， 一维长度为2， 二维长度为3， 元素为1的数组
    x3 = np.ones((2, 3))
    print(x3)            # [[1. 1. 1.] [1. 1. 1.]]
    # 使用empty创建一个二维数组， 一维长度为3， 二维长度为3， 元素为初始化的数组
    x4 = np.empty((3, 3))
    print(x4)            # [[ 6.23042070e-307  1.95564605e+093  3.01926635e+121]
                        #  [ 6.30749269e-307 -2.24792301e-252  1.78021798e-306]
                        #  [ 7.56596412e-307  1.37961302e-306  1.41695307e+241]]
    # 使用arange生成连续元素
    x5 = np.arange(5)
    print(x5)            # [0 1 2 3 4]
    x6 = np.arange(1, 5, 2)
    print(x6)            # [1 3]

elif choose == 5:
    x = np.array([1, 2, 3, 4])
    x.shape = (2, 2)
    y = x + x
    z = x ** x

elif choose == 6:
    x = np.array([0, 12, 5, 20])
    # 判断数组中的元素是不是大于10
    print(x > 10)
    # 数组中所有大于10的元素的索引位置
    print(np.where(x > 10))
    # Numpy 有两种基本对象：ndarray (N-dimensional array object) 和 ufunc (universal function object)。
    # ndarray 是存储单一数据类型的多维数组，而 ufunc 则是能够对数组进行处理的函数。
    a = np.array([0, 1, 2])
    b = np.array([2, 3, 4])
    print(np.add(a, b))

input('Press Enter to exit...')