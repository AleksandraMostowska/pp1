# 25.	Define an anonymous function that returns True when the first number is greater 
# than the second one. Otherwise returns False. Use a conditional operator. 
# Then, check the function for pairs of numbers: 34, 25 and 19,23.

def main() -> None:
    fun = lambda x, y: True if x > y else False

    result1 = fun(34, 25)
    result2 = fun(19, 23)

    print(result1)  
    print(result2)  

if __name__ == '__main__':
    main()