# From the book "Deep Learning from Scratch"
# O'reilly Series
# Korean version from 한빛미디어
# 저자: 사이토 고키
# 역자: 개앞맵시 (이복연) wegra.lee@gmail.com


a = [1, 2, 3, 4, 5] # list 리스트 생성
a[4] = 99 # 색인4값의 원소로 99 대입
a[1:] # 인덱스 1부터 끝까지 얻기 
a[:-2] # 처음부터 마지막 원소의 2개 앞까지 얻기 

me = { 'height': 180}  # generation of a dictionary
me['height'] # accessing the element
me['weight'] = 83  # adding a new element
print(me)

hungry = True  # I'm hungry
sleepy = False # I'm not sleepy

type(hungry)
not hungry
hungry and sleepy # I'm hungry and I'm not sleepy
hungry or sleepy  # I'm hungry or sleepy

if hungry:
	print("I'm hungry!")


hungry = False

#1.3.8 Python for statement
for i in [1, 2, 3]:
    print(i)



# 1.3.9 Python function
def hello():
    print("Hello World!")

hello()

def hello(object):
    print("Hello " + object +"!")


hello("cat")
#Python interpreter Ending: 
#  On Linux or Mac: ^D only
#  On Windows: ^Z + Enter

# 1.4 Python Script Files










