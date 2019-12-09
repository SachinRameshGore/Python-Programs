def checkNum(num):
    if num % 2 == 0:
        print(num, " is Even Number")
    else:
        print(num, "is Odd Number")


num = int(input("Enter Number :"))
checkNum(num)