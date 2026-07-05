N = int(input())
P = list(map(int, input().split()))

ans = 0
now = N - 2
while now != -1:
    now = P[now] - 2
    ans += 1

print(ans)