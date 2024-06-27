


# from turtle import * (전체 임포트지만 웬만하면 지양)

##하나만 사용할때
# import turtle
# tim = turtle.Turtle()

# import turtle as t
# timmy = t.Turtle()

# import heroes
# print(heroes.gen())


from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("orange")

colors = ["black", "blue", "yellow"]

def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range(3,11):
    timmy.color(random.choice(colors))
    draw_shape(shape_side_n)


# for _ in range(20):
#     timmy.forward(10)
#     timmy.penup() #color("white")
#     timmy.forward(10)
#     timmy.pendown() #color("black")

#
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

