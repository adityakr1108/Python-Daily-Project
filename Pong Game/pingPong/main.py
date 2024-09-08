# import PythonTurtle # type: ignore
from turtle import *
from Paddle import Paddle

# Screen
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=1250, height=600)
screen.tracer(0)


L_Paddle = Paddle((-650, 250))
R_Paddle = Paddle((650, 250))



# Middle line design
middle = Turtle()
middle.shape("square")
middle.color("white")
middle.shapesize(stretch_wid=4, stretch_len=1)
def middleDesign():
    for i in range(-600, 600, 100):
        middle.penup()
        middle.goto(0, i)
        middle.stamp()

middleDesign()


# BALL DESIGN

ball = Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0) 

ball.dx = 1  # Change in x
ball.dy = -1  # Change in y

def move_ball():
    x = ball.xcor()
    y = ball.ycor()
    # ball.setx(x + ball.dx)
    # ball.sety(y + ball.dy)



# Screen luisten according to the key
screen.listen()
screen.onkey(R_Paddle.go_up,"Up")
screen.onkey(R_Paddle.go_down,"Down")
screen.onkey(L_Paddle.go_up,"w")
screen.onkey(L_Paddle.go_down,"s")


# Gaem_is_ON
game_is_on = True
while game_is_on:
    move_ball()
    screen.update()


screen.mainloop()
screen.exitonclick()