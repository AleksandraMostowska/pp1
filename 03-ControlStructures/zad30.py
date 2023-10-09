# 30.	Write a program that allows you to convert time in 24-hour format to 12-hour format. The time in 
# 24-hour format (hh:mm) is read from the keyboard. Sample result:
# Enter time (24-hour format): 16:32
# Time in 12-hour format: 4:32pm

def get_time() -> None:
    time = input('Enter time (24-hour format): ')
    hours, mins = time.split(':')
    formatted_time = ''
    
    if int(hours) < 12:
        period = 'am'
    else:
        period = 'pm'
        hours = str(int(hours) - 12)
    
    formatted_time += hours + ':' + mins + period
    print(f'Time in 12-hour format: {formatted_time}')


def main() -> None:
    get_time()

if __name__ == '__main__':
    main()