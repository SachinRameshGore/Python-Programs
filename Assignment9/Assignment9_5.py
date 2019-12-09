from sys import *;
import filecmp

def main():
    if len(argv) < 3:
        print("Invalid Number Of Argument ")
        print("Example :")
        print("python Assignment9_4.py FileName1 String");
        print("Filename1 : Name Of the File ");
        print("String : Name Of the String to count Frequency ")
        exit()
    file1 = open(argv[1],"r");
    str = argv[2]
    count =0
    for line1 in file1:
        line1 = line1.split()
        for s in line1:
            if str == s:
                count = count +1
    print("Frequency Of ",str ,"Is :",count)
    file1.close()



if __name__ == "__main__":
    main()