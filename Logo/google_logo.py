# Code by @AmirMotefaker

# Google Logo


# Solution 1
# Step-by-Step code:
# 1- First, we have import the turtle library.
# 2- We have created a turtle object by turtle.
#    Turtle() method and save it in the variable t, now we will use t variable to draw lines, curves etc.
# 3- turtle.forward(distance) method is used draw a straight line.
# 4- turtle.right(angle) and turtle.left(angle) methods are used to rotate the turtle.
# 5- turtle.goto() method is used to reposition the pen.
# 6- t.penup() method is used to stop drawing i.e. pen up means now the pen is in up state.
# 7- t.pendown() method signals the pen to start drawing.
# 8- t.color() method is used to change the color of pen.
# 9- t.speed() method is used to change the drawing speed.
# 10- t.circle() method is used to draw circle with specified radius.

import turtle

t=turtle.Turtle()

#select color
t.color('#4285F4','#4285F4') ## RBG value of color

#change the pen size
t.pensize(5)

#change the drawing speed
t.speed(3)

t.forward(120)
t.right(90)
t.circle(-150,50)  ## first circle for red color
t.color('#0F9D58')
t.circle(-150,100)
t.color('#F4B400')
t.circle(-150,60)
t.color('#DB4437','#DB4437')

t.begin_fill()
t.circle(-150,100)
t.right(90)
t.forward(50)
t.right(90)
t.circle(100,100)
t.right(90)
t.forward(50)
t.end_fill()

t.begin_fill()

## second circle for yellow color
t.color("#F4B400","#F4B400")
t.right(180)
t.forward(50)
t.right(90)

t.circle(100,60)
t.right(90)
t.forward(50)
t.right(90)
t.circle(-150,60)
t.end_fill()


# third circle of green color
t.right(90)
t.forward(50)
t.right(90)
t.circle(100,60)
t.color('#0F9D58','#0F9D58')
t.begin_fill()
t.circle(100,100)
t.right(90)
t.forward(50)
t.right(90)
t.circle(-150,100)
t.right(90)
t.forward(50)
t.end_fill()


# Draw last circle
t.right(90)
t.circle(100,100)
t.color('#4285F4','#4285F4')
t.begin_fill()
t.circle(100,25)
t.left(115)
t.forward(65)
t.right(90)
t.forward(42)
t.right(90)
t.forward(124)
t.right(90)
t.circle(-150,50)
t.right(90)
t.forward(50)

t.end_fill()
turtle.write("@AmirMotefaker")
t.penup()



# Solution 2

import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
# t.speed()

t.color("#4285F4", "#4285F4")
t.pensize(3)
t.forward(120)
t.right(90)
t.circle(-150, 50)
t.color("#34A853")
t.circle(-150, 100)
t.color("#FBBC05")
t.circle(-150, 60)
t.color("#EA4335", "#EA4335")
t.begin_fill()
t.circle(-150, 100)
t.right(90)
t.forward(50)
t.right(90)
t.circle(100, 100)
t.right(90)
t.forward(50)
t.end_fill()
t.begin_fill()
t.color("#FBBC05", "#FBBC05")
t.right(180)
t.forward(50)
t.right(90)
t.circle(100, 60)
t.right(90)
t.forward(50)
t.right(90)
t.circle(-150, 60)
t.end_fill()
t.right(90)
t.forward(50)
t.right(90)
t.circle(100, 60)
t.color("#34A853", "#34A853")
t.begin_fill()
t.circle(100, 100)
t.right(90)
t.forward(50)
t.right(90)
t.circle(-150, 100)
t.right(90)
t.forward(50)
t.end_fill()
t.right(90)
t.circle(100, 100)
t.color("#4285F4", "#4285F4")
t.begin_fill()
t.circle(100, 25)
t.left(115)
t.forward(65)
t.right(90)
t.forward(42)
t.right(90)
t.forward(124)
t.right(90)
t.circle(-150, 50)
t.right(90)
t.forward(50)
t.end_fill()

t.up()
t.goto(100,100)
t.down()
turtle.color("White")
turtle.write("@AmirMotefaker")

t.hideturtle()
turtle.done()
