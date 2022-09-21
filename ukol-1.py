baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

kodBaliku = input("Zadejte kód balíku: ")
if kodBaliku in baliky:
    if baliky[kodBaliku] == True:
        print("Balík byl předán kurýrovi.")
    else:
        print("Balík zatím nebyl předán kurýrovi.")
else:
    print("Balík neevidujeme.")