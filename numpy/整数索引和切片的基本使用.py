# 整数索引和切片的基本使用
# 
import numpy as np
arr = np.arange(2,8)
print(arr[0])
# 切片

print(arr[0:3]) 

#  定义函数
def runTime():
    for (i) in range(2,10):
        print(i)
runTime()

def runTime2():
    return np.arange(9).reshape((3,3))

arr2 = runTime2();
print(arr2)
print(arr2[1,1])

# 多维数组的索引和切片的使用

demo_arr = np.empty((4,4))
print(demo_arr)
for i in range(4):
    demo_arr[i]=np.arange(i,i+4)
#获取索引为[0,2]的元素
print(demo_arr[0:2,:2])


arr = np.arange(16)
# 修改数据的形状
new_arr = arr.reshape((4,4))
print(new_arr)
print(new_arr.T)
print("-----")
new_arr = arr.reshape((2,2,4))
print(new_arr)
print(new_arr.transpose().shape)

#swapaxes  new_arr  2 2 4  指定轴转换

data = np.random.uniform(4)
print(data)

