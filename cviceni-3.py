from tkinter import Y


def greet_user(name):
    print(f'Ahoj {name}')
greet_user('Domi')

pocet = len('Dominika')
print(pocet)

def sum_a_b(a, b):
    #print(a+b)
    return a + b + konstanta
konstanta = 30
print(sum_a_b(1,2))

def funkce_co_je_jenom_definovana():
    pass

def vypocti_znamku(body, bonusove_body=0):
    celkove_body = body + bonusove_body
    if body > 20:
        return 1
    return 5
body = int(input('Zadej body: '))
print(vypocti_znamku(body, 30))

def mult(x, y):
    return x * y
print(mult(2, 3))

def total_price(persons, breakfast=False):
    price_night = 850
    price_breakfast = 125
    if breakfast == True:
        return(persons * price_night + persons * price_breakfast)
    return(persons * price_night)
print(total_price(2, True))

def month_of_birth(rc):
    month = rc[2] + rc[3]
    month = int(month)
    month = month % 50
    return month
print(month_of_birth('9257054439'))