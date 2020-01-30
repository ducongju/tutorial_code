"""Ipython 提供了一个很好的解释器界面。
Matplotlib 提供了一个类似 Matlab 的画图工具。
Numpy 提供了 ndarray 对象，可以进行快速的向量化计算。
Scipy 是 Python 中进行科学计算的一个第三方库，以 Numpy 为基础。
Pandas 是处理时间序列数据的第三方库，提供一个类似 R 语言的环境。
StatsModels 是一个统计库，着重于统计模型。
Scikits 以 Scipy 为基础，提供如 scikits-learn 机器学习和scikits-image 图像处理等高级用法。"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg, optimize
from scipy.interpolate import interp1d
from scipy.stats import norm

choose = 2

if choose == 1:
    # np.info(optimize.fmin)
    np.lookfor("resize", module="numpy")

elif choose == 2:
    x_norm = norm.rvs(size=500)
    print(type(x_norm))
    h = plt.hist(x_norm)
    print('counts, ', h[0])
    print('bin centers', h[1])
