# T:1
# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
# montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.


Input_kuhan_pituus = float(input("Mika on kuhan pituus cm?: "))

ala_mittainen_kuha = 37
if Input_kuhan_pituus < ala_mittainen_kuha:
    loput_sentit = ala_mittainen_kuha - Input_kuhan_pituus
    print("Kuha on alamittainen, laske kuha takaisin jarveen")
    print(f"Alimmasta sallitusta pyyntimitasta puuttuu {loput_sentit} cm.")

else:
    print("Hienoa!")