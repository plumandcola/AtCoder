memo = {0: 1}

def f(x: int) -> int:
    if x in memo: return memo[x]

    memo[x] = f(x//2) + f(x//3)
    return memo[x]


N = int(input())

print(f(N))