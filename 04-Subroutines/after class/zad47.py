# 47.	Define a function f(text) that returns the given text with all characters separated 
# by "-" (minus sign). 
# Example:
# f("Univesity") returns "U-n-i-v-e-r-s-i-t-y"
# f("UE") returns "U-E"
# f("x") returns "x"
# f("") returns ""

def f(text: str) -> str:
    return '-'.join([i for i in text])

def main() -> None:
    print(f("Univesity")) 
    print(f("UE"))
    print(f("x"))
    print(f(""))

if __name__ == '__main__':
    main()