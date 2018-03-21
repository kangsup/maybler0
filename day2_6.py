#day2_8-2
def equation(x):
	y=3*x+1
	return y

print(equation(3)) 


def sum(a, b):
	z=a+b
	return z

print(sum(10, 20))

#Ex. 8-3
def multiple(*a):
	result = 1
	for x in a:
		result *= x
	return result

print("Execute multiple(1,2,3,4)")
print (multiple(1, 2, 3, 4))


#Ex. 8-4
def print_func(*a):
	for x in a:
		print(x)


print_func(11, 22, 33, 44)


#Ex. 8-5
def calculator(num1, num2, method='sum'):
	if method=='sum':
		y=num1+num2
	elif method=='min':
		y=num1-num2
	elif method=='mul':
		y=num1*num2
	elif method=='div':
		y=num1/num2
	return y

print (calculator(3, 5))
print (calculator(3, 5, 'mul'))


#Ex. 8-7
def onlyone(a, b):
	return a+b, a*b

print(onlyone(10,20))


#Ex. 8-8 
def onlyone_2(a, b):
	return a+b
	return a*b

print(onlyone_2(10, 20))
