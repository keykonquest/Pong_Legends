from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle()
        self.y_axis = 0
        self.goto(position)

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        y_axis = self.ycor() + 20
        self.goto(self.xcor(), y_axis)

    def down(self):
        y_axis = self.ycor() - 20
        self.goto(self.xcor(), y_axis)
