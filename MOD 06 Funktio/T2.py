# Muokkaa edellistä funktiota, siten, että funktio saa parametrinaan nopan
# tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi
# 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä
# jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka
# kysytään käyttäjältä ohjelman suorituksen alussa.


import random

def nopan_heitto(tahkot):
   return random.randint(1, tahkot)

tahkojen_maara = int(input('Mikä on nopan maksimisilmäluku?: '))
max_silmaluku = tahkojen_maara

while True:
    silmaluku = nopan_heitto(tahkojen_maara)
    print(silmaluku)
    if silmaluku == max_silmaluku:
        print(f"Nopan maksimisilmäluku on {silmaluku}!")
        break