# 创建数组
import numpy as np;
a = np.array([1,2,3,4,5])
print(a)
print(type(a))

b=np.array([[1,2,3],[4,5,6]])
print(b)
#ndim 数组的维数
#  a 是一维数组
#  b 是二维数组
print(a.ndim)
print(b.ndim)

#  a shape
print(a.shape)
print(b.shape)
c = np.array([[1.0,2,3],[4,5,5]])
print(c.shape)

# dtype
print(a.dtype)
print(c.dtype)