# -*- coding: utf-8 -*-
"""
Created on Wed May  5 21:42:49 2021

@author: 13397
"""
import jieba
import numpy as np
import PIL.Image as Image
import pandas as pd
import wordcloud



#def chinese_jieba(text):
#    wordlist_jieba=jieba.lcut(text)
#   space_wordlist=" ".join(wordlist_jieba)
#    print(space_wordlist)
#    return space_wordlist

#读取csv文件
path = r'douban_movie.csv'
f = open(path,encoding='utf-8')

# exclude={'我们','你们','他们','它们','因为','因而','所以','如果','那么',\
#           '如此','只是','但是','就是','这是','那是','而是','而且','虽然',\
#           '这些','有些','然后','已经','于是','一种','一个','一样','时候',\
#     '没有','什么','这样','这种','这里','不会','一些','这个','仍然','不是',\
#     '自己','知道','可以','看到','那儿','问题','一会儿','一点','现在','两个',\
#          '三个','也','的','我','是','了'\
#           }


df=pd.read_csv("douban_movie.csv")
comment_list=df['comment'].values.tolist()
recommend_list=df['recommend'].values.tolist()
text=f.read()



#for jj in range (len(comment_list)):
#    if recommend_list[jj]==1:
#        text=text+chinese_jieba(comment_list[jj])
#print(text)


wordlist_jieba=jieba.lcut(text)
space_wordlist=" ".join(wordlist_jieba)
print(space_wordlist)
#设置停用词，这里使用哈工大停用词表
stopwords = set()
content = [line.strip() for line in open('hit_stopwords.txt','rb').readlines()]
stopwords.update(content)
stopwords=stopwords#设置停用调,停用词则不再词云图中表示

#调用包PIL中的open方法,读取图片文件,通过numpy中的 array方法生成数组
mask_pic= np.array(Image.open("background.jpg"))
w=wordcloud.WordCloud(font_path="C:/Windows/Fonts/simfang.ttf",#设置字体
                     mask= mask_pic,#设置背景图片
                     background_color="white",#设置背景颜色
                     max_font_size=150,#设置字体最大值
                     max_words=2000,#设置最大显示的字数
                     
                     ).generate(space_wordlist)
image=w.to_image()
w.to_file('ciyun.png')
image.show()