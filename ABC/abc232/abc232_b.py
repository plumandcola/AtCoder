S = input()
T = input()

K = (ord(T[0]) - ord(S[0])) % 26
for i in range(len(S)):
    if (ord(T[i]) - ord(S[i])) % 26 != K:
        print("No")
        break
else:
    print("Yes")
