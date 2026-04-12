import math

def f(n: int) -> int:
    return n * (n + 1) // 2

N, A, B = map(int, input().split())
L = math.lcm(A, B)

print(f(N) - A * f(N // A) - B * f(N // B) + L * f(N // L))