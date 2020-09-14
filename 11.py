#!/usr/bin/python3

import turtle

def circle(N: int) -> int:
    for i in range(360):
        turtle.forward(N)
        turtle.left(1)
    return 0

def main() -> int:
    turtle.shape("turtle")
    turtle.tracer(False)
    for i in range(1, 11):
        circle(i)
        turtle.left(180)
        circle(i)
        turtle.left(180)
    turtle.mainloop()
    return 0

if (__name__ == "__main__"):
    main()
