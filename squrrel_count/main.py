import csv


"""with open("/Users/furkancinko/Desktop/weather_data.csv") as datas:
    data = csv.reader(datas)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)"""


import pandas

"""data = pandas.read_csv("/Users/furkancinko/Desktop/weather_data.csv")
temp_list = data["temp"].to_list()

total = 0
for i in temp_list:
    total += i

avarage = total / len(temp_list)
print(avarage)

print(data["temp"].max())
print(data.condition)

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print((monday.temp * 9) / 5 + 32) """""

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240312.csv")
color_list = data["Primary Fur Color"].to_list
type_of_color = data["Primary Fur Color"].unique()
print(type_of_color)

gray = data[data["Primary Fur Color"] == "Gray"]
cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
black = data[data["Primary Fur Color"] == "Black"]

squirrel_dict = {
    "colors": ["Gray", "Cinnamon", "Black"],
    "number": [f"{len(gray)}", f"{len(cinnamon)}", f"{len(black)}"]
}
data = pandas.DataFrame(squirrel_dict)
data.to_csv("squirrel_count.csv")
