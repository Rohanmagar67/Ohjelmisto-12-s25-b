# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa,
# onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia
# vain ykkösellä ja itsellään.
# * Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13
# siten, että jako menee tasan.
# * Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan
# myös luvulla 3 tai luvulla 7.


kokonaisluku = int(input("Anna kokonaisluku: "))

if kokonaisluku < 2:
    print("Kokonaisluku ei ole alkuluku")
else:
    on_alkuluku = True
    for jako in range(2, kokonaisluku):
        if kokonaisluku % jako == 0:
            on_alkuluku = False
            break
    if on_alkuluku:
        print("Kokonaisluku on alkuluku!")

    else:
        print("Kokonaisluku ei ole alkuluku")