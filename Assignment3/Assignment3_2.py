def findMaximum(arr, num):
    max = arr[0]
    for i in range(1, num):
        if max < arr[i]:
            max = arr[i]
    return max


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
    max = findMaximum(arr, num)
    print("Entered Numbers In Array Are :", arr)
    print("Maximum Number Is :", max)


if __name__ == "__main__":
    main()