from dataclasses import dataclass
from typing import Self
import re

# todo DECIMAL

# @dataclass
class BankAccount:
    PATTERN = '^\d{2} (\d{4} ){5}\d{4}$'
    # number: str = "DEFAULT NUMBER"
    # balance: float = 0.0
    # currency: str = "PLN"

    def __init__(self, number: str = 'DEFAULT NAME', balance: float = 0.0, currency: str = 'PLN') -> None:
        if not self.validate(number):
            raise ValueError('Numer konta jest nieprawidłowy.')
        self.number = number
        self.balance = balance
        self.currency = currency

    def display_information(self) -> None:
        print(f'Bank Account No: {self.number}')
        print(f'Balance: {self.currency} {self.balance}')
    
    def deposit(self, amount: float | int) -> None:
        if not isinstance(amount, float | int):
            raise ValueError('Please enter digit.')
        self.balance += amount
    
    def withdraw(self, amount: float | int) -> None:
        if not isinstance(amount, float | int):
            raise ValueError('Please enter digit.')
        if amount > self.balance:
            print('Insufficient funds on the account".')
        else:
            self.balance -= amount
    
    @staticmethod
    def validate(number: str):
        return re.match(BankAccount.PATTERN, number)
    
def main() -> None:
    acc = BankAccount('12 3456 5555 9090 1111 0000 7722')
    acc.display_information()
    acc.deposit(25.3)
    acc.display_information()
    acc.withdraw(31.7)
    acc.display_information()
    acc.withdraw(14)
    acc.display_information()

if __name__ == '__main__':
    main()