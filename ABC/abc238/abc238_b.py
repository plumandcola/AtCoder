N = int(input())
A = list(map(int, input().split()))

ans = [0, 360]
now = 0
for i in range(N):
    now = (now + A[i]) % 360
    ans.append(now)

ans.sort()

print(max(ans[i+1] - ans[i] for i in range(len(ans) - 1)))