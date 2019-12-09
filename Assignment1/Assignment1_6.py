def checkNum(Num):
    if num > 0:
        print(Num, " Is Positive ")
    elif num < 0:
        print(Num, "Is Negative ")
    else:
        print(" number is Zero")


num = int(input("Enter the Number :"))
checkNum(num)