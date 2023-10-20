def get_nth_odd_num(x: int, n: int) -> int:
    num = 1
    nums = [1]
    while len(nums) < n:
        candidate = num + x
        if candidate % 2 == 1:
            nums.append(candidate)
        num += x
    
    return nums[-1]

def main() -> None:
    print(get_nth_odd_num(2, 8))
    print(get_nth_odd_num(3, 4))

if __name__ == '__main__':
    main()