#Ex9_Program_Excercise_fileWrite_Read


f=open('C:\\Users\\mayblerHome\\Desktop\\language.txt', 'rt')
lines=f.readlines()

for line in lines:
	print(line)


for line in lines:
	print(line, end='')



f=open('C:\\Users\\mayblerHome\\Desktop\\program.txt', 'wt')
f.write('카카오톡\n')
f.write('페이스북\n')
f.write('구글\n')

f.close()
