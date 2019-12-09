class Circle:
    PI = 3.14

    def __int__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def accept(self):
        self.radius = int(input("Enter Radius :"))

    def display(self):
        print("Radius : ",self.radius)
        print("Area of the circle : ",self.area)
        print("Circumference is :",self.circumference)
