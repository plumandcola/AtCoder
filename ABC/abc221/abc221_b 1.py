S = input()
T = input()

ans = False
if S == T:
    ans = True
for i in range(len(S) - 1):
    if S[:i] + S[i+1] + S[i] + S[i+2:] == T:
        ans = True

print("Yes" if ans else "No")