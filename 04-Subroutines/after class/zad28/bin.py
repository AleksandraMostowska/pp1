import re

def f(bin_num: str) -> bool:
    return len(re.sub("[^01]", "", bin_num)) == len(bin_num)