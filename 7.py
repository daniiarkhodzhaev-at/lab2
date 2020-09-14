#!/usr/bin/python3

import turtle
import math
import random

k = 0.1

def main() -> int:
    turtle.shape("turtle")
    for i in range(5000):
        turtle.goto(k * i * math.cos(i * math.pi / 180), k * i * math.sin(i* math.pi / 180))
        turtle.left(random.randint(-10, 11))
    return 0

if (__name__ == "__main__"):
    main()
