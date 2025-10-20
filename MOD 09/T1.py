class Car:
    def __init__(self, id_number, top_speed):
        self.speed = 0
        self.trip = 0
        self.top_speed = top_speed
        self.id_number = id_number

new_car = Car("ABC-123", 142)

print(f"Uuden rekisteritunnus ja huippunopeus ovat: {new_car.id_number} ja {new_car.top_speed} km/h.")
print(f"Tämänhetkinen nopeus: {new_car.speed} km/h.")
print(f"Kuljettu matka: {new_car.trip} km.")