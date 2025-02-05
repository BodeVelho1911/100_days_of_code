import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Scoreboard
scoreboard = Scoreboard()

# Car manager
car_manager = CarManager()

# Create player
player = Player()

# Detect player key press
screen.listen()
screen.onkeypress(fun=player.move, key="Up")

# Loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect successful crossing
    if player.detect_end_line():
        player.back_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
        print("You've reached end line, next level coming!")

    # Detect collisions with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
