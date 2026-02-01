N = int(input())

S = []
for _ in range(N):
    S_i = list(input())
    if '#' in S_i:
        S.append(S_i)

while all(S_i[-1] == '.' for S_i in S):
    for S_i in S:
        S_i.pop()

while all(S_i[0] == '.' for S_i in S):
    for S_i in S:
        S_i.pop(0)

T = []
for _ in range(N):
    T_i = list(input())
    if '#' in T_i:
        T.append(T_i)

while all(T_i[-1] == '.' for T_i in T):
    for T_i in T:
        T_i.pop()

while all(T_i[0] == '.' for T_i in T):
    for T_i in T:
        T_i.pop(0)

ans = False
if len(S) == len(T) and len(S[0]) == len(T[0]):
    for i in range(len(S)): #0度回転で一致するかを確認
        for j in range(len(S[0])):
            if S[i][j] != T[i][j]:
                break
        else:
            continue
        break
    else:
        ans = True
    
    for i in range(len(S)): #180度回転で一致するかを確認
        for j in range(len(S[0])):
            if S[i][j] != T[len(T) - i - 1][len(T[0]) - j - 1]:
                break
        else:
            continue
        break
    else:
        ans = True

if len(S) == len(T[0]) and len(S[0]) == len(T):
    for i in range(len(S)): #時計回りに90度回転して一致するかを確認
        for j in range(len(S[0])):
            if S[i][j] != T[j][len(T[0]) - i - 1]:
                break
        else:
            continue
        break
    else:
        ans = True

    for i in range(len(S)): #反時計回りに90度回転して一致するかを確認
        for j in range(len(S[0])):
            if S[i][j] != T[len(T) - j - 1][i]:
                break
        else:
            continue
        break
    else:
        ans = True

print("Yes" if ans else "No")