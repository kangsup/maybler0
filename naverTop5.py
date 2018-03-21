#네이버 실시간 검색 순위 
import requests
import time
from bs4 import BeautifulSoup

loopNum = 1
while True:
	print("*"*30)
	response = requests.get('https://www.naver.com/')
	assert response.status_code is 200

	dom = BeautifulSoup(response.content, "html.parser") # (print(dom))
	ranking_elements = dom.select("li.ah_item") # (print(ranking_elements))
	for i, ranking_element in enumerate(ranking_elements):
		ranking_title_element = ranking_element.select(".ah_k")[0]
		print(i+1, "위: ", ranking_title_element.text)
		if i+1>=20:
			break
	print("*"*30)
	print("[", loopNum, "] 1분에 한번씩 갱신됩니다.")
	print("*"*30, "\n")
	#time.sleep(20) #20초마다 갱신 
	time.sleep(60)