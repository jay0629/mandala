#! /usr/bin/python3.5
import turtle
import random


def shapes():
    mandalaDraw = turtle.Turtle()
    turtle.Screen().bgcolor("gray")
    colorlist = ["pink", "blue", "orange", "purple", "red"]
    mandalaDraw.color("blue")
    for i in range(6):
        for i in range(2):
            mandalaDraw.forward(10)
            mandalaDraw.left(20)
            mandalaDraw.left(10)
            mandalaDraw.circle(100)
        mandalaDraw.color(random.choice(colorlist))
shapes()
