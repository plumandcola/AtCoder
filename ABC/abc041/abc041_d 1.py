#30点解法
import itertools

N, M = map(int, input().split())

x = [0] * M
y = [0] * M
for i in range(M):
    x[i], y[i] = map(int, input().split())

ans = 0
for p in itertools.permutations(range(1, N+1)):
    indices = {p[i]: i for i in range(N)}
    for i in range(M):
        if indices[x[i]] < indices[y[i]]:
            break
    else:
        ans += 1

print(ans)