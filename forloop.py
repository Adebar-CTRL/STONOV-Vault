class newCar():
    def __init__(self, price, sell):
        self.carprice = int(price)
        self.sellprice = int(sell)
    def calc(self):
        for i in range(10):
            self.carprice = self.carprice * 0.8
            print("YEAR ", i + 1, "Price: ", self.carprice)
            if self.carprice < self.sellprice:
                print("SEll")
            else:
                print("hold")

c1 = newCar(input("enter pirce"), input("enter sellprice"))
c1.calc()