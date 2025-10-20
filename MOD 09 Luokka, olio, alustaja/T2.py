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

new_car = Car("ABC-123", 142)

new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)

print(f"Auton nopeus on {new_car.speed} km/h")

new_car.accelerate(-200)
print(f"Hätäjarrutus! Auton nopeus on nyt {new_car.speed} km/h")