import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color = data["Primary Fur Color"]
grey = 0
cinnamon = 0

data_grey = len(data[data["Primary Fur Color"] == "Gray"]) ## total rows which one having grey color
print("Total no of grey color squirall",data_grey)


data_cinnamon  = len(data[data["Primary Fur Color"] == "Cinnamon"]) ## total rows which one having cinnamon color

print("Total no cinnamon color squirall",data_cinnamon)

data_black  = len(data[data["Primary Fur Color"] == "Black"]) ## total rows which one having  Black color

print("Total no cinnamon color squirall",data_black)


data_frame = {
    "fur Color" : ["Grey","Cinnamon","Black"],
    "Count" : [data_grey,data_cinnamon,data_black]
}

df = pd.DataFrame(data_frame)  # for conversion of dictionary to data frame

df.to_csv("squirall_count_through_color.csv")  # for creating a new csv file
