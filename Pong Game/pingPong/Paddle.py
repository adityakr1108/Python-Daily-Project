from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=6, stretch_len=1)
    # Function for A while moving up and down
    def go_up(self):
        y = self.ycor()
        y += 40
        if(y < 300):
            self.sety(y)
    def go_down(self):
        y = self.ycor()
        y -= 40
        if(y > -300):
            self.sety(y)

