from turtle import Screen, Turtle
import time
from player import Player
from cars import random_cars

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width = 600, height  = 600)

player = Player()
random_cars = random_cars()
# Screen on Key
screen.listen()
screen.onkey(player.go_to, "Up")

game_is_on = True
while(game_is_on):
    time.sleep(0.1)
    random_cars.create_car()
    random_cars.move_car()
    screen.update()
screen.exitonclick()
