#Ex9_Program_Excercise_fileWrite_Read


f=open('C:\\Users\\mayblerHome\\Desktop\\language.txt', 'rt')
lines=f.readlines()

for line in lines:
	print(line)


for line in lines:
	print(line, end='')

