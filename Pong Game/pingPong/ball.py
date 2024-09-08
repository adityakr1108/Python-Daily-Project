from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 1
        self.dy = -1

    def move(self):
        x = self.xcor()
        y = self.ycor()
        if(x > 620 or x < -620):
            self.dx *= -1
        if(y > 300 or y < -300):
            self.dy *= -1
        self.goto(x + self.dx, y + self.dy)
        
