import pandas as pd
from collections import Counter

choujiang = pd.Series(['未中奖', '一等奖'])
cnt = Counter(choujiang.sample(n=100, replace=True, weights=[99, 1]))
# print(cnt)

# 模拟1000周的中将情况
import numpy as np

a = np.zeros(1000)
for i in range(1000):
    for j in range(7):
        a[i] = np.sum(choujiang.sample(n=100,
                                       replace=True,
                                       weights=([99, 1]))
                      == '一等奖') + a[i]

# 画出直方图
import pylab
pylab.hist(a, bins=18, normed=0, edgecolor='black', facecolor='blue', alpha=0.75)
pylab.show()
print(np.transpose(Counter(a)))