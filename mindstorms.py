# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

"""Simple computer graphics program.

Uses the turtle module to draw shapes.

"""

import turtle
import random

def draw_square():
    window = turtle.Screen()
    window.bgcolor('#AEF')

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

    window.exitonclick()

if __name__ == '__main__':
    draw_square()
