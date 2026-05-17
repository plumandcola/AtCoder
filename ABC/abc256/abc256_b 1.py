N = int(input())
A = list(map(int, input().split()))

P = 0
squares = [False] * 4
for i in range(N):
    squares[0] = True
    for j in range(3, -1, -1):
        if squares[j] == False:
            continue

        if j + A[i] >= 4:
            squares[j] = False
            P += 1
        else:
            squares[j + A[i]] = True
            squares[j] = False

print(P)