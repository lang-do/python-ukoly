import math

def validate_number(tel_num=False):
	tel_num = input('Zadejte telefonni cislo adresata: ')
	tel_num = tel_num.replace(' ', '')
	if len(tel_num) == 9:
		return True
	elif len(tel_num) == 13 and tel_num[0:4] == '+420':
		return True
	else:
		return False
		
if validate_number(True):
	def price(message):
		message = input('Zadejte text zpravy: ')
		num_char = len(message)
		num_messages = math.ceil(num_char / 180)
		return num_messages * 3
	print(f'Cena zpravy je {price(input)} Kč.')
else:
	print('Chybny format telefonniho cisla.')
