N, x, y = map(int, input().split())
A = list(map(int, input().split()))

X = [set() for _ in range((N+1) // 2)]
Y = [set() for _ in range((N+2) // 2)]

X[0].add(A[0])
for i in range((N+1)//2 - 1):
    for x_i in X[i]:
        X[i+1].add(x_i + A[2*i + 2])
        X[i+1].add(x_i - A[2*i + 2])

Y[0].add(0)
for i in range((N+2)//2 - 1):
    for y_i in Y[i]:
        Y[i+1].add(y_i + A[2*i + 1])
        Y[i+1].add(y_i - A[2*i + 1])

print("Yes" if x in X[-1] and y in Y[-1] else "No")