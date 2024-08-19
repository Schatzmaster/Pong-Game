from turtle import Turtle

ALIGN_left = "left"
FONT = "Arial"
SIZE = 16


class Scoreboard(Turtle):

    def __init__(self, score=0, x_cor=int, y_cor=int, align=str):
        super().__init__()
        self.goto(x=x_cor, y=y_cor)
        self.score = score
        self.penup()
        self.color("white")
        self.hideturtle()
        self.write(f"SCORE: {score}", align=align, font=(FONT, SIZE, "normal"),
                   move=False)
