# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes
# tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa
# saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: Listan alkioiden lajittelyjärjestyksen voi kääntää antamalla sort-
# metodille argumentiksi "reverse = True".

luvut = []

while True:
    syote = (input("Anna luvut: "))
    if syote == '':
        break
    luku = float(syote)
    luvut.append(luku)

luvut.sort(reverse=True)
print("Viisi suurinta lukua: ")
print(luvut[:5])