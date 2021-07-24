# 案例1演示温度
# 是python的一个绘图库，仿照了matlab
#
# 假设一天每个两个小时的气温分别是
# （range(2,26,2)）
#  [15,13,14.5,17,20,25,26,26,27,22,18,15]
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.font_manager import FontProperties #字体管理器
font = FontProperties(fname="c:\\windows\\fonts\\simsun.ttc", size=15)
np.random.seed(19680801)
x = range(0,24,1);
y = [15,13,14.5,17,20,25,26,26,27,22,18,15,15,13,14.5,17,20,25,26,26,27,22,18,15]
plt.plot(np.random.rand(20),x,y);
plt.title("一天每个两个小时的气温",fontproperties=font)
plt.xlabel('时间',fontproperties=font)
plt.ylabel('温度',fontproperties=font)
plt.show()