#!/usr/bin/python3

import turtle

def draw_square(size: int) -> int:
    turtle.penup()
    turtle.goto(-size / 2, -size // 2)
    turtle.pendown()
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    return 0

def main() -> int:
    turtle.shape("turtle")
    for i in range(1, 11):
        draw_square(50 * i)
    return 0

if (__name__ == "__main__"):
    main()
