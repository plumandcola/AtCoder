events = []

N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    events.append((A, 1))
    events.append((A + B, -1))

events.sort()

ans = [0] * (N+1)
s = 0 #ログインしている人数
for i in range(2*N - 1):
    s += events[i][1]
    ans[s] += events[i+1][0] - events[i][0]

print(*ans[1:])
