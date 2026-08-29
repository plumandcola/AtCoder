N = int(input())

ans = [0] * (2*N + 1)
for i, A in enumerate(map(int, input().split())):
    ans[2*i + 1] = ans[A-1] + 1
    ans[2*i + 2] = ans[A-1] + 1

print(*ans, sep="\n")