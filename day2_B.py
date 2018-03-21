
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


#Ex. 9-3 Multiinheritance
class number:
	age=54
	def myage(self):
		print('당신의 나이는 %s' %self.age)


class letter:	
	name='maybler'
	def myname(self):
		print('당신의 이름은 %s' %self.name)


class total(number, letter):
	def myprofile(self):
		print('%s의 나이는 %s살' %(self.name, self.age))

maybler_profile=total()
maybler_profile.myage()
maybler_profile.myname()
maybler_profile.myprofile()

