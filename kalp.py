import math
import turtle

t = turtle.Turtle()
t.speed(500)
turtle.bgcolor('black')

t.penup()
t.goto(0, 250)
t.pendown()
t.color('red')
t.write("Bebeğim Seni Seviyorum <3", align="center", font=("Arial", 20, "normal"))
t.penup()
t.goto(0, 0)
t.pendown()

def xt(t):
    return 16 * math.sin(t)**3

def yt(t):
    return 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)

for i in range(2550):
    t.goto((xt(i)*20, yt(i)*20))
    t.pencolor('purple')
    t.goto(0, 0)

turtle.done()
