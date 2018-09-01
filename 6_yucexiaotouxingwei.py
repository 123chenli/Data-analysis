# 失窃额线型图
import pandas as pd
xiaotailang = pd.read_csv('datas/xiaotailang.csv', encoding='utf-8')
print(xiaotailang.head(10))
xiaotailang.date = pd.to_datetime(xiaotailang.date)
import matplotlib.pylab as plt
import pylab
plt.rcParams['font.sans-serif'] = ['SimHei']
xiaotailang.index = xiaotailang.iloc[:, 2]
xiaotailang.iloc[:, 0].plot()
plt.ylabel('数额')
plt.title('失窃数据')
pylab.show()

# 绘制14年10月份数据的线型图
xiaotailang.iloc[0:30, 0].plot()
plt.ylabel('数额')
plt.title('10月份失窃数额')
pylab.show()

# 将列虚拟化
xiaotailang.iloc[:, 3] = xiaotailang.iloc[:, 3].replace(['no', 'yes'], [1, 0])
day = pd.get_dummies(xiaotailang['周几'])
xiaotailang = xiaotailang.iloc[:, 0:4].join(day) # 整合数据
xiaotailang.iloc[:, 4:] = xiaotailang.iloc[:, 4:].replace([0, 1], [1, 0])
print(xiaotailang.head())

# 逻辑回归
import statsmodels.api as sm
logit = sm.Logit(xiaotailang.iloc[:, 1], xiaotailang.iloc[:, 3: 10])
# 拟合模型
result = logit.fit()
print(result.summary())