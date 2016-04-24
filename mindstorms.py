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

def draw_square(turtle, length):
    """Draw square with given side length."""
    for side in xrange(0,4):
        turtle.forward(length)
        turtle.right(90)

def draw_triangle(turtle, length, fill):
    """Draw triange with given side length."""
    turtle.fill(fill)
    for side in xrange(0,3):
        turtle.forward(length)
        turtle.left(120)
    turtle.fill(False)

def draw_rand_squares(turtle):
    """Draws 4 squares in random sizes."""
    for square in xrange(0,4):
        multiple = random.randint(1,5)
        for side in xrange(0,4):
            turtle.forward(50*multiple)
            turtle.right(90)
        turtle.right(90)

def draw_circle_withsquares(turtle, radius, div):
    """Draws a circle by drawing rotating squares."""
    for i in xrange(0,div):
        draw_square(turtle, radius)
        turtle.right(360/div)

def draw_rhombus(turtle, length, squish):
    """Draws a diamond squished from a square by squish.

    Args:
        squish (float): Float between 0-1."""
    for i in xrange(0,2):
        turtle.forward(length)
        turtle.right(90-(90*squish))
        turtle.forward(length)
        turtle.right(90+(90*squish))

def draw_flower(turtle, radius, div):
    """Draws a flower circle using diamonds."""
    for i in xrange(0,div):
        draw_rhombus(turtle,radius/2,.3)
        turtle.right(360/div)
    turtle.right(90)
    turtle.forward(radius*2)

def draw_tri_fractal(turtle, length, level):
    """Draws a triangle fractal with given length and levels.

    Args:
        length (integer): A number that is a power of 2 for accuracy
        level (integer): Number >= 1."""
    if level == 1:
        draw_triangle(turtle, length, True)
        turtle.left(60)
        turtle.forward(length)
        turtle.right(60)
        draw_triangle(turtle, length, True)
        turtle.right(60)
        turtle.forward(length)
        turtle.left(60)
        draw_triangle(turtle, length, True)
        # Move turtle to starting point
        turtle.right(180)
        turtle.forward(length)
        turtle.right(180)
    else:
        draw_tri_fractal(turtle, length/2, level-1)
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
        turtle.right(120)
        draw_tri_fractal(turtle, length/2, level-1)
        turtle.forward(length)
        turtle.right(120)
        turtle.forward(length)
        turtle.left(120)
        draw_tri_fractal(turtle, length/2, level-1)
        # Move turtle to starting point
        turtle.right(180)
        turtle.forward(length)
        turtle.right(180)


if __name__ == '__main__':
    window = start()

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('#AEB','#164')
    brad.speed(0)

    # draw_square(100, 0)
    # draw_circle(100)
    # draw_triangle(150)
    # draw_circle_withsquares(brad, 100, 30)
    # draw_rhombus(brad, 100, .5)
    # draw_flower(brad, 100, 40)
    draw_tri_fractal(brad, 2**6, 4)

    window.exitonclick()
