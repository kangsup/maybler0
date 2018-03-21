
# Ex(Lesson4-2)-Ex
str27 = "www.naver.com"
print(str27[4:9])

str28 = "900123-1234567"
print(str28[7:8])

print("홍길동은 "+str28[0:2]+"년생 "+str28[2:4]+"월 "+str28[4:6]+"일이다")

# Ex 4-3_3
country = ["Korea", "America", "China", ["Seoul", "New York", "Beijing"]]
print(country)
print(country[3][1])

country[2] = "Japan"
print(country)

#country[0:2] = "France", "Italy"
#print(country)

country.append("Hong Kong")
#print("\n"+country)
print(country)

del country[3]
print(country)

country.remove("America")
print(country)

#4-3 Sorting and Reversing
random = [1, 5, 6, 3, 9, 1, 8]
random.sort()
random.reverse()
print(random)
