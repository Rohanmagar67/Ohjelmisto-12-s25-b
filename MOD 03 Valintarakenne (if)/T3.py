# T:3
# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l

sukupuoli = input('Oletko mies vai nainen: ')

if sukupuoli == 'nainen':
    hemoglobiiniarvo = int(input("Mikä on sinun hemoglobiiniarvo (g/l): "))
    if hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvosi on alhainen")
    elif hemoglobiiniarvo > 175:
        print("Hemoglobiiniarvosi on korkea")
    elif 117 <= hemoglobiiniarvo <= 175:
        print("Hemoglobiiniarvosi on normaali!")

if sukupuoli == 'mies':
    hemoglobiiniarvo = int(input("Mikä on sinun hemoglobiiniarvo (g/l): "))
    if hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvosi on alhainen")
    elif hemoglobiiniarvo > 195:
        print("Hemoglobiiniarvosi on korkea")
    elif 134 <= hemoglobiiniarvo <= 195:
        print("Hemoglobiiniarvosi on normaali!")
