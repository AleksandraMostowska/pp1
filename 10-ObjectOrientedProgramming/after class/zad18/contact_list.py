from dataclasses import dataclass, field
from contact import Contact

@dataclass
class Contact_List:
    contacts: list = field(default_factory=list)

    def add_contact(self, contact: str) -> None:
        try:
            self.contacts.append(Contact.get_contact(contact))
        except ValueError:
            print('Wrong contact input.')
    
    def display(self) -> None:
        print('Contact list: ')
        for c in self.contacts:
            print(c)

def main() -> None:
    c1 = 'John Brown,brown@onet.pl,555234000'
    c2 = 'Anna May,am@o2.pl,232000199'
    c3 = 'George Small,smallg@google.pl,222999100'
    c4 = 'Paola Big,bigpaola@poczta.pl,100200300'
    c_list = Contact_List()
    c_list.add_contact(c1)
    c_list.add_contact(c2)
    c_list.add_contact(c3)
    c_list.add_contact(c4)
    c_list.display()

if __name__ == '__main__':
    main()