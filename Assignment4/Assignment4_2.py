fptr = lambda no1,no2 : no1 * no2

def main():
    num1 = int(input("Enter First number :"))
    num2 = int(input("Enter Second number :"))
    ans = fptr(num1, num2)
    print("Multiplication is :", ans)

if __name__ == "__main__":
    main()