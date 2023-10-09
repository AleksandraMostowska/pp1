# 41.	The payment card is secured with a four-digit PIN code (0805). 
# Write a program that checks if the PIN code entered in the payment terminal is correct. 
# The user has up to three possibilities for entering a PIN code. 
# In case of three unsuccessful attempts, the card is blocked. Sample result:
# Enter the PIN code: 2398
# Incorrect...
# Enter the PIN code: 0912
# Incorrect...
# Enter the PIN code: 7860
# Incorrect...
# Sorry, your payment card has been blocked.


def verify_PIN() -> None:
    PIN_code = '0805'
    for i in range(3):
        attempt = input("Enter the PIN code: ")
        if attempt != PIN_code:
            print('Incorrect...')
        else:
            break
    
    if attempt != PIN_code:
        print('Sorry, your payment card has been blocked.')


def main() -> None:
    verify_PIN()

if __name__ == '__main__':
    main()
