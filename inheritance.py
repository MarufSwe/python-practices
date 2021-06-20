class Computer():
    def processor(self):
        print("cori5 intel processor")

    def monitor(self):
        print("39 inches LG monitor")

class Mobile(Computer):  # Computer parent class inherit by Mobile child class
    def model(self):
        print("This is iPhone 7 plus")

    def price(self):
        print("70000 taka BD")

class Gadget(Mobile):
    print("Gadget class inherit above two classes")


com = Computer()
com.monitor()

mob = Mobile()
gad = Gadget()
gad.processor()