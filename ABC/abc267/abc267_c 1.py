N, M = map(int, input().split())
A = list(map(int, input().split()))

ans_i = sum((i+1) * A[i] for i in range(M))
ans = ans_i
s = sum(A[:M]) #s := sum(A[i : i+M])
for i in range(N - M):
    ans_i += - s + M * A[i+M]
    ans = max(ans, ans_i)
    s += - A[i] + A[i+M]

print(ans)