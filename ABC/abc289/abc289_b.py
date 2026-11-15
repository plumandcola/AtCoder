N, M = map(int, input().split())
a = list(map(int, input().split()))

i = 0 #aのインデックス
l = 0 #pのインデックス
p = list(range(1, N+1))
while l < N:
    r = l + 1
    while i < M and a[i] == r:
        i += 1
        r += 1
    p[l:r] = p[l:r][::-1]

    l = r

print(*p)