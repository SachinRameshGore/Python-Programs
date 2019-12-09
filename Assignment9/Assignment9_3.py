from sys import *;

def main():
    if len(argv) < 3:
        print("Invalid Number Of Argument ")
        print("Example :")
        print("python Assignment9_3.py FileName1 FileName2");
        print("Filename1 : Name Of the File ");
        print("FileName2 : Name Of the Second File into which we copy the contents form Filename1")
        exit()
    fread = open(argv[1],"r");
    fwrite = open(argv[2],"w")

    fwrite.write(fread.read());
    fread.close();
    fwrite.close()

if __name__ == "__main__":
    main()