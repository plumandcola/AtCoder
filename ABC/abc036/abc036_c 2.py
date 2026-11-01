#30点解法2
N = int(input())
a = [int(input()) for _ in range(N)]

a_sorted = sorted(set(a))
ans = [-1] * (max(a) + 1)

for i in range(len(a_sorted)):
    ans[a_sorted[i]] = i

for i in range(N):
    print(ans[a[i]])
