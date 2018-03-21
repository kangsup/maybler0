#예제 4-2
str2 = "programming"
print (str2[1])

print (str2[5])

#Ex 4-4
str4="980123-1234567"
print(str4[:6])


#Ex 4-5
str5 = "20180129"
print (str5[6:])

#Ex 4-6
str6 = "Hi \n\tCodewings"
print(str6)


#Ex4-8
str8 = "mayblerDotCom"
print (str8.upper())
print ("\n\t", str8.lower())

#Ex 4-10
str10 = "apple"
print(str10[0].upper()+str10[1:])

#Ex 4-15
str15 = "I like tomato, tomato juice, and tomato cake"
print(str15.index("tomato"))

# Ex 4-20
str20 = "a,b,c,d,e"
print(str20.split(","))

str21 = "python is fun"
print(str21.split(" "))

#Ex 4-24
str24 = "*"
print(str24*10)

#Ex 4-25
age = int(input("나이를 입력하세요"))
str25 = "I am %d years old" %age
print(str25)


# Ex 4-26
name = input("이름: ")
city = input("도시: ")
str26 = "my name is %s and I live in %s" %(name, city)
print (str26)

# Ex(Lesson4-2)-Ex
str27 = "www.naver.com"
print(str27[4:9])

str28 = "900123-1234567"
print(str28[7:8])

print("홍길동은 "+str28[0:2]+"년생 "+str28[2:4]+"월 "+str28[4:6]+"일이다")