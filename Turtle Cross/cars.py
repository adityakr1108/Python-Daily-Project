from turtle import Turtle
import random

import time
MOVE_DISTANCE = 5
car_color = ["red", "blue", "green", "yellow", "orange", "purple", "brown", "pink", "cyan",
             "magenta", "lime", "maroon", "navy", "olive", "teal", "violet", "indigo", "gold", "silver"]
class random_cars:
    def __init__(self):
        self.all_cars = [] 
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(car_color))
            new_car.penup()
            random_y = random.randint(-250,250)
            new_car.goto(600,random_y)
            self.all_cars.append(new_car)
    def move_car(self):
        for car in self.all_cars:
            car.backward(MOVE_DISTANCE)
    
    def increaseSpeed(self):
        global MOVE_DISTANCE
        MOVE_DISTANCE += 3



    
    