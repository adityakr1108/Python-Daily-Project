from turtle import Turtle

STARTING_POSITION = (0, -300)
MOVE_FORWARD = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.penup()
        self.color("white")


    def go_to(self):
        self.forward(MOVE_FORWARD)

    def go_to_start(self):
        self.goto(STARTING_POSITION)