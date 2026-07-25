n = 4

c = [input().split() for _ in range(n)]

for i in range(n-1, -1, -1):
    print(*c[i][::-1])
