def findMinimum(arr, num):
    min = arr[0]
    for i in range(1, num):
        if min > arr[i]:
            min = arr[i]
    return min


def Accept(num):
    arr = list()
    print("Enter Numbers In Array :")
    for i in range(0, num):
        no = int(input("Num :"))
        arr.append(no)
    return arr


def main():
    num = int(input("Enter How Many Elements You Want : "))
    arr = Accept(num)
    min = findMinimum(arr, num)
    print("Entered Numbers In Array Are :", arr)
    print("Minimum Number Is :", min)


if __name__ == "__main__":
    main()