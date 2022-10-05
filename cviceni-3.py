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

# 4 Ruleta (smrt v přímém přenosu)
# Napiš funkci, která bude jednoduchou simulací rulety.
# Budeme uvažovat pouze možnost sázení na řady. Uživatel si může vybrat jednu ze tří řad:

# první řada (hodnoty 1, 4, 7 atd.),
# druhá řada (hodnoty 2, 5, 8 atd.),
# třetí řada (hodnoty 3, 6, 9 atd.).

# Zeptej se uživatele, na kterou ze tří řad sází a na výši sázky.

# Vytvoř funkci roulette, která bude mít parametry číslo řady a výši sázky.
# Pomocí funkce randint z modulu random vygeneruj náhodné číslo v rozsahu od 0 (včetně) do 36.
# Vyhodnoť, do které řady číslo náleží. Nezapomeň, že 0 nepatří do žádné z řad a pokud padne,
# uživatel vždy prohrává.

# Funkce roulette vrací hodnotu výhry.
# Pokud uživatel vsadil na správnou řadu, vyhrává dvojnásobek sázky,
# v opačném případě nevyhrává nic jeho sázka propadá.

import random
value = random.randint(0, 36)

def rada1(i):
    for i in range (1, 36, 3):
        return i
def rada2(i):
    for i in range (2, 36, 3):
        return i
def rada3(i):
    for i in range (3, 37, 3):
       return i
def roulette(no_rady, h_sazky):
    if value in rada1:
        return h_sazky*2
    elif value in rada2:
        return h_sazky*2
    elif value in rada3:
        return h_sazky*2
    elif value == 0:
        return None
    else:
        return None
print(roulette(1, 100))


