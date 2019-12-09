fptr = lambda no: no ** 2

def main():
    num = int(input("Enter the Number :"))
    ans = fptr(num)
    print("Power of ", num, " Is :", ans)


if __name__ == "__main__":
    main()