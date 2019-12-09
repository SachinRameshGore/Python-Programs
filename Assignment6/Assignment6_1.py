class Demo:
    value = 0

    def __init__(self, value1, value2):
        self.no1 = value1
        self.no2 = value2

    def fun(self):
        print("Number1 :", self.no1)
        print("Number2 :", self.no2)

    def gun(self):
        print("Number1 :", self.no1)
        print("Number2 :", self.no2)


def main():
    number1 = int(input("Enter First Number :"))
    number2 = int(input("Enter Second Number :"))
    obj1 = Demo(number1, number2)
    obj2 = Demo(number1, number2)
    obj1.fun()
    obj2.fun()
    obj1.gun()
    obj2.gun()


if __name__ == "__main__":
    main()
