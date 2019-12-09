def Addition(arr):
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i]
    return sum


def Accept(num):
    arr = list()
    print("Enter Numbers In Array :")
    for i in range(0, num):
        no = int(input("Num :"))
        arr.append(no)
    return arr


def main():
    num = int(input("Enter How Many Elements You Want :"))
    arr = Accept(num)
    sum = Addition(arr)
    print("Entered Numbers In array are :", arr)
    print("Addition Is :", sum)


if __name__ == "__main__":
    main()
