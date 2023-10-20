# 9.	A test is passed when the number of correctly completed tasks is at least 50%. Write a program that checks whether the test is passed and displays the following information:
# Test passed
# The total number of test tasks and the number of correctly completed tasks are included in variables.

def main() -> None:
    number_of_tasks = 10
    number_of_correct = 7
    percentage = number_of_correct * 100 / number_of_tasks

    if percentage >= 50:
        print('Test passed')
    
if __name__ == '__main__':
    main()