from turtle import *
import turtle

screen = turtle.Screen()
t = turtle.Turtle()
s = 1
colours = turtle.Turtle()
box = turtle.Turtle()

turtles = {
    "Red" : -15,
    "Blue" : 5,
    "Green" : 25,
    "Orange" : 45,
    "Black" : -35,
    "Gray" : -55,
    "white": 65,
    "White": 85
}

box.up()
box.ht()
box.setpos(-1000,440)
box.down()
box.forward(2000)

for colour,x in turtles.items():
    colours.ht()
    colours.speed(0)
    colours.penup()
    colours.shape('square')
    colours.color("Black",colour)
    colours.setpos(x, 450)
    colours.stamp()
    colours.pendown()
    colours.st()
screen.tracer(0)

def drag(x, y):
    if 430 > y:
        t.setheading(t.towards(x, y))
        t.goto(x, y)
        t.ondrag(drag)
        screen.update()
    else:
        t.pu() # too cold ez win🥶
        t.undo()
        t.pd()


def button(x, y):
    global s
    if 440 > y:
        t.up()
        t.setheading(t.towards(x, y))
        t.setpos(x, y)
        t.down()
        screen.update()
    else:
        if y >= 440 and y <= 460:
            if x > - 65 and x < -45:
                t.clear()
                s = 1
                t.pensize(s)
                t.color('Black')
            if x > -45.1 and x < -25:
                t.color('Black')
                t.pensize(s)
            if x > -25.1 and x < -5:
                t.color('Red')
                t.pensize(s)
            if x > -5.1 and x < 10:
                t.color('Blue')
                t.pensize(s)
            if x > 10.1 and x < 35:
                t.color('Green')
                t.pensize(s)
            if x > 35.1 and x < 55:
                t.color('Orange')
                t.pensize(s)
            if x > 55.1 and x < 75:
                t.color("White","Black")
                t.pensize(15)
            if x > 75.1 and x < 95:
                s += 1
                if s > 10:
                    s = 1
                t.pensize(s)
    screen.update()

def main():
    listen()
    t.ondrag(drag)
    onscreenclick(button, 1)
    mainloop()
main()