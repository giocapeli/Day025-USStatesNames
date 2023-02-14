import turtle
import pandas

s = turtle.Screen()
s.bgpic('blank_states_img.gif')
s.title("US States name gme")

states_frame = pandas.read_csv('50_states.csv')
# print(states_frame)

for n in states_frame:
    print(n)

s.exitonclick()