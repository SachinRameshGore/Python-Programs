def Printnumber(num):
    for i in range(1, num+1):
        n = 1
        for j in range(1, num+1):
            print(n, end=" ")
            n = n + 1
        print()

num = int(input("Enter Number :"))
Printnumber(num)