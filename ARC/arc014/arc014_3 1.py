#30点解法
from collections import deque

N = int(input())
S = input()

ans = float("inf")
for b in range(1 << N):
    q = deque()
    for i in range(N):
        if (b >> i) & 1:
            if len(q) >= 1 and q[0] == S[i]:
                q.popleft()
            else:
                q.appendleft(S[i])
        else:
            if len(q) >= 1 and q[-1] == S[i]:
                q.pop()
            else:
                q.append(S[i])
    ans = min(ans, len(q))

print(ans)