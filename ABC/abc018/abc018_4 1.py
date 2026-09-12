#30点解法
import itertools

N, M, P, Q, R = map(int, input().split())

x = [0] * R
y = [0] * R
z = [0] * R
for i in range(R):
    x[i], y[i], z[i] = map(int, input().split())

ans = 0
for c_g in itertools.combinations(range(1, N+1), P):
    for c_b in itertools.combinations(range(1, M+1), Q):
        s = 0
        for i in range(R):
            if x[i] in c_g and y[i] in c_b:
                s += z[i]
        ans = max(ans, s)

print(ans)