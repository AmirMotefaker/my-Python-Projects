# Code by @AmirMotefaker

# Batman Logo


# Solution 1

import turtle
 
#get the turtle object and save it in bat variable
bat = turtle.Turtle()
 
#size of pointer and pen
bat.turtlesize(1, 1, 1)
bat.pensize(3)
 
#screen info
screen = turtle.Screen()
screen.bgcolor("dark blue")
screen.title("BATMAN Logo")
 
#change the color of pen
bat.color("yellow", "black")
 
 
#begin filling color
bat.begin_fill()
 
#turn1
bat.left(90)   # turn pointer direction to left of 90'
bat.circle(50, 85) #draw circle of radius = 50 and 85'
bat.circle(15, 110)
bat.right(180) 
 
#turn 2
bat.circle(30, 150)
bat.right(5)
bat.forward(10) #draw forward line of 10 units
 
#turn 3
bat.right(90)
bat.circle(-70, 140)
bat.forward(40)
bat.right(110)
 
#turn 4
bat.circle(100, 30)
bat.circle(30, 100)
bat.left(50)
bat.forward(50)
bat.right(145)
 
#turn5
bat.forward(30)
bat.left(55)
bat.forward(10)
 
#reverse
 
#turn 5
bat.forward(10)
bat.left(55)
bat.forward(30)
 
#turn 4
 
bat.right(145)
bat.forward(50)
bat.left(50)
bat.circle(30, 100)
bat.circle(100, 30)
 
#turn 3
bat.right(90)
bat.right(20)
bat.forward(40)
bat.circle(-70, 140)
 
#turn 2
bat.right(90)
bat.forward(10)
bat.right(5)
bat.circle(30, 150)
 
#turn 1
bat.left(180)
bat.circle(15, 110)
bat.circle(50, 85)
 
#end color filling
bat.end_fill()
 
#end the turtle method
turtle.done()



# Solution 2

# import turtle
# import math

# kalam = turtle.Turtle()
# kalam.speed(500)

# window = turtle.Screen()
# window.bgcolor("#000000")
# kalam.color("yellow")

# ankur = 20

# kalam.left(90)
# kalam.penup()
# kalam.goto(-7 * ankur, 0)
# kalam.pendown()

# for a in range(-7 * ankur, -3 * ankur, 1):
#     x = a / ankur
#     rel = math.fabs(x)
#     y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
#                 1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
#                     4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
#                         math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
#     kalam.goto(a, y * ankur)

# for a in range(-3 * ankur, -1 * ankur - 1, 1):
#     x = a / ankur
#     rel = math.fabs(x)
#     y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
#         math.fabs(rel - 1) / (rel - 1))
#     kalam.goto(a, y * ankur)

# kalam.goto(-1 * ankur, 3 * ankur)
# kalam.goto(int(-0.5 * ankur), int(2.2 * ankur))
# kalam.goto(int(0.5 * ankur), int(2.2 * ankur))
# kalam.goto(1 * ankur, 3 * ankur)
# print("Batman Logo with Python Turtle")
# for a in range(1 * ankur + 1, 3 * ankur + 1, 1):
#     x = a / ankur
#     rel = math.fabs(x)
#     y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
#         math.fabs(rel - 1) / (rel - 1))
#     kalam.goto(a, y * ankur)

# for a in range(3 * ankur + 1, 7 * ankur + 1, 1):
#     x = a / ankur
#     rel = math.fabs(x)
#     y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
#                 1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
#                     4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
#                         math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
#     kalam.goto(a, y * ankur)

# for a in range(7 * ankur, 4 * ankur, -1):
#     x = a / ankur
#     rel = math.fabs(x)
#     y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
#     kalam.goto(a, y * ankur)

# for a in range(4 * ankur, -4 * ankur, -1):
#     x = a / ankur
#     rel = math.fabs(x)
#     y = math.fabs(x / 2) - 0.0913722 * x ** 2 - 3 + math.sqrt(1 - (math.fabs(rel - 2) - 1) ** 2)
#     kalam.goto(a, y * ankur)

# for a in range(-4 * ankur - 1, -7 * ankur - 1, -1):
#     x = a / ankur
#     rel = math.fabs(x)
#     y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
#     kalam.goto(a, y * ankur)

# kalam.penup()
# kalam.goto(300, 300)
# turtle.done
