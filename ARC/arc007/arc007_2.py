N, M = map(int, input().split())

ans = list(range(N+1)) #ans[i] := i番目のCDケースに入ってるCDの番号
indices = list(range(N+1)) #indices[i] := i番のCDが入ってるCDケースの番号
for _ in range(M):
    disk = int(input())
    i = indices[disk]
    indices[ans[0]], indices[ans[i]] = indices[ans[i]], indices[ans[0]]
    ans[0], ans[i] = ans[i], ans[0]

print(*ans[1:], sep="\n")