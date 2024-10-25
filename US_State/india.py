import turtle
import pandas as pd
import time

screen = turtle.Screen()

# Screen Setup
screen.title("Guess India State Name")
screen.setup(800, 600)
screen.screensize(800, 600)
image = "india.gif"
screen.addshape(image)
turtle.shape(image)

india_data = {
    "state": [],
    "x": [],
    "y": []
}

def get_mouse_click_coor(x, y):
    print(x, y)
    india_data["x"].append(x)
    india_data["y"].append(y)
    state_name = screen.textinput(title="Enter the state name", prompt="Enter the state name").lower()
    india_data["state"].append(state_name)
    
    # Save the data to a CSV file
    df = pd.DataFrame(india_data)
    df.to_csv("india_states.csv", index=False)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()