N, K = map(int, input().split())

w = [0] * N
p = [0] * N
for i in range(N):
    w[i], p[i] = map(int, input().split())

#二分探索
l = 0
r = 10000
while abs(r - l) > 0.0000000001:
    mid = (l + r) / 2
    if sum(sorted((p[i] * w[i] - mid * w[i] for i in range(N)), reverse=True)[:K]) >= 0:
        l = mid
    else:
        r = mid

print(l)