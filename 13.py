#!/usr/bin/python3

import turtle

def halfcircle(N, a=1):
    for i in range(180):
        turtle.forward(N)
        turtle.left(a)
    return 0

def main() -> int:
    turtle.shape("turtle")
    turtle.tracer(False)
    turtle.penup()
    turtle.goto(0,-200)
    turtle.pendown()
    turtle.begin_fill()
    halfcircle(5)
    halfcircle(5)
    turtle.color("#ffff00")
    turtle.end_fill()
    turtle.color("#000000")
    turtle.penup()
    turtle.goto(-100, 150)
    turtle.pendown()
    turtle.begin_fill()
    halfcircle(1)
    halfcircle(1)
    turtle.color("#0000ff")
    turtle.end_fill()
    turtle.color("#000000")
    turtle.penup()
    turtle.goto(100, 150)
    turtle.pendown()
    turtle.begin_fill()
    halfcircle(1)
    halfcircle(1)
    turtle.color("#0000ff")
    turtle.end_fill()
    turtle.color("#000000")
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.width(20)
    turtle.goto(0,0)
    turtle.penup()
    turtle.goto(110, -50)
    turtle.color("#ff0000")
    turtle.pendown()
    turtle.right(90)
    halfcircle(2,-1)
    turtle.penup()
    turtle.goto(10000,10000)
    turtle.mainloop()
    return 0

if (__name__ == "__main__"):
    main()
