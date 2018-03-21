#Ex9_Program_Excercise
class Contact:
	def __init__(self, name, phone_number, e_mail, addr):
		self.name=name
		self.phone_number=phone_number
		self.e_mail=e_mail
		self.addr=addr

	def print_info(self):
		print("이름: ", self.name)
		print('연락처: ', self.phone_number)
		print('이메일: ', self.e_mail)
		print('주소: ', self.addr)


def set_contact():
	name=input('이름: ')
	phone_number=input('연락처: ')
	e_mail=input('이메일: ')
	addr=input('주소: ')
	contact=Contact(name, phone_number, e_mail, addr)
	return contact
	#print(name, phone_number, e_mail, addr)

def print_menu():
	print('1: 연락처 생성')
	print('2: 연락처 출력')
	print('3: 연락처 삭제')
	print('4: 종료')
	menu=int(input("메뉴 선택: "))
	return menu

def print_contact(contact_list):
	print('='*15)
	for contact in contact_list:
		contact.print_info()
		print('-'*10)
	print('='*15)

def delete_contact(contact_list, name):
	for i, contact in enumerate(contact_list):
		if contact.name==name:
			del contact_list[i]
			print('**삭제되었습니다**')

def run():  #set_contact()
	contact_list=[]
	while True:
		menu=print_menu()
		if menu==1:
			contact=set_contact()
			contact_list.append(contact)
			print('->생성되었습니다<-')
		elif menu==2:
			print_contact(contact_list)
		elif menu==3:
			name=input("Name: ")
			delete_contact(contact_list, name)
		elif menu==4:
			break

run()


#Test of enumerate()
fruit=['apple', 'banana', 'mango']
for i, food in enumerate(fruit):
	print(i, food)

