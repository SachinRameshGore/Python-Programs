def checkPrimeNumber(num):
    flag = True
    for i in range (2,(num//2)+1):
        if num % i == 0:
            flag = False
            break
    return flag


num = int(input("Enter Number :"))
ans = checkPrimeNumber(num)
if ans ==True:
    print(num, "Is Prime Number")
else:
    print(num, " Is not Prime Number")