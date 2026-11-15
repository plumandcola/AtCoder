#200点解法
from collections import Counter

s = input()
n = len(s)

ans = (-1, -1)
for i in range(n-1):
    for j in range(i+1, n):
        count = Counter(s[i : j+1])
        for c in count:
            if count[c] > (j - i + 1) // 2:
                ans = (i+1, j+1)

print(*ans)