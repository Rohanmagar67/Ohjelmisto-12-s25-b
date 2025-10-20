import mysql.connector

def hae_lentokentta_icao_koodilla(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    kursori.close()
    return tulos


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='rohan',
         password='',
         autocommit=True
         )

icao = input("Anna lentokentän ICAO-koodi: ")
lentokentta = hae_lentokentta_icao_koodilla(icao)

if lentokentta:
    nimi, kunta = lentokentta
    print(f"Lentokentän nimi: {nimi}")
    print(f"Kunta nimi: {kunta}")

yhteys.close()
