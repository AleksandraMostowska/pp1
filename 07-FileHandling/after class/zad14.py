# 14.	Write a program that calculates the number of lines for any text file. 
# The user enters the name of the file from the keyboard. Display the result of the calculation (the file name and the number of lines). 
# Do not display the contents of the file. Sample result:
# File name: countries.txt
# Number of lines: 14

def count_lines(filename: str) -> int:
    print(f'File name: {filename}')
    with open(filename, 'r') as f:
        counter = len(f.readlines())
    print(f'Number of lines: {counter}')
    return counter

def main() -> None:
    filename = input('Enter filename: ')
    count_lines(filename)

if __name__ == '__main__':
      main()