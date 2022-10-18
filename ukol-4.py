class Recept:
    def __init__(self, nazev, narocnost, url_adresa):
        self.nazev = nazev
        self.narocnost = narocnost
        self.url_adresa = url_adresa
        self.vyzkouseno = False
    def __str__(self):
        return f'Recept na {self.nazev} ma narocnost {self.narocnost} a muzete ho vyzkouset dle postupu na {self.url_adresa}.'
    def zmen_narocnost(self, nova_hodnota):
        self.narocnost = nova_hodnota
    def uvarit(self):
        self.vyzkouseno = True

class Kucharka:
    def __init__(self, nazev, autor):
        self.nazev = nazev
        self.autor = autor
        self.recepty = []
    def __str__(self):
        return f'Vitejte v kucharce {self.nazev}, kterou pro Vas pripravil {self.autor}.'
    def pocet_receptu(self):
        return len(self.recepty)
    def pridej_recept(self, novy_recept):
        self.recepty.append(novy_recept)


 # Recepty
tiramisu = Recept('Tiramisu', 5, 'url-adresa')
print(tiramisu) # -> 'Tiramisu (narocnost: 5) - jeste nevyzkouseno'
muffiny = Recept('Muffiny', 3, 'url-adresa')
muffiny.uvarit()
muffiny.zmen_narocnost(2)
print(muffiny) # -> Muffiny (narocnost: 2) - vyzkouseno'

#Kucharka
moje_kucharka = Kucharka('Dezerty', 'Andy')
print(moje_kucharka) # -> 'Dezerty od Andy (0 receptu)'
moje_kucharka.pridej_recept(tiramisu)
moje_kucharka.pridej_recept(muffiny)
print(moje_kucharka.pocet_receptu()) # -> 2