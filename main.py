import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


# def get_mouse_click_cord(x, y):
#   print(x, y)

# turtle.onscreenclick(get_mouse_click_cord)
# turtle.mainloop()

data = pd.read_csv("50_states.csv")
answer_list = data["state"].to_list()
# print(answer_list)

is_game_on = True
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    answer_data = data[data["state"] == answer_state]

    if not answer_data.empty:
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        t.goto(int(answer_data.x), int(answer_data.y))
        t.write(answer_data.state.item())

        guessed_states.append(answer_data.state.item())


states_to_learn = [state for state in answer_list if state not in guessed_states]
df = pd.DataFrame(states_to_learn)
df.to_csv("states_to_learn.csv")

screen.exitonclick()
