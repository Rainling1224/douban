# -*- coding: utf-8 -*-
"""
Created on Tue May 25 12:29:09 2021

@author: 13397
"""
#百度情感分析统计
import pandas as pd
from collections import Counter

#读取cv文件
df=pd.read_csv('cpbaidu.csv')

#统计打分数量
recommend_list=df['contentsenti'].values.tolist()
num_count=Counter(recommend_list)


#显示热评中不网分值的评论数里
print(num_count)

#分组求平均
grouped=df.groupby('contentsenti').describe().reset_index()
recommend=grouped['contentsenti'].values.tolist()
print(recommend)

#根据用户打分的分组,对每组的情感值求平均
sentiment_average =df.groupby('contentsenti')['contentposprob'].mean()
sentiment_scores=sentiment_average.values
print(sentiment_scores)

from bs4 import BeautifulSoup
import time
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
#柱状图
# plt.rc("font",family='MicroSoft YaHei',weight="bold")
# x=['积极','消极','中性']
keys = num_count.keys()
values = num_count.values()
# plt.bar(x, values)
# plt.show()
#饼状图
mpl.rcParams["font.sans-serif"] = ["SimHei"]
labels =keys
sizes = values
elements=['积极','消极','中性']
#explode = [0,0,1]
colors = ['red','pink','purple']
#fraces = [15,30,45,10]
plt.axes(aspect='equal')
plt.xlim(0,8)
plt.ylim(0,8)
plt.pie(x=sizes,labels= labels,autopct='%.3f%%',colors=colors)
plt.legend(elements,title="名称含义")
plt.show()
