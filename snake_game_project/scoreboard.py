from turtle import Turtle

# Constants
ALIGNMENT = "center"
FONT = ("Courier", 20, "italic")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=(0, 270))
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()


    def update_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER!!", align=ALIGNMENT, font=FONT)
