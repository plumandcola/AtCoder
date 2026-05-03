N = int(input())

d = list(range(N+1))
"""
正整数xに対しf(x)を、xの約数のうち最大の平方数として、d[i] := i // f(i)
"""

#平方因子を取り除く
i = 2
while i * i <= N:
    if d[i] == i: #iが素数のとき
        ii = i * i
        for j in range(ii, N+1, ii):
            while d[j] % ii == 0:
                d[j] //= ii
    i += 1

h = [0] * (N+1) #h[i] := i以下の平方数の個数
i = 1
while i * i <= N:
    h[i * i] += 1
    i += 1

#累積和
for i in range(N):
    h[i+1] += h[i]

print(sum(h[N // d[i]] for i in range(1, N+1)))