import mysql.connector

def hae_maa_koodilla(maa_koodi):
    sql = f"""
    select type, count(*) as maara
    from airport 
    where iso_country = '{maa_koodi}'
    group by type
    order by maara
    """
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulokset = kursori.fetchall()
    kursori.close()
    return tulokset
    
def hae_maa_nimi(koodi):
    sql = f"select name from country where iso_country = '{koodi}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    kursori.close()
    if tulos:
        return tulos[0]

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='rohan',
         password='',
         autocommit=True
         )
    
maa_koodi = input("Anna maakoodi: ")
maan_nimi = hae_maa_nimi(maa_koodi)
lentokentat = hae_maa_koodilla(maa_koodi)
    
print(f"{maan_nimi} {maa_koodi}")
    
if lentokentat:
    for tyyppi, maara in lentokentat:
        print(f"{tyyppi}: {maara} kappaletta")
