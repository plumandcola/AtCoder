N = int(input())
A = set(map(int, input().split()))

ans = 0
while ans in A:
    ans += 1

print(ans)