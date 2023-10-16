# 18.	Using any text editor, create the following two text files:
# MeatAndFish.txt
# Skinless white meat
# Tuna fish
# Luncheon meat
# Lean cuts of red meat
# GrainsAndBread.txt
# Bread
# Rice
# All purpose flour
# Breakfast cereal
# Pasta 
# Then write a program that creates a shoppinglist.txt file, in which save the contents of the MeatAndFish.txt and the GrainsAndBread.txt files.

def create_shopping_list(filename: str) -> None:
    content = []
    with open('MeatAndFish.txt', 'r') as maf:
        meat_and_fish = [line.strip() for line in maf.readlines()]

    with open('GrainsAndBread.txt', 'r') as gab:
        grains_and_bread = [line.strip() for line in gab.readlines()]
    
    with open(filename, 'w') as f:
        f.write('\n'.join(meat_and_fish + grains_and_bread))


def main() -> None:
    create_shopping_list('shoppinglist.txt')

if __name__ == '__main__':
    main()