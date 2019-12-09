from threading import *


def Even():
    for i in range(1,21):
        if i % 2 == 0:
            print("Even : ", i)


def Odd():
    for i in range(21):
        if i % 2 != 0:
            print("Odd : ", i)


def main():
    even = Thread(target=Even)
    odd = Thread(target=Odd)
    even.start();
    odd.start();


if __name__ == "__main__":
    main()
