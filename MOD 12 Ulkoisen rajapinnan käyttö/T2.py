import json
import requests

city_name = input("Anna kaupunki: ")
API_key = "f96f2242bf5917dcacc6332cedbf777a"
lang = "fi"
pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang={lang}"

try:
    vastaus = requests.get(pyyntö)
    print("Status code", vastaus.status_code)
    if vastaus.status_code==200:
        data = vastaus.json()
        print(json.dumps(data, indent=2))
        print(f"Sää kohteessa {city_name} on {data["weather"][0]["description"]}")


except requests.exceptions.RequestException as e:
    print (e)
    print ("Hakua ei voitu suorittaa.")

lämpötila = data["main"]["temp"]
print(f"Lämpötila on: {lämpötila:.0f} celsius astetta")