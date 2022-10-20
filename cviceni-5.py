class Zamestnanec:
    def __init__(self, jmeno, pozice):
        self.jmeno = jmeno
        self.pozice = pozice
        self.pocet_dni_dovolene = 25
    def __str__(self):
        return f'{self.jmeno} pracuje jako {self.pozice}'
    def cerpani_dovolene(self, pocet_dni):
        if pocet_dni <= self.pocet_dni_dovolene:
            self.pocet_dni_dovolene -= pocet_dni
            return f'Zbyva dovolene: {self.pocet_dni_dovolene}'
        else:
            return f'Nemas dostatek dovolene: {self.pocet_dni_dovolene}'

franta = Zamestnanec('Frantisek', 'svacinar')
#print(franta.cerpani_dovolene(10))

class Manazer(Zamestnanec):
    def __init__(self, jmeno, pocet_podrizenych):
        super().__init__(jmeno, 'Manazer')
        self.pocet_dni_dovolene = 30
        self.pocet_podrizenych = pocet_podrizenych
    def __str__(self):
        return f'{super().__str__()} a ma {self.pocet_podrizenych} podrizenych.'

leopold = Manazer('Leopold', 10)
#print(leopold.cerpani_dovolene(10))
#print(leopold)

class Brigadnik(Zamestnanec):
    def __init__(self, jmeno, uvazek):
        super().__init__(jmeno, 'Brigadnik')
        self.uvazek = uvazek
    def __str__(self):
        return f'{super().__str__()} a ma {self.uvazek} uvazek.'

#ondra = Brigadnik('Ondrej', 0.6)
#print(ondra)

class Balik:
    def __init__(self, adresa, hmotnost):
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.doruceno = False

    def doruc(self):
        self.doruceno = True

    def __str__(self):
        vypis = f'{self.adresa}({self.hmotnost} kg) - {self.doruceno}'
        return vypis

class CennyBalik(Balik):
    def __init__(self, adresa, hmotnost, hodnota):
        super().__init__(adresa, hmotnost)
        self.hodnota = hodnota
    def __str__(self):
        return f'{super().__str__()} a ma cenu {self.hodnota} penez.'

balikPenez = CennyBalik('Praha', '55', 'bilion')
#print(balikPenez)

pisemky = [0, 2, 0, 1, 1, 3]
#chci všechny +1
pisemky_1 = []
for znamka in pisemky:
    pisemky_1.append(znamka+1)
print(pisemky_1)
#list comprehention
print([znamka+1 for znamka in pisemky])
#copy
print([znamka for znamka in pisemky])
#z 0 -> 1
print([znamka+1 for znamka in pisemky if znamka == 0])

jmena = ['Marek', 'Dominika']
jmena_m = [jmeno.lower() for jmeno in jmena]
print(jmena_m)

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
soucty = [sum(teplota) for teplota in teploty]
print(soucty)