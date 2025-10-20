class Car:
    def __init__(self, id_number, top_speed):
        self.speed = 0
        self.trip = 0
        self.top_speed = top_speed
        self.id_number = id_number

    def accelerate(self, speed_change):
        new_speed = self.speed + speed_change
        if new_speed > self.top_speed:
            self.speed = self.top_speed

        elif new_speed < 0:
            self.speed = 0

        else:
            self.speed = new_speed

    def kulje(self, hours):
        self.trip += self.speed * hours


new_car = Car("ABC-123", 142)

new_car.accelerate(60)
new_car.trip = 2000

new_car.kulje(1.5)
print(f"1.5 t kuljetun matka: {new_car.trip} km ja nopeus {new_car.speed} km/h")