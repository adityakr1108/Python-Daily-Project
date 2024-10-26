from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=7, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def go_up(self):
        y = self.ycor()
        y += 40
        if(y < 300):
            self.sety(y)

    def go_down(self):
        y = self.ycor()
        y -= 40
        if (y > -300):
            self.sety(y)