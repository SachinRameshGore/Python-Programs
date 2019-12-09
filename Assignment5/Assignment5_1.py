def pattern(num):
    if num != 0:
        print("*", end=" ")
        pattern(num - 1)


def main():
    num = int(input("Enter The Number :"))
    pattern(num)


if __name__ == "__main__":
    main()
