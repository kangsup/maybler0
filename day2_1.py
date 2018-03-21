
number = int(input("Input any number among 1~9999: "))
if number < 10:
	print("one digit number")
elif number < 100:
	print("two digit number")
elif number < 1000:
	print("three digit number")
elif number < 10000: 
    print("four digit number")
else:
	print("please input a number less than 9999")


for i in range(1, 101):
	if i%5!=0:
		print(i)

x=1
while x<=100:
	if x%5!=0:
		print(x)
	x=x+1

