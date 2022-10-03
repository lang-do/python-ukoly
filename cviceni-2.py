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

"""

purchase_list = [
    {"person": "Petr", "item": "Prací prášek", "value": 399},
    {"person": "Ondra", "item": "Savo", "value": 80},
    {"person": "Petr", "item": "Toaletní papír", "value": 65},
    {"person": "Libor", "item": "Pivo", "value": 124},
    {"person": "Petr", "item": "Pytel na odpadky", "value": 75},
    {"person": "Míša", "item": "Utěrky na nádobí", "value": 130},
    {"person": "Ondra", "item": "Toaletní papír", "value": 120},
    {"person": "Míša", "item": "Pečící papír", "value": 30},
    {"person": "Zuzka", "item": "Savo", "value": 80},
    {"person": "Pavla", "item": "Máslo", "value": 50},
    {"person": "Ondra", "item": "Káva", "value": 300}
]

total_value = 0
sum_per_person = {}

for item in purchase_list:
    person = item["person"]
    value = item["value"]
    
    if person in sum_per_person:
        sum_per_person[person] += value
    else:
        sum_per_person[person] = value

for person, value in sum_per_person.items():
    total_value += value
    print(f"{person} utratil(a) za společné nákupy {value} Kč.")

average_value = total_value / len(sum_per_person)
print(f"Průměrná hodnota na osobu je {round(average_value)} Kč.")


for person, value in sum_per_person.items():
    result = average_value - sum_per_person[person]
    result_final = round(result)
    if result >= 0:
        print(f'{person} by mel doplatit {result_final}.')
    elif result < 0:
        print(f'{person} zaplatil o {-result_final} vice nez je prumerna platba.')



books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]

books_2019 = list(filter(lambda item: item["year"] == 2019, books))
print(books_2019)


sum_pop_reg = {}
pop_value = 0
for stat in staty:
    subregion = stat['subregion']
    population = stat['population']
    region = stat['region']
    if subregion in sum_pop_reg:
        sum_pop_reg[subregion] += population
    else:
        sum_pop_reg[subregion] = population


for subregion, population in sum_pop_reg.items():
    if subregion in stat['region']:
        pop_value += population
        print(sum_pop_reg)


if value in list:
    for stat in staty:
        if stat['region'] == value:
            print(stat['name'])
            dict_sub_reg = {stat['subregion']}

sum_pop_reg = {}
pop_value = 0
for stat in staty:
    subregion = stat['subregion']
    population = stat['population']
    region = stat['region']
    if subregion in sum_pop_reg:
        sum_pop_reg[subregion] += population
    else:
        sum_pop_reg[subregion] = population


for subregion, population in sum_pop_reg.items():
    if subregion in stat['region']:
                pop_value += population
                print(sum_pop_reg)