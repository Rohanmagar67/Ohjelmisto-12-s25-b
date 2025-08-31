# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luvut = []

while True:
    syote = input('Anna luku: ')
    if syote == '':
        break
    luku = float(syote)
    luvut = luvut + [luku]

if luvut:
    print(f"Pienin luku on {min(luvut)} ja suurin luku on {max(luvut)}")
