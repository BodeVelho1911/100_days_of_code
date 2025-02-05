from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL_LOC = (-280, 250)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(LEVEL_LOC)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER!!", align="center", font=FONT)


