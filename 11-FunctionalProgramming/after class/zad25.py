# 25.	Measuring stations recorded the following temperatures in degrees Celsius:
# {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
# Write a program that displays the names of towns where positive temperatures were recorded. 
# Use anonymous and filter() functions. Sample result:
# 	Cities with positive temperatures: Krakow Sopot Opole

def main() -> None:
    temps = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
    filtered_temps = dict(filter(lambda x: x[1] > 0, temps.items()))
    print(list(filtered_temps.keys()))

if __name__ == '__main__':
    main()