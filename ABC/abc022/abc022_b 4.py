N = int(input())

ans = 0
flowers = []
for _ in range(N):
    A = int(input())
    if A in flowers:
        ans += 1
    else:
        flowers.append(A)

print(ans)