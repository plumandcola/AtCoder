N = int(input())

ans = 101
for _ in range(N):
    T = int(input())
    if T < ans:
        ans = T

print(ans)