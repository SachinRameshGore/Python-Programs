sum1 = 0
def sum(num):
    global sum1
    if num != 0 :
        sum1 = sum1 + num % 10
        sum(num // 10)
        return sum1


def main():
    num = int(input("Enter The Number :"))
    ans = sum(num)
    print("Addition of digits is :",ans)


if __name__ == "__main__":
    main()
