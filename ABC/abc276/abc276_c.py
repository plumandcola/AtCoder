N = int(input())
P = list(map(int, input().split()))

#末尾から降順になっているのが崩れるインデックスを探す
i = N-2
while P[i] < P[i+1]:
    i -= 1

#P[i]の次に小さい数字を見つける
j = N-1
while P[j] > P[i]:
    j -= 1

P[i], P[j] = P[j], P[i]
#i+1項目以降は昇順になっている

print(*P[:i+1], *P[:i:-1])