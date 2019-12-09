def Sumfactorial(num):
    sum = 0
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            sum = sum + i
    return sum


num = int(input("Enter Number :"))
ans = Sumfactorial(num)
print("Sum Of Factor is ",ans)