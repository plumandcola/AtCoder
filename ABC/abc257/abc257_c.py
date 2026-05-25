from collections import defaultdict

N = int(input())
S = list(map(int, input()))
W = list(map(int, input().split()))

count = defaultdict(int) #count[w] := 体重がwの子供の数 - 大人の数
for i in range(N):
    if S[i] == 0:
        count[W[i]] += 1
    elif S[i] == 1:
        count[W[i]] -= 1

f = S.count(1) #正しく判定できる人数 <- Xがmin(W)未満の時に正しく判定できる人数は、大人の人数
ans = f
for X in sorted(count): #Wに出てくる体重のみを調べれば良い
    f += count[X] #体重がXの子供の数 - 大人の数だけ、正しく判定できる人数が増える
    ans = max(ans, f)

print(ans)