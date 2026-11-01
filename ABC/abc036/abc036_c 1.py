#30点解法1
N = int(input())
a = [int(input()) for _ in range(N)]

a_sorted = sorted(set(a))

for i in range(N):
    print(a_sorted.index(a[i]))
