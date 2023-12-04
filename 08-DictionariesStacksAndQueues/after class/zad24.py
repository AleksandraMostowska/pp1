# 14.	A dictionary contains course names along with the number of hours. Write a program that calculates 
# and displays the total number of hours. Sample results:
# winter_semester = {
#     "math":60,
#     "programming":30,
#     "history":15
# }
# The total number of hours in the winter semester is …

def count_hours() -> int:
    winter_semester = {
        "math":60,
        "programming":30,
        "history":15
    }

    return sum([int(i) for i in winter_semester.values()])

def main() -> None:
    print(count_hours())

if __name__ == '__main__':
    main()