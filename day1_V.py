
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


list1 = [1, 3, 5]
list2 = [7, 9, 11]
print(list1 + list2)

print(list2 * 3)

tuple1 = (1,2,3,4,5)
print(tuple1)
#del tuple[4]

tuple1 = (1,2,3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)

print(tuple1 * 3)

#Ex 5-8
country = {"Asia":"Korea", "America":"USA", "Europe":"Italy"}
country["America"] = "Canada"
print(country)

country["Asia"] = "China"
print(country)

country["South America"] = "Brazil"
print(country)

del country["Asia"];
country["Africa"] = "Egypt"
print(country)

score = {"Korean": 90, "math": 80, "science":70}
#score["English"] = 60
#print(score)

#del score["science"]
#print(score)
str30 = "Avg. score: %d" %((score["Korean"] + score["math"] + score["science"])//3)
print(str30)

