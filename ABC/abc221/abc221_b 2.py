S = list(input())
T = list(input())

ans = False

if S == T:
    ans = True

for i in range(len(S)):
    if S[i] != T[i]:
        if i > 0:
            S[i-1], S[i] = S[i], S[i-1]
            if S == T:
                ans = True
            S[i-1], S[i] = S[i], S[i-1] #元に戻す
        
        if i+1 < len(S):
            S[i], S[i+1] = S[i+1], S[i]
            if S == T:
                ans = True
            S[i], S[i+1] = S[i+1], S[i] #元に戻す
        
        break

print("Yes" if ans else "No")