N = int(input())
S = list(map(int, input().split()))

flag = [False] * 1001
for a in range(1, 1001):
    for b in range(1, 1001):
        if 4*a*b + 3*a + 3*b <= 1000:
            flag[4*a*b + 3*a + 3*b] = True

ans = 0
for s in S:
    if flag[s] == False:
        ans += 1

print(ans)