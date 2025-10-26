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


print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")


class Talo:
    def __init__(self, alin_kerros_num, ylin_kerros_num, h_lkm):
        self.alin_kerros_num = alin_kerros_num
        self.ylin_kerros_num = ylin_kerros_num
        self.hissit = []

        for i in range(h_lkm):
            hissi = Hissi(alin_kerros_num, ylin_kerros_num)
            self.hissit.append(hissi)

    def aja_hissiä(self, h_num, kohde_kerros):
        print(f"Hissi num: {h_num} kerrokseen {kohde_kerros}")
        self.hissit[h_num].siirry_kerrokseen(kohde_kerros)

kerrostalo = Talo(1, 5, 3)
kerrostalo.aja_hissiä(0,1)
kerrostalo.aja_hissiä(1,2)
kerrostalo.aja_hissiä(2,3)
kerrostalo.aja_hissiä(2, 0)