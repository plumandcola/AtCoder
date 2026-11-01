N = int(input())
a = [int(input()) for _ in range(N)]

a_sorted = sorted(set(a))
d = {a_i: i for i, a_i in enumerate(a_sorted)}

for i in range(N):
    print(d[a[i]])
