# coding: utf-8
import pylab
import matplotlib.pylab as plt
import pandas as pd
from pylab import *

# 画出3个月的饭团销售额时间序列图
menus = pd.read_csv('datas/menus.csv', encoding='utf-8')
menus.日期 = pd.to_datetime(menus.日期)
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示问题
menus.index = menus.iloc[:, 1]
menus.loc[menus.品名 == '饭团'].iloc[:, 2].plot()
plt.ylabel('销售额')
pylab.show()

# 画出炒饭的销售额时间序列图
menus.loc[menus.品名 == '炒饭'].iloc[:, 2].plot()
plt.ylabel('销售额')
pylab.show()

# 面类的销售情况
menus.loc[menus.品名 == '意大利面'].iloc[:, 2].plot(label='意大利面')
menus.loc[menus.品名 == '酱汁炒面'].iloc[:, 2].plot(label='酱汁炒面')
menus.loc[menus.品名 == '乌冬面'].iloc[:, 2].plot(label='乌冬面')
menus.loc[menus.品名 == '什锦面'].iloc[:, 2].plot(label='什锦面')
menus.loc[menus.品名 == '拉面'].iloc[:, 2].plot(label='拉面')
plt.ylabel('销售额')
plt.legend()
pylab.show()

# 牛奶和饭团的散点图
plt.scatter(menus.loc[menus.品名 == '饭团'].iloc[:, 2],
            menus.loc[menus.品名 == '牛奶'].iloc[:, 2])
plt.xlabel("牛奶")
plt.ylabel('饭团')
pylab.show()

# 牛奶的销售情况
menus.loc[menus.品名 == '牛奶'].iloc[:, 2].plot()
plt.ylabel("销售额")
pylab.show()

# 计算牛奶和饭团销售额的相关系数
a = menus.loc[menus.品名 == '牛奶'].iloc[:, 2]
b = menus.loc[menus.品名 == '饭团'].iloc[:, 2]
c = pd.concat([a, b], axis=1)
c.columns = ['牛奶', '饭团']
print(c.corr())