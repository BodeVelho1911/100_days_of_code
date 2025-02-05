from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.back_to_start()
        self.setheading(90)

    def move(self):
        """Move player by MOVE_DISTANCE amount"""
        self.forward(MOVE_DISTANCE)

    def detect_end_line(self):
        """Detect if player has reached the finish line, if yes return True,
        otherwise return False"""
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

    def back_to_start(self):
        self.goto(STARTING_POSITION)
