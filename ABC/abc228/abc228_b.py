N, X = map(int, input().split())
A = list(map(int, input().split()))

visited = [False] * N
while visited[X-1] == False:
    visited[X-1] = True
    X = A[X-1]

print(sum(visited))