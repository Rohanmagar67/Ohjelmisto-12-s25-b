import math
import random
from http.cookiejar import join_header_words

# T1
nimi = input("Anna nimesi: ")
tervehdys = "Terve, Rohan!"
print(tervehdys)


# T2
# Ympyrän pinta-ala lasku
# Ympyran pintaala ja sade = pi*r^2
ympyran_sade = float(input("Anna ympyran sade: "))
ympyran_pinta_ala = math.pi * ympyran_sade ** 2
print(f"ympyran_pinta_ala on: {ympyran_pinta_ala:.1f}")


# T3
# Suorakulmio piiri ja pinta-ala lasku

suorakulmion_kanta = float(input("Anna suorakulmion kanta: "))
suorakulmion_korkeus = float(input("Anna suorakulmion korkeus: "))

suorakulmion_piiri = suorakulmion_kanta + suorakulmion_kanta + suorakulmion_korkeus + suorakulmion_korkeus
suorakulmion_pintaala = suorakulmion_kanta * suorakulmion_korkeus

print(f"suorakulmion_piiri on: {suorakulmion_piiri:.1f}")
print(f"suorakulmion_pintaala on: {suorakulmion_pintaala:.1f}")

# T4
# Kolme kokonaislukua, jossa ohjelma tulostaa lukujen summan, tulon ja keskiarvon
# Kysytään ohjelmalta arvot
luku1 = float(input("Anna luku 1: "))
luku2 = float(input("Anna luku 2: "))
luku3 = float(input("Anna luku 3: "))

#Lasketaan nyt
lukujen_summa = luku1 + luku2 + luku3
lukujen_tulo = luku1 * luku2 * luku3
lukujen_keskiarvo = (luku1 + luku2 + luku3) / 3

print(f"lukujen_summa on: {lukujen_summa:.1f}")
print(f"lukujen_tulo on: {lukujen_tulo:.1f}")
print(f"lukujen_keskiarvo on: {lukujen_keskiarvo:.1f}")

# T5
Leiviskat = float(input("Anna leiviskat: "))
Naulat = float(input("Anna naulat: "))
Luodit = float(input("Anna luodit: "))

grammat = (Leiviskat * 20 * 32 * 13.3) + (Naulat * 32 * 13.3) + (Luodit * 13.3)


kilogrammat = int(grammat / 1000)
jaljet_grammat = grammat % 1000


print(f"Massa on {kilogrammat} kilogrammaa ja {jaljet_grammat:.2f} grammaa")


# T6
# Eka on kolminumeroinen koodi (1-6) valilla
koodi1 = "" .join(str(random.randint(0, 9)) for _ in range(3))
print(f"Kolminumeroinenlukon koodi: {koodi1}")


# Toka on nelinumeroinen koodi (1-6) valilla
koodi2 = "" .join(str(random.randint(1, 6)) for _ in range(4))
print(f"Nelinumeroinenlukon koodi: {koodi2}")


