class computer:
    def __init__(self):
        self.__maxprice = 3000

    def sell(self):
        print("maxprice:",self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice = price
    

c = computer()
c.sell()

c.__maxprice = 1000


c.sell()


c.setmaxprice(2500)

c.sell()
