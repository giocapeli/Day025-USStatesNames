import turtle
import pandas

s = turtle.Screen()
s.title("US States name gme")
# s.bgpic('blank_states_img.gif')
s.addshape('blank_states_img.gif')

ts = turtle.Turtle()
ts.shape('blank_states_img.gif')

states_frame = pandas.read_csv('50_states.csv')
states_dict = states_frame.to_dict()
states_list = states_frame["state"].tolist()
# print(states_frame)

guessed_states = []

while len(guessed_states) < 50:    
    guess = s.textinput(title=f'{len(guessed_states)} of 50 States guessed right', prompt='Guess a US State:').title()
    
    if guess == 'Exit':
        missed_states = []
        for n in states_list:
            if n not in guessed_states:
                missed_states.append(n)
        save_dataframe = pandas.DataFrame(missed_states)
        save_dataframe.to_csv("missed_states.csv")
        break

    # print(data_with_pandas[data_with_pandas["temp"] == data_with_pandas["temp"].max()]) #it will print the item in a position that returns True
    # check = states_frame[states_frame["state"] == guess]

    if guess in states_list:
        print("Right")
        found_state = states_frame[states_frame["state"] == guess]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto((int(found_state['x']) , int(found_state['y'])))
        t.write(found_state['state'].item()) #it pick the item, or value, instead of the object of pandas
        guessed_states.append(guess)
    else:
        print("Wrong")

turtle.mainloop()
# s.exitonclick()