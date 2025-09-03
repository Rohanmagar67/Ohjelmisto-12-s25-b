# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä "for"-toistorakennetta.

import random

nopat = int(input('Anna arpakuutioiden lukumäärä: '))

summa = 0

for arpa in range(nopat):
    silmaluku = random.randint(1,6)
    summa += silmaluku

print(f'Silmälukujen summa on: {summa}')
