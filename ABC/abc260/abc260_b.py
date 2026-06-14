N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = set()
for score, i in sorted([-A[i], i] for i in range(N))[:X]: #点について降順にするため、マイナスにしている
    ans.add(i+1)

for score, i in sorted([-B[i], i] for i in range(N) if i+1 not in ans)[:Y]:
    ans.add(i+1)

for score_total, i in sorted([- A[i] - B[i], i] for i in range(N) if i+1 not in ans)[:Z]:
    ans.add(i+1)

print(*sorted(ans), sep="\n")