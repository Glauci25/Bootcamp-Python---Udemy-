#with open("weather_data.csv", "r") as file:
#    dados = file.readlines()
#    print(dados)

'''
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperature = int(row[1])
            temperatures.append(temperature)
    print(temperatures)

'''

#import pandas
#um print super bonito
#data = pandas.read_csv("weather_data.csv")

'''
#Transforma em dicionário
data_dict = data.to_dict()
print(data_dict)

#Cálculo da média: jeito python básico
temp_list = data["temp"].to_list()
media = sum(temp_list)/len(temp_list)
print(f"A média é {media:.2f}.")

#Cálculo da média pelo pandas:
print(data["temp"].mean())

#Achando o maior valor pelo pandas:
print(data["temp"].max())
'''

#Get data conditions
#print(data.condition)

#Get data in a row
#print(data[data.day == "Monday"])
#print(data[data.temp == data.temp.max()])

#monday = data[data.day == "Monday"]
#monday_temp_fahrenheit = (monday.temp * 9/5) + 32
#print(monday_temp_fahrenheit)

#create a dataframe from scratch
#data_dict = {
 #   "students": ["Amy","James","Angela"],
  #  "scores": [76,56,65]
#}
#data = pandas.DataFrame(data_dict)
#data.to_csv("new_file.csv")

import pandas

data = pandas.read_csv("squirrel_data.csv")
grey_squirrel_count = data[data["Primary Fur Color"] == "Gray"]
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")


























