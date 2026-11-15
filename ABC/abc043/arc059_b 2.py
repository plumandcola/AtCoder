#400点解法
from collections import Counter

s = input()
n = len(s)

ans = (-1, -1)
if n == 2:
    if s[0] == s[1]:
        ans = (1, 2)
else:
    for i in range(n-2):
        count = Counter(s[i : i+3])
        for c in count:
            if count[c] >= 2:
                ans = (i+1, i+3)

print(*ans)