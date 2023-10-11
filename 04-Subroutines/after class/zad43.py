# 43.	A text contains any number of words. Define a function f(name) that returns the acronym 
# (first letters of all words). 
# Sample result:
# f("Internet of Things") returns "IoT"
# f("For Your Information") returns "FYI"
# f("Python") returns "P"

def f(name: str) -> str:
    words = name.split(" ")
    return ''.join([i[0] for i in words])

def main() -> None:
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))

if __name__ == '__main__':
    main()