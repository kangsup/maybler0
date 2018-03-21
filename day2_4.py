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
