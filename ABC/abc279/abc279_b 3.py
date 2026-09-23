S = input()
T = input()

n = len(S)
m = len(T)
LPS = [0] * m
j = 0
i = 1
while i < m:
    if T[i] == T[j]:
        j += 1
        LPS[i] = j
        i += 1
    elif j != 0:
        j = LPS[j-1]
    else:
        i += 1

i = 0
j = 0
while i < n:
    if T[j] == S[i]:
        i += 1
        j += 1
        if j == m:
            print("Yes")
            break
    elif j != 0:
        j = LPS[j-1]
    else:
        i += 1
else:
    print("No")
