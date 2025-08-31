# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä
# antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa.

while True:
   tuumat = float(input("Anna tuumat: "))
   if tuumat < 1:
       print('Toiminta lopetettu')
       break
   sentit = tuumat * 2.54
   print(f'{tuumat} tuuma on {sentit:.2f} cm')