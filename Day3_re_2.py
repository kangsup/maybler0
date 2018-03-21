#정규식 : 컴파일 - 검색 실행 - 매치결과 활용 
import re
r = re.compile('a.c')

print('1. ')
print(r.search('abc'))   #1
print('2. ')
print(r.search('adc'))   #2
print('3. ')
print(r.search('ac'))   #3
print('4. ')
print(r.search('aac'))   #4

r=re.compile('\d')
r1=re.compile('\d+')

print(r.search('코드윙즈는 100명'))
print(r1.search('코드윙즈는 100명'))