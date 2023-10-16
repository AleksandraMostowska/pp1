# 23.	The announcement regarding the temperature forecast in degrees Celsius for the next three days was published on the Internet:
# "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
# Create a program that calculates the average temperature. Use regular expressions to extract the values of temperatures from the message.
# import re

# message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
# temperatures = re.findall("\d{2}",message)
# complete the program code
# ...

import re

def get_avg(temps: list[str]) -> float:
    numbers = [float(temp) for temp in temps]
    return sum(numbers) / len(numbers)

def main() -> None:
    message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
    temperatures = re.findall(r'\d{2}', message)
    print(temperatures)
    print(get_avg(temperatures))

if __name__ == '__main__':
    main()