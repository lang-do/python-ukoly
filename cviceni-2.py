from optparse import Values
from turtle import goto


sales = {
    "A": 4165,
    "B": 5681,
    "C": 2565,
    "A": 4166 #nove A nebo sales["B"] = 333
}
"""
print(sales['A'])
print(sales.get('D')) #D je None misto KeyError
print(sales.get('D', 'neexistuje'))
print(list(sales)) #predelam slovnik na list
print(sales.values()) #print(list(sales.values()))
print(sales.keys())
print('A' in sales.keys())

print(sales)
print(sales.pop('A')) # == hodnota_A = sales.pop('A') bez outputu
print(sales)

for book in sales: #book je nazev promenne do ktere ukladame, v sales jsou 3 promenne proto vypise 3x
    print(1)
    print(book)

for key, value in sales.items():
    print(f'Klic {key} -- {value}')

books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]

sum_profit = 0
for book in books:
    profit_knihy = book['sold'] * book['price']
    sum_profit += profit_knihy
print(sum_profit)

"""

school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

sum = 0
for mark in school_report.values():
    sum += mark
    average = sum / len(school_report)
print(f'průměrná známka je {average}')

for key, value in school_report.items():
    if value == 1:
        print(key)

books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

sum_pages = 0
for book in books:
    num_pages = book['pages']
    sum_pages += num_pages
print(f'počet přečtených stran je {sum_pages}')

good_book = 0
for book in books:
    if book['rating'] >= 8:
        good_book += 1
print(f'dobrých knih je {good_book}')

plates = {"4A2 3000": "František Novák",
    "6P5 4747": "Jana Pilná",
    "3B7 3652": "Jaroslav Sečkár",
    "1P5 5269": "Marta Nováková",
    "37E 1252": "Martina Matušková",
    "2A5 2241": "Jan Král"}     

for key, value in plates.items():
    if key[1] == "P":
        print(value)

for item in 'Dominika':
    print(item)

for item in range(3):
    print('Knock')