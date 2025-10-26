class Hissi:
    def __init__(self, alin_kerros_num, ylin_kerros_num):
        self.alin_kerros_num = alin_kerros_num
        self.ylin_kerros_num = ylin_kerros_num
        self.nyky_kerros_num = alin_kerros_num

    def kerros_ylos(self):
        if self.nyky_kerros_num < self.ylin_kerros_num:
            self.nyky_kerros_num += 1
        print(f"Hissi on kerroksessa: {self.nyky_kerros_num}")

    def kerros_alas(self):
        if self.nyky_kerros_num > self.alin_kerros_num:
            self.nyky_kerros_num -= 1
        print(f"Hissi on kerroksessa: {self.nyky_kerros_num}")

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin_kerros_num:
            kohde_kerros = self.alin_kerros_num

        elif kohde_kerros > self.ylin_kerros_num:
            kohde_kerros = self.ylin_kerros_num

        while self.nyky_kerros_num < kohde_kerros:
            self.kerros_ylos()

        while self.nyky_kerros_num > kohde_kerros:
            self.kerros_alas()

h = Hissi(1,10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)