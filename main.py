from turtle import Screen, Turtle
import random
import turtle

turtle.colormode(255)
turtle.bgcolor("beige")
t = Turtle()

colors = [
    (156, 156, 187), (20, 240, 238), (100, 100, 108),
    (46, 24, 123), (234, 123, 68), (90, 124, 65)
]

t.pu()
t.hideturtle()
t.speed("fastest")
t.setheading(225)
t.forward(400)
t.setheading(0)

num_dots = 100

for dot_count in range(1, num_dots + 1):
    t.dot(20, random.choice(colors))
    t.forward(60)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(60)
        t.setheading(180)
        t.forward(600)
        t.setheading(0)

s = Screen()

s.exitonclick()
