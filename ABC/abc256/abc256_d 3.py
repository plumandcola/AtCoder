N = int(input())
intervals = sorted(tuple(map(int, input().split())) for _ in range(N))

X = [] #答えを格納する配列
Y = []
for L, R in intervals:
    if len(X) == 0 or Y[-1] < L: #追加する
        X.append(L)
        Y.append(R)
    else: #併合する
        Y[-1] = max(Y[-1], R)

for x, y in zip(X, Y):
    print(x, y)
