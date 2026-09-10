import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(3)

ขนาด_และ_สี = [(200, "red"), (160, "blue"), (120, "green"), (80, "orange"), (40, "purple")]

for ขนาด, สี in ขนาด_และ_สี:
    t.penup()
    t.goto(-ขนาด/2, -ขนาด/2)
    t.pendown()
    t.pencolor(สี)
    t.pensize(3)

    for i in range(4):
        t.forward(ขนาด)
        t.left(90)

turtle.done()
