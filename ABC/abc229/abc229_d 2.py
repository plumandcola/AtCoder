S = input()
K = int(input())

ans = 0
n = len(S)
r = 0
count = 0
for l in range(n):
    while r < n and count + int(S[r] == '.') <= K:
        count += int(S[r] == '.')
        r += 1
    
    ans = max(ans, r - l)

    if S[l] == '.':
        count -= 1

print(ans)