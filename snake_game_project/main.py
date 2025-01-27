from turtle import Screen
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food

# Constants
LIMIT_CORD = 280

# Screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
scoreboard = Scoreboard()

# Create the snake body
snake = Snake()

# Move the snake
screen.listen()
screen.onkey(fun=snake.face_up, key="Up")
screen.onkey(fun=snake.face_down, key="Down")
screen.onkey(fun=snake.face_right, key="Right")
screen.onkey(fun=snake.face_left, key="Left")

food = Food()
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collisions with food
    if snake.head.distance(food) < 15:
        food.refresh_loc()
        snake.extend()
        scoreboard.increase_score()

    # Detect collisions with walls
    if snake.head.xcor() > LIMIT_CORD or snake.head.ycor() > LIMIT_CORD or snake.head.xcor() < -LIMIT_CORD or snake.head.ycor() < -LIMIT_CORD:
        is_game_on = False
        scoreboard.game_over()

    # Detect tail collisions
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()


screen.exitonclick()
