import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

# Set up Screen
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # Tracer controls the animation. 0 turns it off.

# Instantiating objects

paddle_right = Paddle(x=350, y=0)
paddle_left = Paddle(x=-350, y=0)
ball = Ball()

# Make screen listen to keystrokes

screen.listen()
screen.onkeypress(paddle_right.up, "Up")
screen.onkeypress(paddle_right.down, "Down")
screen.onkeypress(paddle_left.up, "w")
screen.onkeypress(paddle_left.down, "s")

# Running game

game_runs = True

while game_runs:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()


screen.exitonclick()
