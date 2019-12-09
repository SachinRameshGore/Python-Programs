from sys import *;

def main():
    if len(argv) < 2:
        print("Invalid Number Of Argument ")
        print("Example :")
        print("python Assignment9_2.py FileName");
        print("Filename : Name Of the File ");
        exit()
    fobj = open(argv[1],"r");
    print(fobj.read());
    fobj.close()

if __name__ == "__main__":
    main()