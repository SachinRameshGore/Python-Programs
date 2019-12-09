from threading import *;


def Evenlist(list):
    i=0
    EvemSum = 0
    for i in list:
        if i % 2 == 0:
            EvemSum += i
    print("Even List Sum {}".format(EvemSum))



def Oddlist(list):
    i = 0
    OddSum = 0
    for i in list:
        if i % 2 == 1:
            OddSum += i
    print("Odd List Sum {}".format(OddSum))


def main():
    num = int(input("Enter How Many Elements You Want :"))
    arr = list()
    print("Enter Numbers In Array :")
    for i in range(0, num):
        no = int(input("Num :"))
        arr.append(no)
    print("___________________________________")
    print(arr)
    print("___________________________________")

    evenlist = Thread(target=Evenlist, args=(arr,))
    evenlist.start()

    oddlist = Thread(target=Oddlist,args=(arr,))
    oddlist.start()

if __name__ == "__main__":
    main()
