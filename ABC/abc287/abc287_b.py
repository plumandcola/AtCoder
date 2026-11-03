N, M = map(int, input().split())
S = [int(input()) for _ in range(N)]

flag = [False] * 1000
for _ in range(M):
    flag[int(input())] = True

print(sum(flag[S[i] % 1000] == True for i in range(N)))