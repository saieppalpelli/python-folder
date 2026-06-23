from turtle import *
from colorsys import *
bgcolor("white")
speed(200)
h = 0
for i in range(2000):
    h += 0.0015
    color(hsv_to_rgb(h,1,1))
    goto(0,0)
    fd(i)
    circle(100,50)
    rt(10)
hideturtle()
done()