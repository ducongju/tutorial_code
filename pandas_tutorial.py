"""pandas 是基于NumPy 的一种工具，该工具是为了解决数据分析任务而创建的。
Pandas 纳入了大量库和一些标准的数据模型，提供了高效地操作大型数据集所需的工具。
pandas提供了大量能使我们快速便捷地处理数据的函数和方法。"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

choose = 2

if choose == 1:
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s)

elif choose == 2:
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df)