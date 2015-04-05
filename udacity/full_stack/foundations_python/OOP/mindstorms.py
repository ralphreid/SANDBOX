__author__ = 'ralph'

import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    # Create the turtle brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("triangle")
    brad.color("black")
    brad.speed("fast")
    draw_square(brad)
    # Create the turtle Angie - Draws a circle
    angie = turtle.Turtle()
    angie.color("blue")
    angie.shape("arrow")
    angie.circle(100)

    window.exitonclick()

draw_square()
