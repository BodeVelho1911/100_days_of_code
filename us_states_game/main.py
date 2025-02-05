import turtle as t
from turtle import Turtle

import pandas as pd

# Screen settings
screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

# Turtle for writing names
name_write = Turtle()
name_write.hideturtle()
name_write.penup()

# Data structure
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

# Loop
guessed_states = []
while len(guessed_states) < 50:
    # Asks user to guess state's name
    user_guess = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                  prompt="What's another state's name?").title()

    # Check if guessed right
    if user_guess in all_states:
        guessed_states.append(user_guess)
        x_coord = data[data["state"] == user_guess].x.item()
        y_coord = data[data["state"] == user_guess].y.item()
        name_write.goto(x=x_coord, y=y_coord)
        name_write.write(user_guess)

    if user_guess == "Exit":
        # States missing saved to .csv
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
