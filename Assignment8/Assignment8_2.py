from threading import *


def evenfactors(no):
    sum1 = 0
    for i in range(1, (no // 2) + 1):
        if no % i == 0 and i % 2 == 0:
            print(i)
            sum1 = sum1 + i
    print("Even Factors Sum is : ", sum1)


def Oddfactors(no):
    sum1 = 0
    for i in range(1, (no // 2) + 1):
        if no % i == 0 and i % 2 != 0:
            print(i)
            sum1 = sum1 + i
    print("Odd Factors Sum is : ", sum1)


def main():
    no = int(input("Enter The Number :"))
    evenFactorThread = Thread(target=evenfactors, args=(no,))
    evenFactorThread.start()
    evenFactorThread.join()
    oddFactorThread = Thread(target=Oddfactors, args=(no,))
    oddFactorThread.start()
    oddFactorThread.join()
    print("Exit From Main")


if __name__ == "__main__":
    main()
