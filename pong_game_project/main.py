from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Screen creation and setup
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

# Create paddles
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

# Create ball
ball = Ball()

# Move the paddle
screen.listen()
screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")
screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")

# Scoreboard creation
scoreboard = Scoreboard()

# Loop
is_game_on = True
interval = 0.1
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect wall collisions
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect paddle collisions
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if r_paddle misses ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if l_paddle misses ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
