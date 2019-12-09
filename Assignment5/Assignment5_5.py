fact = 1
def Factorial(num):
    global fact
    if num != 0:
        fact = fact * num
        Factorial(num - 1)
        return fact

def main():
    num = int(input("Enter The Number :"))
    ans = Factorial(num)
    print("Factorial  is :",ans)


if __name__ == "__main__":
    main()
