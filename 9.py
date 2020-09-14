#!/usr/bin/python3

import turtle
import math

L = 100

def draw(n: int) -> int:
    r = L / 2 / math.sin(2 * math.pi / n)
    turtle.penup()
    turtle.goto(r, 0)
    turtle.pendown()
    for i in range(1, n+1):
        turtle.goto(r * math.cos(2 * math.pi * i / n), r * math.sin(2 * math.pi * i / n))
    return 0

def main() -> int:
    turtle.shape("turtle")
    for i in range(3, 13):
        draw(i)
    return 0

if (__name__ == "__main__"):
    main()
