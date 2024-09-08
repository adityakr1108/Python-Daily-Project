from turtle import Screen, Turtle
from paddle import Paddle  # Import the Paddle class
from ball import Ball  # Import the Ball class

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1250, height=600)
screen.title("Pong Game")
screen.tracer(0)

# Create paddles
R_Paddle = Paddle(615, 275)  # Right paddle
L_Paddle = Paddle(-625, 275)  # Left paddle

# Middle line design
middle = Turtle()
middle.shape("square")
middle.color("white")
middle.shapesize(stretch_wid=4, stretch_len=1)

def middleDesign():
    for i in range(-300,300,100):  # Adjusted range to fit the screen
        middle.penup()
        middle.goto(0, i)
        middle.stamp()

middleDesign()


ball = Ball()  # Create the ball

# if(ball.score_Left()):
#     print("Left player scored", ball.score_Left())
# if(ball.score_Right()):
#     print("Right player scored", ball.score_Right())
# # Bind paddle movement to keys
screen.listen()
screen.onkey(R_Paddle.go_up, "Up")
screen.onkey(R_Paddle.go_down, "Down")
screen.onkey(L_Paddle.go_up, "w")
screen.onkey(L_Paddle.go_down, "s")

# Game loop
game_is_on = True
while game_is_on:
    ball.move()
    screen.update()

# Keep the window open
screen.mainloop()