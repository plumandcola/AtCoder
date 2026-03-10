def solve(a: int, b: int, c: int, x: int) -> int:
    q, r = divmod(x, a+c)
    return (q * a + min(a, r)) * b


A, B, C, D, E, F, X = map(int, input().split())

n = solve(A, B, C, X)
m = solve(D, E, F, X)

if n > m:
    print("Takahashi")
elif n < m:
    print("Aoki")
else:
    print("Draw")
