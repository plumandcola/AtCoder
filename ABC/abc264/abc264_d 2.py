from collections import deque

S = list(input())
T = list("atcoder")

ans = {tuple(S): 0}
q = deque([S])

while q:
    current = q.popleft()
    if current == T:
        print(ans[tuple(current)])
        break

    for i in range(1, 7):
        next = current[:]
        next[i-1], next[i] = next[i], next[i-1]
        if tuple(next) not in ans:
            q.append(next)
            ans[tuple(next)] = ans[tuple(current)] + 1
