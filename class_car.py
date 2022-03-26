class CAR:

    def __init__(self):
        self.name = input("Enter your Car name: ")
        self.modelno = input("Enter your car model NO : ")
        self.color = input("Enter your car color : ")


class Test(CAR):
    def display(self):
        print("/n ============ CAR Details ==========")
        print("Name is : ", self.name)
        print("Car Model no is:", self.modelno)
        print("Car color is:", self.color)


obj = Test()
obj.display()