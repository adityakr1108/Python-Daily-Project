from turtle import Screen, Turtle
from player import Player
from cars import random_cars
from scoreCard import SoreBoard
import time
from special_abilities import create_power_ups

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width = 600, height  = 600)

player = Player()
score = SoreBoard()
cars = random_cars()
# Screen on Key
screen.listen()
screen.onkey(player.go_to, "Up")


text_turtle = Turtle()
text_turtle.hideturtle()
text_turtle.penup()
game_is_on = True
while(game_is_on):
    time.sleep(0.1)
    cars.create_car()
    cars.move_car()
    screen.update()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            text_turtle.goto(0, 0)
            text_turtle.color("white")
            text_turtle.clear()
            text_turtle.write("Game Over", align="center", font=("Arial", 24, "normal"))
            print("Game Over")
        # screen.bye()
        # break
        elif(player.ycor() > 300):
            player.go_to_start()
            score.update_score()
            cars.increaseSpeed()
            game_is_on = True
screen.exitonclick()
