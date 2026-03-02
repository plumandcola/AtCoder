from collections import defaultdict

N = int(input())

X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

S = input()

R = defaultdict(list)
L = defaultdict(list)
for i in range(N):
    if S[i] == 'L':
        L[Y[i]].append(X[i])
    elif S[i] == 'R':
        R[Y[i]].append(X[i])

for y in L:
    if len(R[y]) != 0 and max(L[y]) > min(R[y]):
        print("Yes")
        break
else:
    print("No")