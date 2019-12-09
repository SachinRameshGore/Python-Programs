from marvellous import *;


def ListPrime():
    def Accept(num):
        arr = list()
        brr = list()
        sum = 0
        print("Enter Numbers In Array :")
        for i in range(0, num):
            no = int(input("Num :"))
            arr.append(no)
            ans = CheckPrime(no)
            if ans == True:
                # print("prime")
                sum += no
                brr.append(no)

        return arr,brr,sum

    num = int(input("Enter How Many Numbers You Want :"))
    arr,brr,sum = Accept(num)
    print("Entered Numbers Are :", arr)
    print("prime numbers are :", brr)
    print("Addition of Prime Numbers is :", sum)


def main():
    ListPrime()


if __name__ == "__main__":
    main()
