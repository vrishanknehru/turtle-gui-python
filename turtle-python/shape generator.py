from turtle import Turtle, Screen 
from random import *

tim = Turtle()
tim.shape("arrow")
tim.color("black") 
colors = ['red', 'blue', 'green', 'orange', 'purple', 'pink', 'yellow','black']

for i in range(3,11):
        tim.pencolor(colors[i-3])
        for j in range(i):
            tim.forward(50)
            angle = 360/i
            tim.right(angle)
        
        

screen = Screen()
screen.exitonclick()  