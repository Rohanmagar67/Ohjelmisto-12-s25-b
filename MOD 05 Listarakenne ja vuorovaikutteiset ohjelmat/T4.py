# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä "for"-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa
# järjestyksessä, kuin ne syötettiin. Käytä "for"-toistorakenetta nimien kysymiseen
# ja "for/in" toistorakennetta niiden läpikäymiseen.


kaupungit = []

for i in range(5):
    kaupunki = input("Anna kaupunki: ")
    kaupungit.append(kaupunki)

for nimi in kaupungit:
    print(f"Kaupungin nimi: {nimi}")