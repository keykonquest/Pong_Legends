from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


def countdown(num):
    for count in range(1, num + 1):
        turt.write(f"{num}", False, "center", ("Adobe Caslon Pro", 100, "bold"))
        time.sleep(1)
        turt.clear()
        num -= 1
    turt.color("red")
    turt.write("PONG!", False, "center", ("Adobe Caslon Pro", 100, "bold"))
    time.sleep(1)
    turt.clear()


turt = Turtle()
turt.color("white")
turt.hideturtle()

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong: Legendary Ping Pong")
screen.tracer(0)

player1 = Paddle((-350, 0))
player2 = Paddle((350, 0))
countdown(3)
ball = Ball()

scoreboard = Scoreboard()
scoreboard.make_net()

screen.listen()
screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")
screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")

keep_ponging = True
while keep_ponging:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.player1_scored()
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.player2_scored()
    elif ball.distance(player2) < 50 and ball.xcor() > 320 or ball.distance(player1) < 50 and ball.xcor() < -320:
        ball.paddle_hit()

    if scoreboard.player1_score == 11:
        ball.clear()
        player1.clear()
        player2.clear()
        scoreboard.clear()
        turt.color("blue")
        turt.write("PLAYER 1 WINS!", False, "center", ("Adobe Caslon Pro", 100, "bold"))
        keep_ponging = False

    if scoreboard.player1_score == 11:
        ball.clear()
        player1.clear()
        player2.clear()
        scoreboard.clear()
        turt.color("red")
        turt.write("PLAYER 2 WINS!", False, "center", ("Adobe Caslon Pro", 100, "bold"))
        keep_ponging = False
