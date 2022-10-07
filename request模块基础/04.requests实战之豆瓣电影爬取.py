# _*_ coding : utf-8 _*_
# @Time : 2022/10/7 15:57
# @Author : 邓浩
# @File : 04.requests实战之豆瓣电影爬取
# @Project : 爬虫
import requests
import json

url = 'https://movie.douban.com/j/chart/top_list'

param = {
    'type': '24',
    'interval_id': '100:90',
    'action':'',
    'start': '0',  # 从库中的第几部开始请求
    'limit': '20', # 一次取出多少个
}
# 2.UA伪装
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}

response = requests.get(url=url,params=param,headers=headers)

list_data = response.json()

fp = open('./douban.json','w',encoding='utf-8')
json.dump(list_data,fp=fp,ensure_ascii=False)

print('over!!!')
