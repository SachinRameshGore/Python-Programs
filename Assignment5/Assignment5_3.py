def patternNumber(num):
    if  num != 0 :
        print(num, end=" ")
        patternNumber(num - 1)


def main():
    num = int(input("Enter The Number :"))
    patternNumber(num)


if __name__ == "__main__":
    main()
