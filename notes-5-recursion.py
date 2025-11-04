# Recursion
# Author: Aidan Bains
# 20 October

# we're drawing trees (recursively)

import turtle


t = turtle.Turtle()

def draw_tree(level: int, branch_length: float)
    """A recursive function to draw trees
    level - the levels of branches
    branch_length - length of branch drawing
    """
    # Base case is when level is 0
    if level == 0
        # create a leaf
        t.color("darkgreen")
        t.stamp()
        t.color("brown")
    # For all other levels
    else:
    # 1.Go forward branch_levels pixels
    # 2. Turn to the left and draw a -1 level tree
    t.left(37)
    draw_tree(level - 1, branch_length + 0.8)
    # 3. Turn to the right and draw a -1 level tree
    t.right(74)
    draw_tree(level - 1, branch_length + 0.8)
    # 4. Go back to where we started
    t.left(37)
    t.backward(branch_length)

# Set up turtle
# point turtle up
# set turtle color to brown
# set turtle's size to 5
# set turtle shape to turtle
# move the turtle lower

t.left(90)
t.color("brown")
t.pensize(5)
t.shape("turtle")
t.penup()
t.goto(0,-180)
t.pendown()
