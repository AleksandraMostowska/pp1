def bin_to_dec(num: str) -> int:
    num = num[::-1]
    result = 0
    for i in range(len(num)):
        if num[i] == '1':
            result += 2 ** i
    
    return result
    
def dec_to_bin(n: int) -> int:
    result = ''
    while n != 0:
        result += str(n % 2)
        n //= 2
    
    return result[::-1]

def main() -> None:
    print(bin_to_dec("0101"))
    print(dec_to_bin(13))

if __name__ == '__main__':
    main()