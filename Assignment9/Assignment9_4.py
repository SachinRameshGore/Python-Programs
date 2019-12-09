from sys import *;

def main():
    print("Comparing Two File ")
    if len(argv) < 3:
        print("Invalid Number Of Argument ")
        print("Example :")
        print("python Assignment9_4.py FileName1 FileName2");
        print("Filename1 : Name Of the File ");
        print("FileName2 : Name Of the Second File")
        exit()
    file1 = open(argv[1],"r");
    file2 = open(argv[2],"r")
    flag = False
    for line1 in file1:
        for line2 in file2:
            if line1 == line2:
                pass
            else:
                print("File Contents Are Not Same");
                flag = True
            break
    if flag == False:
        print("File Contents Are same")

    file1.close();
    file2.close()

if __name__ == "__main__":
    main()