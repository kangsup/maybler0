#Ex9_Program_Excercise
class Contact:
	def __init__(self, name, phone_number, e_mail, addr):
		self.name=name
		self.phone_number=phone_number
		self.e_mail=e_mail
		self.addr=addr

	def print_info():
		print("이름: ", self.name)
		print('연락처: ', self.phone_number)
		print('이메일: ', self.e_mail)
		print('주소: ', self.addr)


def set_contact():
	name=input('이름: ')
	phone_number=input('연락처: ')
	e_mail=input('이메일: ')
	addr=input('주소: ')
	print(name, phone_number, e_mail, addr)

def print_menu():
	print('1: 연락처 생성')
	print('2: 연락처 출력')
	print('3: 연락처 삭제')
	print('4: 종료')
	menu=int(input("메뉴 선택: "))
	return menu



def run():
	#set_contact()
    while True:
    	menu=print_menu()
    	if menu==4:
    		break

run()