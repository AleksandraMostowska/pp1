# 15.	Find any text file on the Internet that contains at least 30 lines of text and download that file to your computer. 
# Then write a program that displays the first five lines from the file and then waits for the Enter key to be pressed. 
# Then repeat displaying the next five lines from the file, waiting for the Enter key to be pressed each time.

def read_from_file(filename: str) -> None:
    with open(filename, 'r') as f:
        lines = f.readlines()
        all_lines = len(lines)
        current_line = 0

        while current_line < all_lines:
            for i in range(current_line, current_line + 5):
                if i < all_lines:
                    print(lines[i].strip())
                
            input('Press Enter to continue\n')

            current_line += 5
            

def main() -> None:
    read_from_file("filename.txt")

if __name__ == '__main__':
    main()