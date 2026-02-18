L, R = map(int, input().split())
S = input()

for i in range(len(S)):
    if L-1 <= i <= R-1:
        print(S[L+R-i-2], end = "") #R-1 - (i - (L-1)) = R-1 - i + L-1 = L+R-i-2
    else:
        print(S[i], end = "")