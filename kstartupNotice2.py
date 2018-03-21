#K-Startup 사업공고 실시간 검색 순위 
import requests
import time
from bs4 import BeautifulSoup


print("*"*60)
response = requests.get('https://www.k-startup.go.kr/main.do')
assert response.status_code is 200

dom = BeautifulSoup(response.content, "html.parser") # (print(dom))

support_lists = dom.select("#divTab01 > ul > li") # (print(ranking_elements))
for i, support_list in enumerate(support_lists):
	support_list_title = support_list.select("a")[0]
	#print(i+1, "위: ", support_list_title.attrs.get('title'))
	print(i+1, "위: ", support_list_title.attrs.get('title')[:-9])
	##NOT_WORKING: print(i+1, "위: ", support_list_title.innerText)
print("*"*60)