# 10.	Create a class that describes cell phones with at least 3 phone states and 2 behaviors. 
# Define the text representation of an object. Then create 2 objects representing 2 phones. 
# Display their features and call their bahaviors.

from dataclasses import dataclass

@dataclass
class Phone:
    color: str = "DEFAULT COLOR"
    brand: str = "DEFAULT BRAND"
    state: str = "OFF"

    def __str__(self) -> str:
        return f'Color: {self.color}\nBrand: {self.brand}\nState: {self.state}'

    def turn_on(self) -> None:
        if self.state == "OFF":
            self.state = "ON"
        else:
            print("Phone is already on.")
    
    def turn_off(self) -> None:
        if self.state == "ON":
            self.state = "OFF"
        else:
            print("Phone is already off.")
    
    def make_a_call(self, number: str) -> None:
        if self.state == "ON":
            print(f'Calling {number}...')
        else:
            print("Turn your phone on first.")

def main() -> None:
    phone1 = Phone("Apple", "iPhone 13")
    phone2 = Phone("Samsung", "Galaxy S21")

    print(phone1)
    print(phone2)

    phone1.turn_on()
    phone1.make_a_call("123-456-7890")
    phone1.turn_off()

    phone2.turn_on()
    phone2.make_a_call("987-654-3210")
    phone2.turn_off()
  

if __name__ == "__main__":
    main()