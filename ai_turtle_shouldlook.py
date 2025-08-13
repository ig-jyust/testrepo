import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# Draw shell
t.penup()
t.goto(0, -100)
t.pendown()
t.color("darkgreen", "green")
t.begin_fill()
t.circle(100)
t.end_fill()

# Head
t.penup()
t.goto(0, 50)
t.pendown()
t.color("darkgreen", "lightgreen")
t.begin_fill()
t.circle(25)
t.end_fill()

# Eyes
for eye_x in [-10, 10]:
    t.penup()
    t.goto(eye_x, 80)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()

# Legs
leg_coords = [(-70, -30), (70, -30), (-50, -100), (50, -100)]
for x, y in leg_coords:
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("darkgreen", "green")
    t.begin_fill()
    t.circle(20)
    t.end_fill()

# Tail
t.penup()
t.goto(-10, -100)
t.setheading(-90)
t.pendown()
t.begin_fill()
t.circle(10, 180)
t.end_fill()

t.hideturtle()
turtle.done()
