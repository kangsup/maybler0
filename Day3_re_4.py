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

r3=re.compile('\d+')
print(r3.search('코드윙즈는 1018년 1월 31일'))
print(r3.findall('코드윙즈는 1018년 1월 31일'))

print('')
r4=re.compile('[:]')
r5=re.compile('[:]+')
r6=re.compile('[: ]+')
print(r4.split('my name is: Hong Gil Dong'))
print(r5.split('my name is: Hong Gil Dong'))
print(r6.split('my name is: Hong Gil Dong'))