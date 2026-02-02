X = input() #元のアルファベット順 → 新たなアルファベット順
x_dict = {X[i]: chr(ord('a') + i) for i in range(26)} #新たなアルファベット順 → 元のアルファベット順

N = int(input())
S = [input() for _ in range(N)]

T = [""] * N #Sを、元のアルファベット順に戻して格納
for i in range(N):
    for j in range(len(S[i])):
        T[i] += x_dict[S[i][j]]

T.sort()

ans = [""] * N #Tを、新たなアルファベット順に戻して格納
for i in range(N):
    for j in range(len(T[i])):
        ans[i] += X[ord(T[i][j]) - ord('a')]
    print(ans[i])