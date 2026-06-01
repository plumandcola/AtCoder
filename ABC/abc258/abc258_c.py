N, Q = map(int, input().split())
S = input()

d = 0 #ずれ
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        d = (d + x) % N
    elif t == 2:
        print(S[(N + x - 1 - d) % N])
