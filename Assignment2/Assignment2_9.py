def CountNumber(num):
    count = 0
    while num != 0:
        num = num // 10
        count = count + 1
    return count


num = int(input("Enter Number :"))
ans = CountNumber(num)
print("Total Number Of Digis in ", num, " Are ",ans)
