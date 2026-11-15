N, L = map(int, input().split())

print(*sorted([input() for _ in range(N)]), sep="")