from collections import Counter

S = Counter(input())

ans = [False, False, True]
for c in S:
    if ord('A') <= ord(c) <= ord('Z'):
        ans[0] = True
    elif ord('a') <= ord(c) <= ord('z'):
        ans[1] = True
    
    if S[c] > 1:
        ans[2] = False

print("Yes" if all(ans[i] == True for i in range(3)) else "No")