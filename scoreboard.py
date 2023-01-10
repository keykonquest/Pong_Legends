from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.player1_score = 0
        self.player2_score = 0
        self.player1_ticker(-50, 250)
        self.player2_ticker(50, 250)

    def make_net(self):
        self.goto(0, -300)
        self.setheading(90)
        for dash in range(0, 31):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()

    def player1_ticker(self, xposition, yposition):
        self.color("white")
        self.hideturtle()
        self.goto(xposition, yposition)
        self.write(f"{self.player1_score}", False, "center", ("Adobe Caslon Pro", 30, "normal"))

    def player2_ticker(self, xposition, yposition):
        self.color("white")
        self.hideturtle()
        self.goto(xposition, yposition)
        self.write(f"{self.player2_score}", False, "center", ("Adobe Caslon Pro", 30, "normal"))

    def player1_scored(self):
        self.clear()
        self.player1_score += 1
        self.make_net()
        self.penup()
        self.player1_ticker(-50, 250)
        self.player2_ticker(50, 250)


    def player2_scored(self):
        self.clear()
        self.player2_score += 1
        self.make_net()
        self.penup()
        self.player2_ticker(50, 250)
        self.player1_ticker(-50, 250)

