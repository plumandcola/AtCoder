#99点解法
import itertools

N = int(input())
C = [int(input()) for _ in range(N)]

ans = 0 #期待値 × N!
for p in itertools.permutations(C):
    front = [True] * N
    for i in range(N):
        for j in range(i+1, N):
            if p[j] % p[i] == 0:
                front[j] ^= True
    ans += sum(front)

#ansをN!で割る
for i in range(1, N+1):
    ans /= i

print(ans)