def f(x: int) -> float:
    return B * x + A / (x+1) ** (1/2)


A, B = map(int, input().split())

x = int((A * A / (4 * B * B)) ** (1/3))

print(min(f(x), f(x+1)))