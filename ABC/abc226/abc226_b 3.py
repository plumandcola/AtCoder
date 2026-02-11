N = int(input())

L = [0] * N
a = [[] for _ in range(N)]
for i in range(N):
    L[i], *a[i] = map(int, input().split())

a.sort()

ans = 1 #a[0]は最初からカウントしておく
for i in range(1, N):
    if a[i] != a[i-1]:
        ans += 1

print(ans)