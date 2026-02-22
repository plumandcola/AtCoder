S = input()

n = len(S)
r = n
while r > 0 and S[r-1] == 'a':
    r -= 1

l = 0
while l < r and S[l] == 'a':
    l += 1

print("Yes" if l <= n-r and S[l:r] == S[l:r][::-1] else "No")