# A variable contains your height in cm. Write a program that displays your height both in cm and in feet
# and inches. Sample result:
# I am 170cm tall, i.e. 5 feet and 7 inches

def main() -> None:
    h = 170

    feet = h // 30.48
    remaining_cm = h % 30.48
    inches = remaining_cm // 2.54

    print(f'I am {h}cm tall, i.e. {feet} feet and {inches} inches')

if __name__ == '__main__':
    main()