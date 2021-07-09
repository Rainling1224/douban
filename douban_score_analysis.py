# -*- coding: gbk -*-
"""
Created on Wed May  5 21:16:07 2021

@author: 13397
"""
import pandas as pd
from collections import Counter

#读取cv文件
df=pd.read_csv('douban_movie.csv')

#统计打分数量
recommend_list=df['recommend'].values.tolist()
num_count=Counter(recommend_list)


#显示热评中不网分值的评论数里
print(num_count)

#分组求平均
grouped=df.groupby('recommend').describe().reset_index()
recommend=grouped['recommend'].values.tolist()
print(recommend)

#根据用户打分的分组,对每组的情感值求平均
sentiment_average =df.groupby('recommend')['score'].mean()
sentiment_scores=sentiment_average.values
print(sentiment_scores)

from bs4 import BeautifulSoup
import time
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
#柱状图
myfont=mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/simfang.ttf');
#图像的名称
plt.title('评星分类柱状图',fontproperties=myfont,fontsize=12)
plt.xlabel('评分档次',fontproperties=myfont,fontsize=12); 
plt.ylabel('人数',fontproperties=myfont,fontsize=12); 
#p=plt.legend(['一星评论','情景二','3','4','5'],prop=myfont);#这里fontsize不起作用，图例很小

keys = num_count.keys()
values = num_count.values()
plt.bar(keys, values)
plt.show()
#饼状图
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
labels =keys
sizes = values
explode = [0,0,0,0,1]
elements = ["三星评论", "五星评论", "四星评论", "二星评论", "一星评论"]
colors = ['red','pink','magenta','purple','orange']
#fraces = [15,30,45,10,]
plt.axes(aspect='equal')
plt.xlim(0,8)
plt.ylim(0,8)
plt.pie(x=sizes,labels= labels,autopct='%.3f%%',colors=colors)
plt.legend(elements,title="名称含义")
# plt.legend(sizes,
#            elements,
#            fontsize=12,
#            title="名称含义",
#            bbox_to_anchor=(0.91, 0, 0.3, 1))
plt.show()