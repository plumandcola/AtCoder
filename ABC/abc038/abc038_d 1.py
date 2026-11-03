#30点解法
N = int(input())

w = [0] * N
h = [0] * N
for i in range(N):
    w[i], h[i] = map(int, input().split())

memo = [-1] * N

def dp(i: int) -> int:
    if memo[i] != -1:
        return memo[i]

    result = 1

    for j in range(N):
        if h[j] < h[i] and w[j] < w[i]:
            result = max(result, dp(j) + 1)

    memo[i] = result
    return result

print(max(dp(i) for i in range(N)))