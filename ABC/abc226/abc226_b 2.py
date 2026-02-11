N = int(input())

print(len(set(tuple(map(int, input().split())) for _ in range(N))))