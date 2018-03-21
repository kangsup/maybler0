#네이버 실시간 검색 순위 
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.naver.com/')
assert response.status_code is 200
