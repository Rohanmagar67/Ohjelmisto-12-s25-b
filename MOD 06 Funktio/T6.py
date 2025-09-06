# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan
# senttimetreinä sekä pizzan hinnan euroina. Funktio laskee ja palauttaa
# pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy
# käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi
# pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math


def pizza(halkaisija_cm, hinta_euroina):
    halkaisija_neliometri = halkaisija_cm / 100
    sade_neliometri = halkaisija_neliometri / 2
    pinta_ala = math.pi * sade_neliometri ** 2
    yksikkohinta = hinta_euroina / pinta_ala
    return yksikkohinta

halkaisija1 = float(input("Anna ekan pizzan halkaisija (cm): "))
hinta1 = float(input("Anna ekan pizzan hinta (€): "))

halkaisija2 = float(input("Anna tokan pizzan halkaisija (cm): "))
hinta2 = float(input("Anna tokan pizzan hinta (€): "))

yksikkohinta1 = pizza(halkaisija1, hinta1)
yksikkohinta2 = pizza(halkaisija2, hinta2)

if yksikkohinta1 < yksikkohinta2:
    print('Eka pizza antaa paremman vastineen rahalle!')

elif yksikkohinta1 > yksikkohinta2:
    print('Toka pizza antaa paremman vastineen rahalle!')

else:
    print('Molemmat pizzat antavat yhtä hyvän vastineen rahalle!')