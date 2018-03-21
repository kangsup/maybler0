#Ex10_Program_Excercise_Random_games
#game1-1
### 정답입니다 오답입니다
import random as r

input('엔터를 누르면 문제가 나옵니다')
a = r.randint(1, 9)
b = r.randint(1, 9)
c = a*b
print(a, '*', b, '= ?')
x = input()
d = int(x)
if d == c:
	print('정답입니다')
else:
	print('오답입니다')