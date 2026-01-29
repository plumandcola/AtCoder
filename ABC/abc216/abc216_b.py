N = int(input())
print("Yes" if len(set(tuple(input().split()) for _ in range(N))) != N else "No")