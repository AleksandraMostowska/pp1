# 26.	Measuring stations recorded the following temperatures in degrees Celsius:
# {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
# Write a program that creates a bar chart showing temperatures recorded in cities. Add a title for the chart and descriptions 
# for the x and y axes. Tip: use the map() function to create two arrays of data for the chart.

import matplotlib.pyplot as plt

# Temperature data
temperatures = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

# Extract city names and temperatures for the chart
cities = list(temperatures.keys())
temperatures_values = list(temperatures.values())

# Create a bar chart
plt.bar(cities, temperatures_values, color='pink')

# Add title and axis labels
plt.title('Temperatures Recorded in Cities')
plt.xlabel('Cities')
plt.ylabel('Temperature (°C)')

# Display the chart
plt.show()
