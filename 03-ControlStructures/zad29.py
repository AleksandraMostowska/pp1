# 29.	A washing machine allows you to wash a jacket, which takes 40 minutes, wash underwear, which takes 
# 70 minutes, and wash shoes, which takes 20 minutes. In addition, it is possible to program an additional rinse 
# (15 minutes) and an additional spin (9 minutes). The washing machine settings are saved in variables. 
# Write a program that calculates and displays the total washing time. Sample result:
# washing_product = "shoes"
# rinse = True
# spin = False
# Total washing time: 35 minutes

def main() -> None:
    washing_product = "shoes"
    rinse = True
    spin = False
    time = 0
    
    if washing_product == 'jacket':
        time += 40
    
    elif washing_product == 'underwear':
        time += 70
    
    elif washing_product == 'shoes':
        time += 20
    
    if rinse:
        time += 15
    if spin:
        time += 9
    
    print(f'Total washing time: {time} minutes')

if __name__ == '__main__':
    main()