import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color = data["Primary Fur Color"]
grey = 0
cinnamon = 0

data_grey = data[data["Primary Fur Color"] == "Gray"] ## total rows which one having grey color
print(data_grey)

# for color in range(0,len(color)):
#     if(color == Grey):
#         grey+=1
#     elif(color == Cinnamon):
#         cinnamon+=1

# print(grey," ",cinnamon)
