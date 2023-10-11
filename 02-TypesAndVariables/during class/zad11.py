# 11.	Write a program that calculates and displays the income of a family per person. 
# To display the results in a readable form, use f-strings. Sample result:
# Enter father’s income: …
# Enter mother’s income: …
# Enter number of people in family: …
# Total income: …
# Income per person: … 

def main() -> None:
    f_ic = int(input('Enter fathers income: '))
    m_ic = int(input('Enter mothers income: '))
    members = int(input('Enter number of people in family: '))
    print(f'Total income: {f_ic + m_ic}')
    print(f'Income per person: {(f_ic + m_ic) / members}')

if __name__ == '__main__':
    main()