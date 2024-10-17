from turtle import Turtle

class SoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-400, 300)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))

    def update_score(self):
        self.level += 1
        print(self.level)
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))
        