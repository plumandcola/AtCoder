N = int(input())
p = list(map(int, input().split()))

ans = [0] * N #ans[i] := 操作をi回行った時の喜ぶ人数
for i in range(N): #p[i]について考える
    ans[(p[i] - i - 1) % N] += 1
    ans[(p[i] - i) % N] += 1
    ans[(p[i] - i + 1) % N] += 1

print(max(ans))