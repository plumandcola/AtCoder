N = int(input())

sq = [False] * (N+1) #平方数かどうか
i = 1
while i*i <= N:
    sq[i * i] = True
    i += 1

d = [[] for _ in range(N+1)] #d[j] := jの約数
for i in range(1, N+1):
    for j in range(i, N+1, i):
        d[j].append(i)

count = [0] * (N+1) #整数Nの約数のうち最大の平方数をf(N)としたとき、count[n] := n = i // f(i)となるiの個数
for i in range(1, N+1):
    f = 0
    for d_ij in d[i]:
        if sq[d_ij]:
            f = d_ij
    count[i // f] += 1

print(sum(count[i] * count[i] for i in range(1, N+1)))