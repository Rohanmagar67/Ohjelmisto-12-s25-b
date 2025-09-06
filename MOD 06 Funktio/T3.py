# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain
# nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita
# pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen
# saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#           * Yksi gallona on 3,785 litraa.


litra = 3.785

def bensiini(gallona):
    return litra * gallona

while True:
    gallona_maarat = float(input("Anna gallonamäärä: "))
    if gallona_maarat < 0:
        break
    litra_maara = bensiini(gallona_maarat)
    print(f"{gallona_maarat} gallonaa on {litra_maara} litraa!")

