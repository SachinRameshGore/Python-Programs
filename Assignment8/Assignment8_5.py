from threading import *;


def reverse1():
    for i in range(1, 51):
        print(i)


def reverse2():
    for i in range(50, 0, -1):
        print(i)


def main():
    thread1 = Thread(target=reverse1)
    thread2 = Thread(target=reverse2)
    thread1.start()
    thread1.join()
    thread2.start()
    thread2.join()


if __name__ == "__main__":
    main()
