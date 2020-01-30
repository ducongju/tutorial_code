from __future__ import print_function         # 即使在python2.X，使用print就得像python3.X那样加括号使用
import torch

x = torch.empty(3, 3, 3)                      # torch.empty: 创建一个未初始化矩阵
print(x)

x = torch.rand(3, 3)                          # torch.rand：创建一个随机初始化矩阵
print(x)

x = torch.zeros(3, 3, dtype=torch.long)       # torch.zeros：创建一个0填充的矩阵，数据类型为long
print(x)

x = torch.tensor([5, 3])                      # torch.tensor：创建tensor并使用现有数据初始化
print(x)

x = x.new_ones(3, 3, dtype=torch.float32)      # x.new_*：根据现有的张量创建张量
print(x)

y = torch.ones(3, 3)
print(x + y)                                  # 加法1
print(torch.add(x, y))                        # 加法2

x = torch.rand(3, 3, 3)                       # 使用size方法与Numpy的shape属性返回的相同，张量也支持shape属性
size1 = x.size()
size2 = size1[1:]
print(size1, size2)                           # torch.Size返回值是tuple类型, 所以它支持tuple类型的所有操作

num_features = 1
for s in size1:                               # for ... in，遍历元组中所有数据
    num_features *= s
print(num_features)
