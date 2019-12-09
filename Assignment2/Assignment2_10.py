def SumOfNumber(num):
    sum = 0
    while num != 0:
        rem = num % 10
        sum = sum + rem
        num = num // 10
    return sum


num = int(input("Enter Number :"))
ans = SumOfNumber(num)
print("Total Sum is  :", ans)
