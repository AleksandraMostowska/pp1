# 23.	Define a function compare(array1, array2) that returns True if both arrays are the same.  
# Two arrays are the same if they have the same number of elements and values of elements in 
# cells of arrays with the same index are equal. Then create a program and try to compare the following arrays: 
# a.	["water","book","sky"]   ["water","book","sky"]
# b.	[True,False]   [True,False,True]
# c.	[5,3,1]   [5,3,1]
# d.	[3,2,1]   [3,2]
# Display both arrays and the result of comparison. Sample result:
# Array1: water book sky
# Array2: water book sky
# Comparison: arrays are the same

def compare(arr1: [int], arr2: [int]) -> bool:
    return arr1 == arr2

def display(arr: [int]) -> str:
    return ' '.join([str(i) for i in arr])

def main() -> None:
    arr1 = ["water","book","sky"]
    arr2 = ["water","book","sky"]
    arr3 = [True,False]   
    arr4 = [True,False,True]
    arr5 = [5,3,1]   
    arr6 = [5,3,1]
    arr7 = [3,2,1]   
    arr8 = [3,2]
    arrays = [[arr1, arr2], [arr3, arr4], [arr5, arr6], [arr7, arr8]]

    for a in arrays:
        print(f'Array1: {display(a[0])}')
        print(f'Array2: {display(a[1])}')
        print(f"Comparison: {'arrays are the same' if compare(a[0], a[1]) else 'arrays are not the same'}")

if __name__ == '__main__':
    main()