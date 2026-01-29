N, K = map(int, input().split())
A = list(map(int, input().split()))

l = 1
r = max(A) + 1
while l != r:
    mid = (l+r) // 2
    s = sum(max(0, a - mid + 1) for a in A) #アトラクションに乗る回数の合計
    if s > K:
        l = mid + 1
    else:
        r = mid

ans = 0
for a in A:
    if a >= l:
        ans += (a + l) * (a - l + 1) // 2
        K -= a - l + 1
ans += (l - 1) * K

print(ans)