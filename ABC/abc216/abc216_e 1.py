N, K = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = max(A) + 1
while r - l > 1:
    mid = (l + r) // 2
    s = sum(max(0, a - mid + 1) for a in A) #アトラクションに乗る回数の合計
    if s > K:
        l = mid
    else:
        r = mid

ans = 0
for a in A:
    if a >= l:
        ans += (a + l + 1) * (a - l) // 2
        K -= a - l
ans += l * K

print(ans)
