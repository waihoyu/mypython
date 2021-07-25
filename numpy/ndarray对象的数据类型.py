# ndarray对象的数据类型
import numpy as np;
a = np.array((2,2,3,4))
print(a)
b=np.array(([1,2],[1,2]))
print(b)
c=np.array([2,3,4,5])
print(c)
d=np.array([(1,2),(3,4)])
print(d)
e=np.array(((8,8,8),(9,9,9)))
print(e)
f=np.array(([88,99],[77,66]))
print(f)
print(f.dtype.name)
g=np.zeros((2,3),dtype="int64")
print(g)
print(g.dtype.name)

