N, K = map(int, input().split())
A = sorted(map(int, input().split()), reverse=True) + [0]

ans = 0
i = 0
while K > 0 and A[i] > 0:
    while A[i+1] == A[i]:
        i += 1
    if K // (i+1) < A[i] - A[i+1]:
        cycle = K // (i+1)
        ans += (A[i] + (A[i] - cycle + 1)) * cycle // 2 * (i+1)
        ans += (A[i] - cycle) * (K % (i+1))
        K = 0
    else:
        ans += (A[i] + A[i+1] + 1) * (A[i] - A[i+1]) // 2 * (i+1)
        K -= (A[i] - A[i+1]) * (i+1) #乗った回数の分、減らす
    i += 1

print(ans)