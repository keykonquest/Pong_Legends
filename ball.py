import turtle
from turtle import Turtle
import random
turtle.colormode(255)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.shape("square")
        self.ball_color = self.color((255, 255, 255))
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.ball_color = self.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.y_move = self.y_move * -1

    def paddle_hit(self):
        self.ball_color = self.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.x_move = self.x_move * -1
        self.ball_speed = self.ball_speed / .9

    def reset_position(self):
        self.ball_color = self.color(255, 255, 255)
        self.ball_speed = 0.1
        self.goto(0, 0)
        self.x_move = self.x_move * -1
