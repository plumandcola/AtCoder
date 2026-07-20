S = input()
T = input()

string = "atcoder"

ans = True
for i in range(len(S)):
    if S[i] != T[i]:
        if S[i] == "@" and T[i] not in string:
            ans = False
        elif T[i] == "@" and S[i] not in string:
            ans = False
        elif S[i] != "@" and T[i] != "@":
            ans = False

print("You can win" if ans else "You will lose")