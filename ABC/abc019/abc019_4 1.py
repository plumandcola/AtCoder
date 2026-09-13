#20点解法
N = int(input())

ans = 0
for i in range(1, N):
    for j in range(i+1, N+1):
        print("?", i, j)
        ans = max(ans, int(input()))

print("!", ans)