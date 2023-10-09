# 37.	Write a program that creates the following pattern. Sample result:
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

def main() -> None:
    for i in range(1, 6):
        print('*' * i)
    
    for j in range(4, 0, -1):
        print('*' * j)

if __name__ == '__main__':
    main()