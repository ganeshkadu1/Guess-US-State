import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)
turtle.penup()

data = pandas.read_csv("50_states.csv")

total_state = 50
correctly_guess = 0
all_states = data.state.to_list()
guess_list = []

while total_state != correctly_guess:
    answer_state = screen.textinput(title=f"{correctly_guess}/{total_state} States Correct",
                                    prompt=f"What's another state's name ? ").title()

    if answer_state == "Exit":
        missing_state =[]
        for state in all_states:
            if state not in guess_list:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        print(new_data)
        break

    if answer_state in all_states:
        guess_list.append(answer_state)
        name = turtle.Turtle()
        name.penup()
        name.hideturtle()
        name.setx(int(data[data.state == answer_state].x))
        name.sety(int(data[data.state == answer_state].y))
        name.write(answer_state)
        screen.update()
        correctly_guess += 1
