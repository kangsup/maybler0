

#Ex 6- Ex
#print(list(range(5)))
#print(list(range(0,5)))
#print(list(range(1,11)))

#for x in range(5, 16):
#   print(x)

#for x in range(16):
#   print(x, "Hello")

#s = 0
#for x in range(51, 101):
#	s = s + x; 
#print(s)

#Ex 7-3
x = 95
while x <= 100:
	print(x)
	x = x+2


x = 81
while x <= 100:
	print(x)
	x=x+3

#Ex-7-Ex
#1) 
for x in range(1,201):
	if x % 10 == 7:
		print(x)

#2)
for x in range(90, 101):
    if x%2 == 0:
    	print(x, "짝수")
    else:
    	print(x, "홀수")

print("different implementation")

x=88
while x<=100:
    if x%2==1:
	    print(x, "Odd number")
    else:
        print(x, "Even number")
    x=x+1



x=1001
while x<=1020:
	if x%10!=8:
		print(x)
	x=x+1


for i in range(1, 11):
	if i%10==8:
		break
	else:
		print(i)

for i in range(1, 11):
	if i%10==8:
		continue
	else:
		print(i)