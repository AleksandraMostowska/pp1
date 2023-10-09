# 23.	Write a program that calculates a dog's age in dog’s years. For the first two years, a dog's life 
# is equal to 10.5 human years. After that, each dog year is equal to 4 human years. Sample result:
# Enter the dog's age in human years: 15
# The dog's age in dog’s years is 73 years.


def countDogYears() -> float:
    years = int(input("Enter the dog's age in human years: "))
    count = 0.0
    if years <= 2:
        count += years * 10.5
    
    else:
        count += 21 + (years - 2) * 4
    
    return count

def main() -> None:
    print(countDogYears())

if __name__ == '__main__':
    main()