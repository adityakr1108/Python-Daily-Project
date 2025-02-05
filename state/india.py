import turtle
import pandas as pd
import time

screen = turtle.Screen()

# Screen Setup
screen.title("Guess India State Name")
screen.setup(500, 600)
screen.screensize(800, 600)
image = "india.gif"
screen.addshape(image)
turtle.shape(image)

india_data = {
    "state": [],
    "x": [],
    "y": []
}


# this below code is used for add the postion of the state to the new india csv file
# def get_mouse_click_coor(x, y):
#     print(x, y)
#     india_data["x"].append(x)
#     india_data["y"].append(y)
#     state_name = screen.textinput(title="Enter the state name", prompt="Enter the state name").lower()
#     india_data["state"].append(state_name)
    
#     # Save the data to a CSV file
#     df = pd.DataFrame(india_data)
#     df.to_csv("india_states.csv", index=False)

# turtle.onscreenclick(get_mouse_click_coor)

turtle_new = turtle.Turtle()
turtle_new.penup()

data = pd.read_csv("india_states.csv")
score = 0
chance = 2
game_is_on = True

while game_is_on:
    input_state = screen.textinput(title="Guess the U.S. State", prompt="What's another state name?")
    if input_state is None:  # If the user cancels the input dialog
        game_is_on = False
        turtle_new.hideturtle()
        turtle_new.goto(0, 220)  # Adjust the y-coordinate as needed to position the text at the top
        turtle_new.write(f"Good Bye, you have scored {score}. Thanks for playing..", align="center", font=("Arial", 12, "bold"))
        time.sleep(3)
        screen.bye()
        break

    found_state = False
    for index, row in data.iterrows():
        if row["state"].lower() == input_state.lower():  # Case insensitive comparison
            score += 1
            xcor = row["x"]
            ycor = row["y"]
            state_name = row["state"]
            turtle_new.goto(xcor, ycor)
            turtle_new.color("red")
            turtle_new.write(state_name,font=("Courier", 12, "bold"))
            turtle_new.color("black")
            found_state = True
            break

    if not found_state:
        chance -= 1
        if chance > 0:
            time.sleep(0.8)
            another_chance = screen.textinput(title=f"Do you want to try again? {chance} left", prompt="Yes or No").lower()
            if another_chance == "yes":
                game_is_on = True
            else:
                game_is_on = False
                turtle_new.hideturtle()
                turtle_new.goto(0, 220)  # Adjust the y-coordinate as needed to position the text at the top
                turtle_new.write(f"Good Bye, you have scored {score}. Thanks for playing..", align="center", font=("Arial", 12, "bold"))
                time.sleep(3)
                screen.bye()
        else:
            game_is_on = False
            turtle_new.hideturtle()
            turtle_new.goto(0, 220)  # Adjust the y-coordinate as needed to position the text at the top
            turtle_new.write(f"Good Bye, you have scored {score}. Thanks for playing..", align="center", font=("Arial", 12, "bold"))
            time.sleep(3)
            screen.bye()


turtle.mainloop()