N, K = map(int, input().split())
A = sorted(set(map(int, input().split())))[:K]

ans = 0
while ans < len(A) and ans == A[ans]:
    ans += 1

print(ans)