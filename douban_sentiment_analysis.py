

"""
Created on Wed May  5 20:12:48 2021

@author: 13397
"""

#encoding='GBK'

import pandas as pd
from snownlp import SnowNLP
from snownlp import sentiment

#读取取的csv文件,标题在第3列,序号为2
df=pd.read_csv('douban_movie.csv', header=None,usecols=[2])

#将 dataframe转换为1ist
contents=df.values.tolist()
#数据长度
print(len(contents))
#定义空列表存储情感分值
score=[]


for content in contents:
    try:
        s=SnowNLP(content[0])
        #情绪判断，返回值为正面情绪的概率，越接近1表示正面情绪，越接近0表示负面情绪
        score.append(s.sentiments)
        #分词
        print(s.words)
    except:
         print("something is wrong")
         score.append (0.5)
         
#显示情感得分长度,与数据长度比较
print(len(score))
#存储
data2=pd.DataFrame(score)
data2.to_csv('sentiment.csv', header=False, index=False,mode='a+')
