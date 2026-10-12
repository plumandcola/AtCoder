A, B = map(int, input().split())

ans = 1
for _ in range(B):
    ans *= A

print(ans)