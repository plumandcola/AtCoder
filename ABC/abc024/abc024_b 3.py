#100点解法
max_t = 1100001
open = [0] * max_t #いもす法

N, T = map(int, input().split())
for _ in range(N):
    A = int(input())
    open[A] += 1
    open[A+T] -= 1

for t in range(max_t - 1):
    open[t+1] += open[t]

print(sum(open[t] > 0 for t in range(max_t)))