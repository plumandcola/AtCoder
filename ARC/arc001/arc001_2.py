from collections import deque

A, B = map(int, input().split())

ans = [-1] * 41
ans[A] = 0
q = deque([A])
while q:
    v = q.popleft()
    for u in (v-1, v+1, v-5, v+5, v-10, v+10):
        if 0 <= u <= 40 and ans[u] == -1:
            ans[u] = ans[v] + 1
            q.append(u)

print(ans[B])