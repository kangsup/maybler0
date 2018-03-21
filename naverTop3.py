#네이버 실시간 검색 순위 
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.naver.com/')
assert response.status_code is 200



dom = BeautifulSoup(response.content, "html.parser")

#(print(dom))

ranking_elements = dom.select("li.ah_item")
#(print(ranking_elements))

for ranking_element in ranking_elements:
	ranking_title_element = ranking_element.select(".ah_k")[0]
	print(ranking_title_element.text)

