#!/usr/bin/python3

import turtle

def star(N):
    for i in range(N):
        turtle.forward(100)
        turtle.left(180)
        turtle.right(180 / N)
    return 0

def main() -> int:
    turtle.shape("turtle")
    star(11)
    return 0

if (__name__ == "__main__"):
    main()
