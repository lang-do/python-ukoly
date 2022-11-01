with open('mereni.txt', 'r', encoding='utf-8') as file:
    radky = file.readlines()

# r read w write a append
#print(radky)
#for radek in radky:
#    print(radek.replace('\n', ''))

radky = [radek.split('\t') for radek in radky]
radky = [[radek[0], float(radek[1])] for radek in radky]
#print(radky)
#radky_bez_newline = [radek.replace('\n', '').replace('\t', ' ') for radek in radky]
#print(radky_bez_newline) #radek.strip() -> odstrani bile znaky



jmena = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']
with open('uzivatele.txt', mode='w', encoding='utf-8') as vystup:
    jmena_radky = [jmeno + '\n' for jmeno in jmena]
    vystup.writelines(jmena_radky)

import random

hody = []
for i in range(10):
    hod = random.randint(1, 12)
    hody.append(str(hod))
print(hody)

vypis_hodu = [(str(hod) + "\n") for hod in hody]

with open(
    "uvod-do-pythonu-DA/04-soubory-cteni-a-zapis/zapis-do-souboru/hody-kostkou.txt",
    mode="w",
    encoding="utf-8",
) as vystup:
    vystup.writelines(vypis_hodu)