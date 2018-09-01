# 聚类分析
import pandas as pd
reviewsdata = pd.read_csv('datas/reviewsdata.csv', index_col=0)
print(reviewsdata.head(10))
# 对数据进行聚类分析，并画出聚类树形图
import scipy
import scipy.cluster.hierarchy as sch
import matplotlib.pylab as plt
import pylab
# 生成点与点之间的欧式距离
disMat = sch.distance.pdist(reviewsdata.T, 'euclidean')
# 层次聚类
Z = sch.linkage(disMat, method='average')
# 将层次聚类结果以树状图表示出来并保存plot_dendrogram.png
sch.dendrogram(Z, labels=reviewsdata.columns,
               leaf_font_size=7.5)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('口碑的聚类')
pylab.show()