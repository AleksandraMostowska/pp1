# 40.	The 'university' variable contains the name of university where you are studying. Write a program that 
# displays the contents of the variable with an extra space between characters 
# (add a space between each character). Sample result:
# Krakow University of Economics
# K r a k o w   U n i v e r s i t y   o f   E c o n o m i c s 


def display() -> str:
    university = 'Krakow University of Economics'
    return " ".join([i for i in university])

def main() -> None:
    print(display())

if __name__ == '__main__':
    main()