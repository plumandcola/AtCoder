N, S, T = map(int, input().split())

W = 0
ans = 0
for _ in range(N):
    A = int(input())
    W += A
    if S <= W <= T:
        ans += 1

print(ans)