# 36.	Write a program that checks whether the first array is a subset of the second one 
# (whether all elements of the first array appear in the second array).

def is_subset(arr1: [int], arr2: [int]) -> bool:
    # return set(arr2).issubset(set(arr1))

    # for i in arr1:
    #     if i not in arr2:
    #         return False
    
    # return True

    return [i for i in arr2 if i in arr1] == arr2

def main() -> None:
    a1 = [1, 2, 3, 4, 5]
    a2 = [1, 2, 3]
    print(is_subset(a1, a2))

if __name__ == '__main__':
    main()