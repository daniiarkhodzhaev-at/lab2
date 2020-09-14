#!/usr/bin/python3

import turtle

def halfcircle(N):
    for i in range(180):
        turtle.forward(N)
        turtle.left(1)
    return 0

def main() -> int:
    turtle.shape("turtle")
    turtle.tracer(False)
    for i in range(10):
        halfcircle(3)
        halfcircle(1)
    turtle.mainloop()
    return 0

if (__name__ == "__main__"):
    main()
