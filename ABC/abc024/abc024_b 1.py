#50点解法
max_t = 1100000
open = [False] * max_t

N, T = map(int, input().split())
for _ in range(N):
    A = int(input())
    for t in range(A, A+T):
        open[t] = True

print(sum(open[t] == True for t in range(max_t)))