# -*- coding: utf-8 -*-  
import requests
from bs4 import BeautifulSoup

def get_html(url):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
	resp = requests.get(url,headers=headers).text
	return resp

def generate_url():
	sum_url = []
	for i in range(0,10):
		i = i * 25
		each_url = 'https://movie.douban.com/top250?start=' + str(i) + '&filter='
		sum_url.append(each_url)
	return sum_url



def html_parse():
	for url in generate_url():		
		soup = BeautifulSoup(get_html(url),'lxml')
		for tag  in soup.find_all('div', attrs={"class":"item"}):
			
			num = tag.find("em").get_text()
			
			name = tag.find('div', attrs={"class":"hd"}).a.get_text()
			name = name.replace('\n','')
			name = name.replace(' ','')
			
			score = tag.find('span', attrs={"class":"rating_num"}).get_text()
			
			tag_body = tag.find('div', attrs={"class":"bd"})
			director = tag_body.find('p').get_text().replace(' ','')
			info = tag.find(attrs={"class":"inq"})
			if(info):
				content = info.get_text()


			movie_num = '[排名]:' + num + '\n'
			movie_name = '[电影]:' + name + '\n'
			movie_score = '[评分]:' + score + '\n'
			movie_director = '[导演]:' + director + '\n'
			movie_info = '[简介]:' + content + '\n'
			data = movie_num + movie_name + movie_score + movie_director + movie_info
			f.writelines(data + '\n' +'------------------------' + '\n')

f = open('/Users/Tim/Desktop/spider/Top250.txt', 'w' ,encoding='utf-8')
html_parse()
f.close()
print('保存成功！')
