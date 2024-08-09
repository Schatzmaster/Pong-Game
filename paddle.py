from turtle import Turtle

COLOR = "white"
UP = 90
DOWN = 270
SPEED = "fastest"
MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.speed(SPEED)
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.color(COLOR)
        self.penup()
        self.goto(x, y)
        self.setheading(UP)


    def create_paddle(self, x, y):
        """Creates a paddle object at given coordinates"""


    def down(self):
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)

    def up(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)


