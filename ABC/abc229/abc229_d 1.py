S = input()
K = int(input())

n = len(S)
count = [0] * (n+1)
for i in range(n):
    count[i+1] = count[i] + int(S[i] == '.')

ans = 0
r = 0
for l in range(n):
    while r < n and count[r+1] - count[l] <= K:
        r += 1
    
    ans = max(ans, r - l)

print(ans)