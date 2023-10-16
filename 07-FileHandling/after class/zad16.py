# 16.	Find any text file on the Internet and download it to your computer. 
# Then write a program that copies the contents of this file to the copy.txt file. 
# Copy the contents of the file as a whole. Finally, open both files in any text editor and check that their contents are the same.

def copy_to_file(filename1: str, filename2: str) -> None:
    try:
        with open(filename1, 'r') as source, open(filename2,'w') as destination:
            destination.write(source.read())
    
    except:
        raise FileExistsError

def main() -> None:
    copy_to_file("filename.txt", 'copy.txt')

if __name__ == '__main__':
    main()