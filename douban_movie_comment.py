# -*- coding: utf-8 -*-
"""
Created on Wed May  5 19:46:34 2021

@author: 13397
"""
#encoding=gbk

import requests
import pandas as pd
import re
import time
#import csv
from bs4 import BeautifulSoup
#import os
#from urllib import request
#url请求文件头
header = {'Content-Type':'text/html; charset=utf-8','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

#登录cookies
Cookie ={'Cookie':'ll="118164"; bid=skjwGPUWDvE; __utmv=30149280.19040; __yadk_uid=gi3fUghbVgYJ3LH3jRftPlitQCgD29Zh; douban-fav-remind=1; push_doumail_num=0; push_noty_num=0; ps=y; __gads=ID=b0743a627afc3cd6-2269ab265bc600f0:T=1615430999:S=ALNI_MZwctcx3dtLCA_HIdYGw32F3wEMGg; ct=y; __utmz=30149280.1619251615.25.17.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=30149280; ap_v=0,6.0; __utma=30149280.543365500.1615257365.1620185404.1620214964.28; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1620215534%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DRCUkCvtfVJCBcavp1-B_90DI2jPi6RN40Z1ccq_DJtXlMdAn7te_mHCVfm2Pncz5%26wd%3D%26eqid%3Dd547f7220060f81400000005609286c5%22%5D; _pk_ses.100001.8cb4=*; __utmt=1; _pk_id.100001.8cb4=9049a2656c40a08f.1615257361.26.1620215671.1619955371.; __utmb=30149280.11.9.1620215672801; dbcl2="190409620:viCtJvwqEqo"'}

#构造请求网址
url_1="https://movie.douban.com/subject/34841067/comments?start="

url_2="&limit=20&sort=new_score&status=P"

#循环抓取多页，循环变量为start,0,20,40...
i=0
while True:

    #拼接url
    url=url_1+str(i*20)+url_2
    print(url)

    try:

        #request请求
        html=requests.get(url,headers=header,cookies=Cookie)

        #beautifulsoup解析网址
        soup = BeautifulSoup(html.content,'lxml')

        #评论时间
        comment_time_list = soup.find_all('span', attrs={'class': 'comment-time'})

        #设置循环终止变量
        if len(comment_time_list)==0:

            break

        #评论用户名
        use_name_list=soup.find_all('span', attrs={'class': 'comment-info'})

        #评论文本
        comment_list=soup.find_all('span', attrs={'class': 'short'})

        #评分
        rating_list=soup.find_all('span',attrs={'class': re.compile(r"allstar(\s\w+)?")})

        for jj in range(len(comment_time_list)):

            data1=[(comment_time_list[jj].string,

                use_name_list[jj].a.string,

                comment_list[jj].string,

                rating_list[jj].get('class')[0],

                rating_list[jj].get('title'))]

            data2 = pd.DataFrame(data1)

            data2.to_csv('yanshi.csv', header=False, index=False, mode='a+',encoding="utf-8-sig")

        print('page '+str(i+1)+' has done')

    except:

        print("something is wrong")

    i=i+1
    time.sleep(4)