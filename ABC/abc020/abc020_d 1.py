#15解法
import math

N, K = map(int, input().split())

ans = 0
for i in range(1, N+1):
    ans = (ans + math.lcm(i, K)) % 1000000007

print(ans)