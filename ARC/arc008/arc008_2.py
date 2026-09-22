from collections import Counter

N, M = map(int, input().split())

name = Counter(input())
kit = Counter(input())

ans = 0
for c in name:
    if kit[c] == 0:
        print(-1)
        break
    else:
        ans = max(ans, (name[c] + kit[c] - 1) // kit[c])
else:
    print(ans)
