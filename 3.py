#!/usr/bin/python3

import turtle

def main() -> int:
    turtle.shape("turtle")
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    return 0

if (__name__ == "__main__"):
    main()
