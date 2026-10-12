S = input()

ans = 0
i = 0
while i < len(S):
    ans += 1
    if i+1 < len(S) and S[i] == S[i+1] == '0':
        i += 2
    else:
        i += 1

print(ans)