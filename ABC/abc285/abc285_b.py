N = int(input())
S = input()

for i in range(1, N):
    k = 0
    while i + k < N and S[k] != S[i+k]:
        k += 1
    print(k)
