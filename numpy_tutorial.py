import numpy as np

choose = 5

# 数组方法
if choose == 1:
    # 使用列表生成一个一维数组
    # ndarray与Python列表的最大的不同就是列表可以存入不同数据类型的元素，而ndarray要求所有元素的数据类型必须一致。
    # Numpy会自动识别ndarray中的数据类型，如果数据类型不一致Numpy会将所有元素自动转换成一个合适的数据类型。
    data = [1 + 1j,
            2,
            3,
            4,
            5]
    print(data)
    # 列表list对象转换为n维数组ndarray对象
    x = np.array(data) # [1.+1.j 2.+0.j 3.+0.j 4.+0.j 5.+0.j]
    # list输出有逗号, ndarray输出没有逗号
    print(x)
    # 查看数组中的数据类型
    print(x.dtype)  # complex128
    # 打印数据结构类型
    print(type(x))  # <class 'numpy.ndarray'>
    # 查看每个元素所占的字节
    print(x.itemsize)  # 16
    # 查看形状，会返回一个元组，每个元素代表这一维的元素数目
    print(x.shape)  # (5,)
    # 查看元素数目
    print(x.size)  # 5
    # 查看它的实部和虚部，复共轭
    print(x.real)  # [1. 2. 3. 4. 5.]
    print(x.imag)  # [1. 0. 0. 0. 0.]
    print(x.conj())  # [1.-1.j 2.-0.j 3.-0.j 4.-0.j 5.-0.j]
    # 切片中使用m:n的形式，表示[m, n)的半开半闭的范围。
    print(x[1:3])  # [2.+0.j 3.+0.j]
    # 转换数据结构类型
    y = x.astype(np.complex64)

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

    x1 = x.ndim
    x2 = x.shape
    x3 = x.size
    x4 = len(x)

# 数组生成
elif choose == 4:
    # 使用zeros创建一个长度为4， 元素为0的一维数组
    x1 = np.zeros(4)
    print(x1)  # [0. 0. 0. 0.]
    # 创建一个二维数组， 一维长度为2， 二维长度为3， 元素为0的数组
    x2 = np.zeros((2, 3))
    print(x2)  # [[0. 0. 0.] [0. 0. 0.]]
    # 使用ones创建一个二维数组， 一维长度为2， 二维长度为3， 元素为1的数组
    x3 = np.ones((2, 3))
    print(x3)  # [[1. 1. 1.] [1. 1. 1.]]
    # 使用empty创建一个二维数组， 一维长度为3， 二维长度为3， 元素为初始化的数组
    x4 = np.empty((3, 3))
    print(x4)
    """
    [[ 6.23042070e-307  1.95564605e+093  3.01926635e+121]
     [ 6.30749269e-307 -2.24792301e-252  1.78021798e-306]
     [ 7.56596412e-307  1.37961302e-306  1.41695307e+241]]
    """
    # 使用arange生成连续元素
    x5 = np.arange(5)
    print(x5)  # [0 1 2 3 4]
    x6 = np.arange(1, 5, 2)
    print(x6)  # [1 3]

# 数组运算
elif choose == 5:
    # Numpy 有两种基本对象：ndarray (N-dimensional array object) 和 ufunc (universal function object)。
    # ndarray 是存储单一数据类型的多维数组，而 ufunc 则是能够对数组进行处理的函数。
    x = np.array([1, 2, 4, 3])
    x.shape = (2, 2)  # [[1, 2], [4, 3]]
    y1 = x + x
    y2 = x ** x
    y3 = np.add(x, x)
    y4 = np.argmax(x, 0)  # [1, 1]
    y5 = np.argmax(x, 1)  # [1, 0]
    y6 = np.amax(x, 0)  # [4, 3]
    y7 = np.amax(x, 1)  # [2, 4]
    y8 = np.tile(x, (1, 2))  # [[1, 2, 1, 2], [4, 3, 4, 3]]  相当于matlab的repmat
    y9 = np.greater([1, 2, 3], 2)  # [False, False, True]
    y10 = np.sign(x)  # [[1, 1], [1, 1]]
    y11 = np.multiply(np.ones((2958)), np.ones((16, 1)))

# 数组操作
elif choose == 6:
    x = np.array([0, 12, 5, 20])
    # 判断数组中的元素是不是大于10, 返回{ndarray: (4,)}
    y1 = x > 10
    # 数组中所有大于10的元素的索引位置, 返回{tuple: 1}
    y2 = np.where(x > 10)
    # 返回一个复制
    y3 = x.copy()
    # 索引
    y4 = (y1, y2, y3)
    y5 = y4[0][1]
    # 切片
    """
    一个完整的切片表达式包含两个“:”，用于分隔三个参数(start_index、end_index、step)。
    当只有一个“:”时，默认第三个参数step=1；
    当一个“:”也没有时，start_index=end_index，表示切取start_index指定的那个元素。
    """
    # 取最后一个元素
    z1 = x[-1]
    # 取除最后一个元素以外的所有元素
    z21 = x[:-1]
    z22 = x[0:-1]
    # 取从后向前（相反）的元素
    z31 = x[::-1]
    z32 = x[-1::-1]
    # 取所有元素
    z41 = x[:]
    z42 = x[::]


# input('Press Enter to exit...')
