
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("air_quality_no2.csv")
x_axis = "station_paris"

# Get the first ten items in the station_paris

x = df[x_axis].head(10)

# Change the Nan value to the name of the column(since we need a header to indicate the name of the column)

x.iloc[0] = x_axis

# Change the index to s/n

x = x.rename(index = {x.index[0]: "s/n"})
# print(x)

# Plot the bar chart
# This is to start from row 1 downward, since the first row is a string

plt.bar(x.index[1: ], x[1: ])
plt.title("Bar chart showing the values of the station_paris column")
plt.xlabel('Index')
plt.ylabel('station_paris')
plt.show()

