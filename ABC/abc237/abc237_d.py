from collections import deque

N = int(input())
S = input()

ans = deque([N])
for i in range(N-1, -1, -1):
    if S[i] == 'R':
        ans.appendleft(i)
    elif S[i] == 'L':
        ans.append(i)

print(*ans)