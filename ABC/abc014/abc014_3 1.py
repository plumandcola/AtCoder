#30点解法
n = int(input())

ans = [0] * 1000001
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        ans[i] += 1

print(max(ans))