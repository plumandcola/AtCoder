N = int(input())

ans = [1, 1]
for _ in range(N):
    T, A = map(int, input().split())
    r = max((ans[0] + T - 1) // T, (ans[1] + A - 1) // A)
    ans = [r * T, r * A]

print(sum(ans))