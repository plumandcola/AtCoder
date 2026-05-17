S = [0] * 200001

N = int(input())
for _ in range(N):
    L, R = map(int, input().split())
    S[L] += 1
    S[R] -= 1

for i in range(200000):
    S[i+1] += S[i]

l = 0
while True:
    while l < 200001 and S[l] <= 0:
        l += 1
    
    if l == 200001:
        break
    
    r = l
    while r < 200001 and S[r] > 0:
        r += 1
    print(l, r)
    l = r
