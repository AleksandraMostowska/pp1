# 31.	Write a program that, for the given array of real numbers, 
# displays the number of elements that are greater than the given value entered from the keyboard.

def main() -> None:
    arr = [0.87, 5.201, 0.366, 7.431215, 0.17, 3.4562]
    float_arr = [float(i) for i in arr]
    n = float(input('Enter number: '))
    print([i for i in float_arr if i > n])

if __name__ == '__main__':
    main()