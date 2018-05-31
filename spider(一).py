# -*- coding: utf-8 -*-  
import requests
from bs4 import BeautifulSoup

#发出请求获得HTML源码
def get_html(url):
	headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}
	resp = requests.get(url,headers=headers).text
	return resp

# 获得所有页面的函数
def generate_url():
	sum_url = []
	for i in range(0,10):
		#URL中start为：0,25,50,75....
		i = i * 25
		each_url = 'https://movie.douban.com/top250?start=' + str(i) + '&filter='
		sum_url.append(each_url)
	return sum_url


# 解析页面，获得数据信息
def html_parse():
	for url in generate_url():		
		soup = BeautifulSoup(get_html(url),'lxml')
		for tag  in soup.find_all('div', attrs={"class":"item"}):
			#电影排名
			num = tag.find("em").get_text()
			#电影
			name = tag.find('div', attrs={"class":"hd"}).a.get_text()
			name = name.replace('\n','')
			name = name.replace(' ','')
			#评分
			score = tag.find('span', attrs={"class":"rating_num"}).get_text()
			
			tag_body = tag.find('div', attrs={"class":"bd"})
			#导演及演员信息
			director = tag_body.find('p').get_text().replace(' ','')
			info = tag.find(attrs={"class":"inq"})
			content = ''
			if(info):
				content = info.get_text()


			movie_num = '[排名]:' + num + '\n'
			movie_name = '[电影]:' + name + '\n'
			movie_score = '[评分]:' + score + '\n'
			movie_director = '[导演及演员信息]:' + director + '\n'
			movie_info = '[简介]:' + content + '\n'
			data = movie_num + movie_name + movie_score + movie_director + movie_info
			f.writelines(data + '\n' +'------------------------' + '\n')

f = open('/home/xxxx/桌面/Top250.txt', 'w' ,encoding='utf-8')
html_parse()
f.close()
print('保存成功！')
