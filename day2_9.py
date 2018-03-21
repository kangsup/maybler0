


#Ex9-3_Concept
class bread:
	material='팥'
	def result(self):
		print('%s빵'%self.material)

a_bread = bread()
a_bread.result()

b_bread=bread()
b_bread.material='크림'
b_bread.result()


print()
print()

#Ex. 9-3_Concept2
class bread:
	def __init__(self, m):
		self.material=m

	def result(self):
		print("%s빵" %self.material)


a2_bread = bread('팥')
a2_bread.result()

b2_bread=bread('크림')
b2_bread.result()



class fish_bread(bread):
	def fish_result(self):
		print('%s맛 붕어빵' %self.material)

a_fish_bread = fish_bread('팥')
a_fish_bread.fish_result()

