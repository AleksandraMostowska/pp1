# 16.	A program contains two functions:
# a.	hotel_list(hotels) that returns a list of hotels names, separated by a comma sign
# b.	avg_price(hotels) that returns the average room price for a given list of hotels, rounded to an integer value
# c.	
# Write a program that calculates and displays the average price for a room in hotels in Krakow and Sopot 
# and indicates in which cities hotels are cheaper.
# Hotels_in_Krakow = [
#     {"name":"Sky","price":320.00},
#     {"name":"Metropol","price":480.00},
#     {"name":"New Port","price":420.00},
#         {"name":"Aparthotel","price":390.00}
# ]
# hotels_in_Sopot = [
#     {"name":"Focus","price":510.00},
#     {"name":"Aqua","price":345.00},
#     {"name":"La Boutique","price":390.00},
#     {"name":"Marina","price":410.00}
# ]
# Sample result:
# Hotels in Krakow: …,…,…,…
# Average hotel price in Krakow: …
# Hotels in Sopot: …,…,…,…
# Average hotel price in Sopot: …
# Cheaper hotels in: …

def hotel_list(hotels: dict) -> str:
    return ','.join([hotel["name"] for hotel in hotels])

def avg_price(hotels: dict) -> float:
    return sum([hotel["price"] for hotel in hotels]) / len(hotels)

def get_cheaper_city(d1: dict, d2: dict) -> str:
    d1_prices = avg_price(d1)
    d2_prices = avg_price(d2)

    return "Krakow" if d1_prices <= d2_prices else "Sopot"

def main() -> None:
    Hotels_in_Krakow = [
        {"name":"Sky","price":320.00},
        {"name":"Metropol","price":480.00},
        {"name":"New Port","price":420.00},
        {"name":"Aparthotel","price":390.00}
    ]
    hotels_in_Sopot = [
        {"name":"Focus","price":510.00},
        {"name":"Aqua","price":345.00},
        {"name":"La Boutique","price":390.00},
        {"name":"Marina","price":410.00}
    ]

    print(hotel_list(Hotels_in_Krakow))
    print(hotel_list(hotels_in_Sopot))

    print(avg_price(Hotels_in_Krakow))
    print(avg_price(hotels_in_Sopot))

    print(get_cheaper_city(Hotels_in_Krakow, hotels_in_Sopot))

if __name__ == '__main__':
    main()