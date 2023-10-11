# 36.	A device in a door registers people entering and leaving a room. The + sign means a person entering a room 
# and the – sign a person leaving a room. Define the function f(detector) that returns True if at least 3 people 
# were in the room at the same time, or False otherwise. Sample result:
# f("+-+++-+---") returns True
# f("+-+-+-+-") returns False
# f("+-++-+--") returns False
# f("+-++-++-+---") returns True

def f(detecor: str) -> bool:
    howManyInTheRoom = 0
    for i in range(len(detecor)):
        if detecor[i] == "+":
            howManyInTheRoom += 1
        elif detecor[i] == "-":
            howManyInTheRoom -= 1
        if howManyInTheRoom >= 3:
            return True
    return False

def main() -> None:
    print(f("+-+++-+---"))
    print(f("+-+-+-+-"))
    print(f("+-++-+--")) 
    print(f("+-++-++-+---"))

if __name__ == '__main__':
    main()
