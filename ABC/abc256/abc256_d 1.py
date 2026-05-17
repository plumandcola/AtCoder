N = int(input())
query = []
for _ in range(N):
    L, R = map(int, input().split())
    query.append((L, 0))
    query.append((R, 1))

query.sort()

cnt = 0
for t, f in query:
    if f == 0:
        if cnt == 0:
            print(t, end=" ")
        cnt += 1
    else:
        cnt -= 1
        if cnt == 0:
            print(t)
