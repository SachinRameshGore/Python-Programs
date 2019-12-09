def printnumber():
    for i in range(1, 6):
        num = 1
        for j in range(1, 6):
            if i >= j:
                print(num, end=" ")
                num = num + 1
            else:
                print(" ",end=" ")
        print()


printnumber()