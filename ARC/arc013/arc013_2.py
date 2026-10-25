C = int(input())

ans = [0, 0, 0]
for _ in range(C):
    N, M, L = sorted(map(int, input().split()))
    ans[0] = max(ans[0], N)
    ans[1] = max(ans[1], M)
    ans[2] = max(ans[2], L)

print(ans[0] * ans[1] * ans[2])