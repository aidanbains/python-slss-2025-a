# Turtle Artist
# Author: Aidan Bains
# # 28 October


import turtle

wn = turtle.Screen()
t = turtle.Turtle()

# Setup
t.speed(8)
t.color("lightblue")
t.pensize(3)
t.hideturtle()

# Draw mug
t.penup()
t.goto(-60, -100)
t.pendown()
t.color("saddlebrown", "peru")
t.begin_fill()
t.forward(120)
t.circle(80, 180)
t.forward(120)
t.circle(80, 180)
t.end_fill()

# Mug handle
t.penup()
t.goto(60, 0)
t.setheading(40)
t.pendown()
t.color("peru")
t.begin_fill()
t.circle(60, 200)
t.end_fill()

# Hot chocolate (inside)
t.penup()
t.goto(-50, 40)
t.pendown()
t.color("chocolate", "sienna")
t.begin_fill()
t.circle(70)
t.end_fill()

# Marshmallows
t.color("white")
for x, y in [(-30, 70), (0, 80), (30, 60)]:
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

# Steam lines
t.color("gray")
t.pensize(2)
steam_positions = [(-30, 110), (0, 120), (30, 110)]

for x, y in steam_positions:
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.pendown()
    for _ in range(3):
        t.circle(10, 60)
        t.circle(-10, 60)


# Setup screen
t.color("lightblue")
t.color("saddlebrown")
t.pensize(3)
t.hideturtle()
t.speed(5)

# Move turtle to start position
t.penup()
t.goto(-180, 0)
t.pendown()

# Write text
t.write("Hot Chocolate", font=("Arial", 48, "bold"))

# Keep window open


t.hideturtle()

wn.exitonclick()
