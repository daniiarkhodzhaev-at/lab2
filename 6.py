#!/usr/bin/python3

import turtle

N = 12

def main() -> int:
    turtle.shape("turtle")
    for i in range(N):
        turtle.forward(100)
        turtle.stamp()
        turtle.backward(100)
        turtle.right(360 / N)
    return 0

if (__name__ == "__main__"):
    main()
