# Create a function f(number, even) that computes the sum of the digits of a number. 
# When the value of the even parameter is True, the function returns the sum of the even digits. 
# When the value of the even parameter is False, the function returns the sum of the odd digits. 

def f(number: int, even: bool) -> int:
    return sum([int(i) for i in str(number) if int(i) % 2 == 0]) if even else sum([int(i) for i in str(number) if int(i) % 2 == 1])