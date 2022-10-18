class Jednorozec:
    def __init__(self, jmeno, barva):
        self.jmeno = jmeno
        self.barva = barva
        self.is_fluffy = True
    def __str__(self):
        return f'{self.jmeno} ({self.barva})'
    def __eq__(self, y):
        return self.jmeno == y.jmeno

    def vypis_informace(self):
        return f'Muj jednorozec se jmenuje {self.jmeno} a jeho barva je {self.barva} a je heboucky.'

jednorozec = Jednorozec('Jonatan', 'duhova')
jednorozecY = Jednorozec('Aja', 'duhova')

print(jednorozec.vypis_informace())
print(jednorozec) #bez __str__ by vypsal misto pameti kde je ulozen objekt jednorozec
print(jednorozec == jednorozecY)

class Balik:
    def __init__(self, adresa, hmotnost):
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.doruceno = False
    def doruc(self):
        self.doruceno = True
    def __str__(self):
        return (
            f"Balik byl odeslan na adresu {self.adresa}, jeho hmotnost je {self.hmotnost}"
            f' - {"dorucen" if self.doruceno else "nedorucen"}'
            )
      
balik = Balik('Praha 8', '1,1 kg')
balik.doruc()
print(balik)

class Kniha:
    def __init__(self, nazev, pocet_stran, cena):
        self.nazev = nazev
        self.pocet_stran = pocet_stran
        self.cena = cena
    def __str__(self):
        return f'Kniha se jmenuje {self.nazev}, ma {self.pocet_stran} stran a stoji {self.cena} kc.'
    def sleva(self, sleva):
        self.sleva = sleva
        return self.cena*self.sleva*0.01

kniha = Kniha('Klub rvacu', '357', '399')
print(kniha)