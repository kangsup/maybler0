
print()
print()

#Ex. 9-3_Concept2
class bread:
	material='팥'

	def result(self):
		print("%s빵" %self.material)


class fish_bread(bread):
	def fish_result(self):
		print('%s맛 붕어빵' %self.material)

a_fish_bread = fish_bread()
a_fish_bread.fish_result()
a_fish_bread.result()
