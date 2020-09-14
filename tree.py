#!/usr/bin/python3

import turtle

N = 10
L = 100
k = 1 / 2 ** .5
angl = 30

def dfs(N: int, a: float) -> int:
    if (N == 0):
        return 0
    turtle.forward(a)
    turtle.left(angl)
    dfs(N - 1, k * a)
    turtle.right(2 * angl)
    dfs(N - 1, k * a)
    turtle.left(angl)
    turtle.backward(a)
    return 0

def main() -> int:
    turtle.speed(1)
    mode = input("(d)fs or (b)fs? ")
    while (not mode in ["d", "b"]):
        mode = input("Incorrect option. Enter \"d\" or \"b\": ")
    if (mode == "d"):
        turtle.speed(0)
        dfs(N, L)
        return 0
    for i in range(N):
        dfs(i, L)
    turtle.mainloop()
    return 0

if (__name__ == "__main__"):
    main()
