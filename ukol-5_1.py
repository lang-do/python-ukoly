class Nemoc:
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        self.jmeno = jmeno
        self.inkubacni_doba = inkubacni_doba
        self.pocet_obeti = pocet_obeti
        self.sireni = sireni
    def __str__(self):
        return f'Jmeno: {self.jmeno}'
    def zmen_pocet_obeti(self, pocet_obeti):
        self.pocet_obeti = pocet_obeti

class Koronavirus(Nemoc):
    def __init__(self, jmeno, varianty):
        super().__init__(jmeno, inkubacni_doba=3, sireni='kašlíčkem', pocet_obeti=0)
        self.varianty = []
    def pridej_variantu(self, varianta):
        self.varianty.append(varianta)
    def __str__(self):
        return f'{super().__str__()}, Varianty: {", ".join(self.varianty)}'

corona = Koronavirus('Coronavirus', 'omikron')
print(corona) # 'Jmeno: Coronavirus (zadne nalezene varianty)'
print(corona.sireni) # 'vzduchem' -- muzete reprezentovat i cislem
print(corona.inkubacni_doba) # 12 -- je mi jedno jake cislo, ale pevne dane ve volani __init__ metody materske tridy
corona.pridej_variantu('omikron')
corona.pridej_variantu('delta')
print(corona) # 'Jmeno: Coronavirus (varianty: omikron, delta)'
corona.pridej_variantu('alpha')
print(corona) # 'Jmeno: Coronavirus (varianty: omikron, delta, alpha)'
