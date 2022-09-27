vysvedceni = {"Český jazyk": 1, "Matematika": 2, "Dějepis": 3}
print(vysvedceni)

sales["Noc, která mě zabila"] = 0
sales["Vrah zavolá v deset"] += 100
print(sales)

number = int(input("Zadejte číslo lístku: "))
if number in tombola:
  # Funkce pop odstraní hodnotu ze slovníku a tuto odstraňovanou hodnotu vrací. 
  # Můžeme ji tedy uložit do proměnné a nemusíme načítat výhru pomocí hranatých závorek.
  win = tombola.pop(number)
  win = win.lower()
  print(f"Vyhráváš: {win}.")
else:
  print("Bohužel nevyhráváš nic.")

  passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}

name = input("Zadej jméno: ")
## je jmeno v seznamu?
if name in passwords:
  password = input("Zadej heslo: ")
  ## souhlasi heslo?
  if password == passwords[name]:
    print("Smíš vstoupit.")
  else:
    password = input("Nesprávné heslo. Zadej heslo znovu: ")
    if password == passwords[name]:
      print("Smíš vstoupit.")
    else:
      print("Neznáš heslo, vstup zakázán.")
else:
  print("Nejsi na seznamu hostů.")