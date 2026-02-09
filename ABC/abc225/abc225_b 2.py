N = int(input())

count = [0] * N
for _ in range(N-1):
    a, b = map(int, input().split())
    count[a-1] += 1
    count[b-1] += 1

print("Yes" if any(count[i] == N-1 for i in range(N)) else "No")