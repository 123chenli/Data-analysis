import pandas as pd
import matplotlib.pylab as plt
from pylab import *

# 导入数据
survey = pd.read_csv('datas/survey.csv', encoding='utf-8')
# 计算店主和顾客对商业街魅力的支持情况
su1 = pd.DataFrame({'顾客': survey[survey.立场 == '顾客'].回答6.value_counts()})
su2 = pd.DataFrame({'店主': survey[survey.立场 == '店主'].回答6.value_counts()})
# 合并数据框，生成列联表
survey2 = pd.concat([su1, su2], axis=1)
print(survey2)

# 绘制柱状图
mpl.rcParams['font.sans-serif'] = ['SimHei']
survey2.T.plot(kind='bar',
               stacked=True,
               color=['black', 'gold', 'red', 'green'],
               grid=False)
plt.show()

# 独立性检验
from scipy.stats import chi2_contingency
print(chi2_contingency(survey2))