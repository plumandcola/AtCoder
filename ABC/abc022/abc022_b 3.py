N = int(input())

ans = 0
flowers = set()
for _ in range(N):
    A = int(input())
    if A in flowers:
        ans += 1
    else:
        flowers.add(A)

print(ans)