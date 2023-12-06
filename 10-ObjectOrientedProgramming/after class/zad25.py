# 25.	A stadium is divided into sectors, each marked with a letter. There is a certain number of fans in each sector. 
# Define the class C, which allows you to create an object representing the stadium with a list of sectors and the number 
# of fans in sectors. Data, as a dictionary, should be transferred to the object at the time of its creation. 
# Define in the class a method m1(s,n) that allows you to change the number of fans n in sector s or add 
# a new sector s with the given number of fans n. Define in the class a method m2(s) that returns the sum of fans 
# in the sectors listed in the string s. Sample result:
# C({"A":120,"D":150,"G":90,"K":110})
# m1("G",130)
# m2("GD") returns 280
# m2("KEJ") returns 110

from dataclasses import dataclass, field

@dataclass
class C:
    sectors: dict[str, int] = field(default_factory=dict)

    def __str__(self) -> str:
        return f'{self.sectors}'

    def m1(self, s: str, n: int):
        self.sectors.update({s: n})

    def m2(self, sec: str):
        return sum([self.sectors[i] for i in sec if i in self.sectors])

def main() -> None:
    s = C({"A":120,"D":150,"G":90,"K":110})
    print(s)
    s.m1("G", 130)
    print(s)
    s.m1("L", 70)
    print(s)

    print(s.m2("GD"))
    print(s.m2("KEJ"))

if __name__ == '__main__':
    main()