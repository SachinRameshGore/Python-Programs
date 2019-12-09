def Factorial(num):
    fact = 1
    while num != 0:
        fact = fact * num
        num = num - 1
    return  fact


num = int(input("Enter Number :"))
ans = Factorial(num)
print("Factorial of", num," Is : ", ans)