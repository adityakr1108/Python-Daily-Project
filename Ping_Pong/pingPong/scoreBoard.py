from turtle import Turtle
from ball import Ball
class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_Scoreboard()
        
    def update_Scoreboard(self):
        self.clear()
        self.goto(-100,280)
        self.write("Player 1: {}".format(self.l_score),align = "center",font = ("Courier",20,"normal"))
        self.goto(100,280)
        self.write("Player 2: {}".format(self.r_score),align = "center",font = ("Courier",20,"normal"))

    def update_L_Score(self):
        self.l_score+=1
        self.update_Scoreboard()

    def update_R_Score(self):
        self.r_score+=1
        self.update_Scoreboard()
    def gameReset(self):
        ball = Ball()
        if(self.l_score > self.r_score):
            self.goto(0,0)
            self.write(f"Game Over: Player 1 wins with {self.l_score - self.r_score}",align = "center",font = ("Courier",20,"normal"))
        else:
            self.goto(0,0)
            self.write(f"Game Over: Player 2 wins with {self.r_score - self.l_score}",align = "center",font = ("Courier",20,"normal"))
        self.l_score = 0
        self.r_score = 0
        ball.x_move = 10
        ball.y_move = 10
        self.update_Scoreboard()
        