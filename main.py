import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

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
scoreboard_left = Scoreboard(score=0, x_cor=-350, y_cor=265, align="left")
scoreboard_right = Scoreboard(score=0, x_cor=350, y_cor=265, align="right")
score_right = 0
score_left = 0

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
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if right paddle misses
    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard_left.clear()
        score_left += 1
        scoreboard_left = Scoreboard(score_left, x_cor=-350, y_cor=265, align="left")
        sleep_time = 0.1

    # Detect if left paddle misses
    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard_right.clear()
        score_right += 1
        scoreboard_right = Scoreboard(score_right, x_cor=350, y_cor=265, align="right")
        sleep_time = 0.1

screen.exitonclick()
