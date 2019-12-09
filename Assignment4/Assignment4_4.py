from functools import *;

def Accept(num):
    arr = list()
    print("Enter Numbers In Array :")
    for i in range(0, num):
        no = int(input("Num :"))
        arr.append(no)
    return arr


def checkNo(no):
    if no % 2 == 0:
        return True


def square(no):
    return no * no


def addition(no1, no2):
    return no1 + no2


def main():
    num = int(input("Enter How Many Elements You Want :"))
    rawData = Accept(num)
    print("Entered Numbers In array are :", rawData)
    filteredData = list(filter(checkNo, rawData))
    print("Filter :", filteredData)
    if len(filteredData) > 0:
        modifiedData = list(map(square, filteredData))
        print("Map :", modifiedData)
        ans = reduce(addition, modifiedData)
        print("Reduce :", ans)
    else:
        print("There is No data Filtered out !!")


if __name__ == "__main__":
    main()
