# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

"""Simple computer graphics program.

Uses the turtle module to draw shapes."""

import turtle
import random

def start():
    window = turtle.Screen()
    window.bgcolor('#AEF')
    return window

def draw_square(length, angle):
    """Draw square with given side length."""
    brad = turtle.Turtle()
    brad.shape('square')
    brad.color('#164','#AEB')
    brad.speed(9)

    brad.right(angle)

    for side in xrange(0,4):
        brad.forward(length)
        brad.right(90)

    return brad

def draw_circle(radius):
    """Draw circle with given radius."""
    alex = turtle.Turtle()
    alex.shape('circle')
    alex.color('#833','#FBB')
    alex.speed(8)

    alex.circle(radius)

    return alex

def draw_triangle(length):
    """Draw triange with given side length."""
    cris = turtle.Turtle()
    cris.shape('triangle')
    cris.color('#146','#3AF')
    cris.speed(8)

    cris.right(180)
    for side in xrange(0,3):
        cris.forward(length)
        cris.left(120)

    return cris

def draw_circle_withsquares(radius):
    div = 20
    for i in xrange(0,div):
        draw_square(radius, 360/div * i)

def draw_rand_squares():
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('#164','#AEB')
    brad.speed(8)

    for square in xrange(0,4):
        multiple = random.randint(1,5)
        for side in xrange(0,4):
            brad.forward(50*multiple)
            brad.right(90)
        brad.right(90)

if __name__ == '__main__':
    window = start()
    # draw_square(100, 0)
    # draw_circle(100)
    # draw_triangle(150)

    draw_circle_withsquares(100)

    window.exitonclick()
