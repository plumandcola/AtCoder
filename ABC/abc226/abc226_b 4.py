N = int(input())

a = sorted(list(map(int, input().split())) for _ in range(N)) #Lも入れてしまって差し支えない

ans = 1 #a[0]は最初からカウントしておく
for i in range(1, N):
    if a[i] != a[i-1]:
        ans += 1

print(ans)