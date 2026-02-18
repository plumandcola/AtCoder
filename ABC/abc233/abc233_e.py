X = list(map(int, input())) #Xを1文字ずつint型にしたlistに

n = len(X)
for i in range(n - 1):
    X[i+1] += X[i]

X.reverse()

for i in range(n-1):
    X[i+1] += X[i] // 10
    X[i] %= 10

while X[-1] >= 10:
    X.append(X[-1] // 10)
    X[-2] %= 10

print(*X[::-1], sep = "")