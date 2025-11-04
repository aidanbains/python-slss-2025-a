# Recursion
# Author: Aidan Bains
# 20 October

import turtle

t = turtle.Turtle()
screen = turtle.Screen()

# Dictionary to hold colors
LEAF_COLORS = {
    "spring": "#edafb8",
    "summer": "#85cb33",
    "winter": "#dcfffd",
    "fall": "#820933",
}


def draw_complicated_tree(level: int, branch_length: float):
    """Draw a recursive tree with more than 2 branches per level."""
    if level == 0:
        # Draw a leaf
        t.color(LEAF_COLORS["fall"])
        t.stamp()
        t.color("brown")
    else:
        t.forward(branch_length)
        # First branch (left)
        t.left(30)
        draw_complicated_tree(level - 1, branch_length * 0.7)
        # Second branch (middle)
        t.right(30)  # back to center
        draw_complicated_tree(level - 1, branch_length * 0.7)
        # Third branch (right)
        t.right(30)
        draw_complicated_tree(level - 1, branch_length * 0.7)
        # Return to center orientation
        t.left(30)
        # Go back to where we started
        t.backward(branch_length)


# Set up the turtle
t.left(90)
t.color("brown")
t.pensize(5)
t.shape("turtle")
t.penup()
t.goto(0, -180)
t.pendown()
draw_complicated_tree(5, 64)
screen.exitonclick()
