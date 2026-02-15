S = input()
T = "oxx"

ans = False
for i in range(len(T)):
    for j in range(len(S)):
        if S[j] != T[(j+i) % len(T)]:
            break
    else:
        ans = True

print("Yes" if ans else "No")