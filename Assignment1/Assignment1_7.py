def div(Num):
    if Num % 5 == 0:
        return True
    else:
        return False


n = int(input("Enter The Number :"))
ans = div(n)
print(ans)