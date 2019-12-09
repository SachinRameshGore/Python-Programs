def Accept(num):
    arr = list()
    print("Enter Numbers In Array :")
    for i in range(0, num):
        no = int(input("Num :"))
        arr.append(no)
    return arr


def SearchNumber(arr,no):
    count = 0
    for i in range(0, len(arr)):
        if no == arr[i]:
            count +=1
    return count


def main():
    num = int(input("Enter How Many Elements You Want : "))
    arr = Accept(num)
    no = int(input("Enter Number To Search :"))
    ans = SearchNumber(arr, no)
    print("Entered Numbers In Array Are :", arr)
    print("Occurrence of ", no, " IS :", ans)


if __name__ == "__main__":
    main()