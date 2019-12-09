from threading import *;


def AsciiValues(str):
    print("Ascii Value of ", str, " is :", ord(str))


def main():
    small = input("Enter Small Character :")
    if small.upper():
        small = small.lower()
    large = input("Enter Capital Character :")
    if large.lower():
        large = large.upper()
    num = input("Enter Number")
    if not (num.isdigit()):
        print("Enter Digit")
    else:
        digitThread = Thread(target=AsciiValues, args=(num,))
        digitThread.start()

    smallThread = Thread(target=AsciiValues, args=(small,))
    largeThread = Thread(target=AsciiValues, args=(large,))

    smallThread.start()
    largeThread.start()


if __name__ == '__main__':
    main()
