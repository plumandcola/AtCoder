N = int(input())
A = list(map(int, input().split()))
X = int(input())

s = sum(A)
ans = N * (X // s)
X %= s
while X >= 0:
    X -= A[ans % N]
    ans += 1

print(ans)