# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan "Tervetuloa" ja jälkimmäisessä "Pääsy evätty".
# Oikea käyttäjätunnus on "python ja salasana "rules".

oikea_kayttajatunnus = "python"
oikea_salasana = "rules"
yritykset = 0

while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    if tunnus == oikea_kayttajatunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break
    else:
        yritykset += 1
if yritykset == 5:
    print("Pääsy evätty")