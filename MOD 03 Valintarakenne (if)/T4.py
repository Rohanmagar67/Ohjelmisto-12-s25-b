# T:4
# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
# Vuosi on karkausvuosi, jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia
# vain jos ne ovat jaollisia myös neljälläsadalla.

vuosiluku = int(input("Mikä vuosiluku nyt on: "))
if vuosiluku % 4 == 0 and vuosiluku % 100 != 0 or vuosiluku % 400 == 0:
    print("Vuosiluku on karkausvuosi")
else:
    print("Vuosiluku ei ole karkausvuosi")
