#!/usr/bin/python3

import turtle

N = 9

def draw_circle() -> int:
    for i in range(360):
        turtle.forward(1)
        turtle.left(1)
    return 0

def main() -> int:
    turtle.shape("turtle")
    turtle.tracer(False)
    for i in range(N):
        draw_circle()
        turtle.left(360 / N)
    turtle.mainloop()
    return 0

if (__name__ == "__main__"):
    main()
