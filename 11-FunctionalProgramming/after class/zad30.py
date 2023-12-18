# 30.	In a beverage factory, a machine fills 500ml bottles. The computer checks whether the bottle has been filled correctly. 
# For a 500ml bottle, the allowable tolerance is 2%. In the last ten bottles checked, the filling was:
# 508,500,512,499,492,511,503,476,501,509
# Write a program that calculates the percentage of incorrectly filled bottles. Use the filter() along with a higher order function. 
# Sample result:
# Bottle capacity:    500ml
# Filling tolerance:  2%
# Filled bottles:     508,500,512,499,492,511,503,476,501,509
# Incorrectly filled: 30%

def main() -> None:
    filled_bottles = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]
    bottle_capacity = 500
    tolerance = 500 * 0.02

    def is_filled_correctly(fill: int) -> bool:
        return fill > (bottle_capacity + tolerance) or fill < (bottle_capacity - tolerance)
    
    filtered_bottles = list(filter(is_filled_correctly, filled_bottles))
    print(len(filtered_bottles) * 100 / len(filled_bottles))

if __name__ == '__main__':
    main()