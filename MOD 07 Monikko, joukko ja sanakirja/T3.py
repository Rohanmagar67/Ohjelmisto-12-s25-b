# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma
# kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn
# lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman, ohjelma
# kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun,
# ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos
# käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden
# toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
# (ICAO-koodi on lentoaseman yksilöivä tunniste. Esim Helsinki lentoaseman ICAO-koodi
# on EFHK. Löydät koodeja helposti selaimen avulla.


lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("Syötä uusi lentoasema (Uusi)")
    print("Hae lentoaseman tietoja (Hae)")
    print("Lopeta (Lopeta)")

    valinta = input("Toiminto: ")
    if valinta == "Uusi":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi

    elif valinta == "Hae":
        icao = input("Anna ICAO-koodi: ")
        if icao in lentoasemat:
            print(f"Lentoasema: {lentoasemat[icao]}")
        else:
            print(f"Lentoasemaa ICAO-koodilla {icao} ei löytynyt")

    elif valinta == "Lopeta":
        print("Ohjelma suljettu")
        break