import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)

# create def for when state's name is matched - it will write that out as a turtle on the screen
# at the passed in coordinates
def write_state_on_map(state, x, y):
    pass


# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

# create states_named variable - use for number of correct states the user names. set to start at 0
states_named = 0

# TODO import CSV file and create a pandas dictionary. state name is key - x and y are the values
# get the data from the CSV
state_data = pandas.read_csv("50_states.csv")

# convert the state data to a dictionary
state_dict = state_data.to_dict()
print(state_dict)

# create list of states_already_named[] and add in states as the user goes along
states_already_named = []

# TODO create pop up to ask for a state
answer_state = screen.textinput(title="Guess The State", prompt="What's a state's name?").lower()

# TODO create while loop - as long as state_count < 50 keep going
if states_named < 50:
    print(answer_state)
    answer_state_title = f'"{answer_state.title()}"'
    print(state_dict.state.get(answer_state_title))
    # check if state is on the state_already_named list.
    if state_dict.state.get(answer_state_title) is not None:
        print(answer_state_title)
        if answer_state not in states_named:
            states_named += 1
            print(states_named)
            states_already_named.append(answer_state)
            print(states_already_named)
            # TODO find upper case version of key
            x_value = state_dict.get("x")
            print(x_value)
            y_value = state_dict.get("y")
            print(y_value)
            # call function to write state name on the screen
            write_state_on_map(answer_state, x_value, y_value)
            # update answer_state
            answer_state = screen.textinput(title=f"{states_named}/50 states "
                                                  f"correct", prompt="What's another state's name?").lower()


turtle.mainloop()


# TODO check if answer_state is one of the states in 50_states.csv.
# if there's a match - create list of states_already_named[] and add in states as the user goes along

# if it is - do nothing and prompt for a new state
# if not - add state to the list and update count
#
# write the state's name out on the screen using the coordinates given
# make sure to use lower()
# if they entered a state that's been matched before - create list of states already correct
# and search that.
# TODO create variable to keep track of unique states answered
# TODO update screen.title with that variable to say "X/50 states correct"
# if there's no match - do nothing except offer the prompt again
