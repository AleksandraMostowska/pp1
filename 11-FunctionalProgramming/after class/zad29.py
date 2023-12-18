# 29.	At one of the Olympic Games, the medal classification is as follows:
# {"country":"Denmark","gold":2,"silver":4,"bronze":6}
# {"country":"Finland","gold":5,"silver":0,"bronze":4}
# {"country":"USA","gold":12,"silver":5,"bronze":11}
# {"country":"Peru","gold":0,"silver":1,"bronze":7}
# Write a program that creates a bar chart showing the total number of medals won by each country. 
# Add a title for the chart and descriptions for the x and y axes. Tip: Use the map() function to create arrays of data for your chart.

import matplotlib.pyplot as plt

def main() -> None:
    countries = [
        {"country":"Denmark","gold":2,"silver":4,"bronze":6},
        {"country":"Finland","gold":5,"silver":0,"bronze":4},
        {"country":"USA","gold":12,"silver":5,"bronze":11},
        {"country":"Peru","gold":0,"silver":1,"bronze":7}
    ]

    x_values = [item["country"] for item in countries]
    y_values = [item["gold"] + item["silver"] + item["bronze"] for item in countries]

    plt.bar(x_values, y_values, color="pink")
    plt.title = "Olympics"
    plt.xlabels = "Countries"
    plt.ylabels = "Medals"

    plt.show()


if __name__ == '__main__':
    main()