#!/usr/bin/python3

import turtle

N = 50

def main() -> int:
    turtle.shape("turtle")
    for i in range(1, N+1):
        for _ in range(2):
            turtle.forward(i * 10)
            turtle.left(90)
    return 0

if (__name__ == "__main__"):
    main()
