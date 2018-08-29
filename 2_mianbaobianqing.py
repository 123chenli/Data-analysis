import pandas as pd
import numpy as np

bread = pd.read_csv('datas/bread.csv', encoding='utf-8')
bread.head()
# 计算面包的均差和标准差
mean = round(np.mean(bread.weight), 4)
std = round(np.std(bread.weight), 4)
import sys

sys.stdout.write('mean = ' + str(mean) + '\n' + 'std = ' + str(std) + '\n')


# 均值差异检验
from scipy.stats import ttest_rel
print(ttest_rel(bread.weight, [400]*30))