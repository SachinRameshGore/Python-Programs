def PrintStar(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print("*", end=" ")
        print()


n=int(input("Enter Number Of Rows : "))
PrintStar(n)