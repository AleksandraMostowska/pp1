from dataclasses import dataclass, field

@dataclass
class Phone:
    brand: str
    model: str
    color: str
    memory: int
    is_turned_on = False
    contacts: list = field(default_factory=list)

    def __str__(self) -> str:
        return f'{self.brand} {self.model} {self.color} {self.memory}\nContacts: {self.contacts}'
    
    def turn_on(self):
        if not self.is_turned_on:
            self.is_turned_on = True
            print("The phone is turned on")
        
        else:
            print("The phone is already on")

    def turn_off(self):
        if self.is_turned_on:
            self.is_turned_on = False
            print("The phone is turned off")
        
        else:
            print("The phone is already off")
    
    def add_contact(self, contact: str):
        if contact not in contact:
            self.contacts.append(contact)
            print('Contact added')
        
        else:
            print('Such contact already exists.')
    

def main() -> None:
    p1 = Phone("Apple", "11", "white", 64)
    print(p1)
    p1.turn_on()
    p1.turn_on()
    p1.turn_off()
    p1.turn_off()

if __name__ == '__main__':
    main()