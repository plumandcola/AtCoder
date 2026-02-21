N, M = map(int, input().split())
S = input().split()
T = input().split()

i = 0
j = 0
while i < N and j < M:
    if S[i] == T[j]: #急行列車が止まる
        print("Yes")
        j += 1
    else: #急行列車が止まらない
        print("No")
    
    i += 1