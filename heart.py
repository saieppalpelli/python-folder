import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("A Question for You...")
screen.bgcolor("black")

# Set up the pen
t = turtle.Turtle()
t.speed(3)
t.color("red")
t.pensize(3)

# Function to draw a heart
def draw_heart():
    t.begin_fill()
    t.left(140)
    t.forward(224)
    for _ in range(200):
        t.right(1)
        t.forward(2)
    t.left(120)
    for _ in range(200):
        t.right(1)
        t.forward(2)
    t.forward(224)
    t.end_fill()

# Draw the heart
draw_heart()

# Write the proposal message
t.penup()
t.goto(0, -70)
t.color("white")
t.write("Will you marry me?", align="center", font=("Arial", 28, "bold"))

# Keep the window open
turtle.done()
