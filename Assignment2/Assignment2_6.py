def PrintStar(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if j <= num + 1 - i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


num = int(input("Enter The Number :"))
PrintStar(num)
