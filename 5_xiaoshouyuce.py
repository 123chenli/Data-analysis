import pandas as pd
import matplotlib.pylab as plt
import pylab

icecream = pd.read_csv('datas/icecream.csv', encoding='utf-8')
plt.rcParams['font.sans-serif'] = ['SemHei']
plt.scatter(icecream.iloc[:, 1],
            icecream.iloc[:, 0])
plt.xlabel('气温')
plt.ylabel('销售量')
pylab.show()

# 计算两者之间的相关系数
print(icecream.iloc[:, 0:2].corr())

# 回归分析
from sklearn.linear_model import LinearRegression
model = LinearRegression()
feature_cols = ['气温']
X = icecream[feature_cols]
y = icecream.销售量
model.fit(X, y)
plt.scatter(icecream.气温, icecream.销售量)
plt.plot(icecream.气温, model.predict(X), color='blue')
plt.xlabel('气温')
plt.ylabel('销售量')
plt.show()
print('截距与斜率为：', model.intercept_, model.coef_)