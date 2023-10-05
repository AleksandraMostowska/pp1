# A tree may be cut down if its diameter is at least 50 cm. Write a program that, based on the
# circumference of the tree entered from the keyboard, calculates and displays the value True
# if the tree can be cut down, or display the value False otherwise. Sample result:
# Enter tree circumference: … Tree can be cut down: …

def main() -> None:
    circumference = float(input('Enter tree circumference (in cm): '))
    
    can_be_cut_down = circumference >= 50
    
    print(f'Tree can be cut down: {can_be_cut_down}')

if __name__ == '__main__':
    main()
