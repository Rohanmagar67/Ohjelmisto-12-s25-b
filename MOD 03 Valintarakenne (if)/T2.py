# T:2
# Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX,A,B,C)
# ja tulostaa sen sanallisen kuvaksen alla olevan luettelon mukaisesti.
# Tehtävässä on käytettävä if/elif/else-toistorakennetta

hyttiluokka = input("Minkä hyttiluokan haluatte: ")

if hyttiluokka == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")

elif hyttiluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")

elif hyttiluokka == "B":
    print('B on ikkunaton hytti autokannen yläpuolella.')

elif hyttiluokka == "C":
    print('C on ikkunaton hytti autokannen alapuolella.')

else:
    print("Virheellinen hyttiluokka")