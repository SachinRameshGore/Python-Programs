def patternNumber(num):
    if  num != 0 :
        patternNumber(num -1)
        print(num, end=" ")


def main():
    num = int(input("Enter The Number :"))
    patternNumber(num)


if __name__ == "__main__":
    main()
