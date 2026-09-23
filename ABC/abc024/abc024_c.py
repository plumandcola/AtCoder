N, D, K = map(int, input().split())

L = [0] * D
R = [0] * D
for i in range(D):
    L[i], R[i] = map(int, input().split())

S = [0] * K
T = [0] * K
for i in range(K):
    S[i], T[i] = map(int, input().split())

for i in range(K): #i番目の民族について
    l = S[i] #現時点で行き来できる街の左端
    r = S[i] #現時点で行き来できる街の右端
    for d in range(D):
        if l <= R[d] and r >= L[d]: #行き来できる街の範囲を伸ばせる
            l = min(l, L[d])
            r = max(r, R[d])
            if l <= T[i] <= r: #街T[i]に到着できる
                print(d+1)
                break
