from dataclasses import dataclass
from typing import Self
from validator import ContactValidator

@dataclass
class Contact:
    name: str = 'DEFAULT NAME'
    email: str = 'DEFAULT EMAIL'
    telephone: str = '000000000'

    def __str__(self) -> str:
        tel = str(self.telephone)
        return f'{self.name:<15}{self.email:<20}{tel:<9}'
    
    # def __repr__(self) -> str:
    #     tel = str(self.telephone)
    #     return f'{self.name:<15}{self.email:<20}{tel:<9}'

    @classmethod
    def get_contact(cls, data: str) -> Self:
        if not ContactValidator.validate(data):
            raise ValueError('Wrong contact')
        contact_data = data.split(',')
        return cls(contact_data[0], contact_data[1], contact_data[2])
    
def main() -> None:
    data = 'John Brown,brown@onet.pl,555234000'
    c = Contact.get_contact(data)
    print(c)

if __name__ == '__main__':
    main()