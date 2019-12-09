from functools import *;
def Accept(num):
    arr = list()
    print("Enter Numbers In Array :")
    for i in range(0, num):
        no = int(input("Num :"))
        arr.append(no)
    return arr


def checknumber(no):
    if no >= 70:
        return True


def modify(no):
    return no + 10


def product(no1, no2):
    return no1 * no2

def main():
    num = int(input("Enter How Many Elements You Want :"))
    rawData = Accept(num)
    print("Entered Numbers In array are :", rawData)
    filteredData = list(filter(checknumber, rawData))
    print("Filter :", filteredData)
    if len(filteredData) > 0:
        modifiedData = list(map(modify, filteredData))
        print("Map :", modifiedData)
        ans = reduce(product, modifiedData)
        print("Reduce :", ans)
    else:
        print("There is No data Filtered out !!")


if __name__ == "__main__":
    main()
