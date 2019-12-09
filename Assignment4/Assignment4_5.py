from functools import *;


def Accept(num):
    arr = list()
    print("Enter Numbers In Array :")
    for i in range(0, num):
        no = int(input("Num :"))
        arr.append(no)
    return arr


def checkPrime(no):
    cnt = 0
    for i in range(2, no):
        if i != no:
            if no % i == 0:
                cnt += 1
    if cnt == 0:
        return no


def multiply(no):
    return no * 2


def Maximum(a, b):
    return max(a, b)

def main():
    num = int(input("Enter How Many Elements You Want :"))
    rawData = Accept(num)
    print("Entered Numbers In array are :", rawData)
    filteredData = list(filter(checkPrime, rawData))
    print("Filter :", filteredData)
    if len(filteredData) > 0:
        modifiedData = list(map(multiply, filteredData))
        print("Map :", modifiedData)
        ans = reduce(Maximum, modifiedData)
        print("Reduce :", ans)
    else:
        print("There is No data Filtered out !!")


if __name__ == "__main__":
    main()