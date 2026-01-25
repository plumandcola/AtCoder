N, M = map(int, input().split())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))

ans = float("inf")
j = 0 #Bのindex
for i in range(N): #Aのindex
    while j < M and A[i] >= B[j]:
        ans = min(ans, A[i] - B[j])
        j += 1
    if j < M:
        ans = min(ans, abs(A[i] - B[j]))

print(ans)