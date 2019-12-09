from sys import *
import os


def FileRename(DirectoryName):
    flag = os.path.isabs(DirectoryName)
    if flag == False:
        DirectoryName = os.path.abspath(DirectoryName)
    flag = os.path.isdir(DirectoryName)
    if flag == False:
        print("It IS Not Directory  ")
        exit()
    count = 0

    print("_________________________________________________________________")
    src_files = os.listdir(DirectoryName)
    print(src_files)
    for Folder, SubFolder, files in os.walk(DirectoryName):
        print("_________________________________________________________________")
        print("Folder Name is")
        print(Folder)
        for i in range(len(src_files)):
            s1 = os.path.join(Folder,src_files[i])
            print(os.path.abspath(s1))
            s=src_files[i].replace('Marvellous Infosystems Python','')
            sa = os.path.join(Folder,s)
            print(os.path.abspath(sa))
            os.rename(s1,sa)



def main():
    print("This Script Is Used For Directory File Search With Specific FileExtension")
    if (len(argv) !=2):
        print("Invalid Number Of Arguments ")
        print("Please use -h or -u for help and usage ");
        exit()
    if argv[1].lower() == "-h":
        print("This Script is Used For Changing the file Extension from directory ");
        print("Example :")
        print("python Filename Extension1 Extension2")
        print("python DirectoryRename.py .txt .doc")
        exit()
    if argv[1].lower() == "-u":
        print("This Script is Used For Changing the file Extension from directory")
        exit()

    DirectoryName = argv[1]

    FileRename(DirectoryName)


if __name__ == "__main__":
    main();
