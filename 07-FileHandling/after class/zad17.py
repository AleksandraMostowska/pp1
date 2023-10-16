# 17.	Find any text file on the Internet and download it to your computer. 
# Then write a program that copies the contents of this file to the copylines.txt file. Copy the contents of the file line by line. 
# Finally, open both files in any text editor and check that their contents are the same.

def copy_to_file(sourse_file: str, destination_file: str) -> None:
    try:
        with open(sourse_file, 'r') as source, open(destination_file, 'w') as destination:
            for line in source:
                destination.write(line)
    except:
        raise FileExistsError

def main() -> None:
    copy_to_file("filename.txt", 'copy2.txt')

if __name__ == '__main__':
    main()