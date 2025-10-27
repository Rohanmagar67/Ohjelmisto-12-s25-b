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

class E_car(Car):
    def __init__(self, akkukapasiteetti , id_number, top_speed):
        super().__init__(id_number, top_speed)
        self.akkukapasiteetti = akkukapasiteetti

class G_car(Car):
    def __init__(self, gas_tank, id_number, top_speed):
        super().__init__(id_number, top_speed)
        self.gas_tank = gas_tank

sähköauto = E_car(52.5,"ABC-15", 180 )
polttomoottoriauto = (G_car(32.3, "ACD-123", 165))
sähköauto.accelerate(50)
polttomoottoriauto.accelerate(25)

sähköauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Sähköauto: {sähköauto.id_number} ja matkamittarilukema: {sähköauto.trip} km")
print(f"Polttomoottoriauto: {polttomoottoriauto.id_number} ja matkamittarilukema: {polttomoottoriauto.trip} km")