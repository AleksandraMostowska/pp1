def number_of_words(text: str) -> int:
    return len(text.split(" "))

def sorted_words(text: str) -> list[str]:
    words = text.split(' ')
    return sorted(words, key=len, reverse=True)

def sort_alphabetically(text: str) -> list[str]:
    return sorted(text.split(' '), key=str.lower)