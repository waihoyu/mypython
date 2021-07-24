# 
import numpy as np;
a = np.zeros((2,3))
print(a)
b = np.ones((2,3))
print(b)
c=np.empty((2,3))
print(c)

d = np.arange(1,20,10)
print(d)
print(d.dtype.name)

f = np.ones((2,3),dtype="int32")
print(f)

e = np.array(["numpy","pandas","scipy","tensorflow"],dtype="string_")
print(e)