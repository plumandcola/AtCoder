N, X = map(int, input().split())

A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

s = [0] * (N+1) #s[i] := ステージiまでを1回ずつクリアするのにかかる時間
for i in range(N):
    s[i+1] = s[i] + A[i] + B[i]

ans = float("inf")
for i in range(min(N, X+1)):
    ans = min(ans, s[i+1] + (X-i-1) * B[i])

print(ans)