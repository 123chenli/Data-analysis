# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
#X轴，Y轴数据
x = [13, 9, 5]
y = [13.0, 13.2, 18.5]
plt.figure(figsize=(8,4)) #创建绘图对象
plt.plot(x,y,"b--",linewidth=1)   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
plt.ylabel("平均误匹配率%")  #Y轴标签
plt.xlabel('窗口大小')
plt.title("Teddy深度不连续区域") #图标题
plt.show()  #显示图
plt.savefig("line.jpg") #保存图