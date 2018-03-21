#네이버 가장 많이 본 뉴스 실시간 순위 
import requests
#import time
from bs4 import BeautifulSoup


print("-"*60)
response = requests.get('http://news.naver.com')
assert response.status_code is 200

dom = BeautifulSoup(response.content, "html.parser") # (print(dom))


newstypes = ['정치','경제','사회','생활/문화','세계','IT/과학','TV연예','스포츠']

#support_lists = dom.select("#divTab01 > ul > li") 
# (print(ranking_elements))

for newstype_index, newstype in enumerate(newstypes):
	newstype_index += 100
	newstype_list = dom.select("#ranking_"+str(newstype_index)+" > ul > li")
	print('\n'+'*'*50)
	print(newstype)
	print('*'*50)
	for j, newsItem in enumerate(newstype_list):
		newsTitleAnchor = newsItem.select("a")[0]
		print(j+1, "위: ", newsTitleAnchor.attrs.get('title'))
print("-"*60)