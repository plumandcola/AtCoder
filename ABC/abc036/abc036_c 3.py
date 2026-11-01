N = int(input())
a = [int(input()) for _ in range(N)]

a_sorted = sorted(set(a))
d = {a_sorted[i]: i for i in range(len(a_sorted))}

for i in range(N):
    print(d[a[i]])
