#!/usr/bin/python3

import turtle

def main() -> int:
    turtle.shape("turtle")
    for i in range(360):
        turtle.forward(1)
        turtle.left(1)
    return 0

if (__name__ == "__main__"):
    main()
