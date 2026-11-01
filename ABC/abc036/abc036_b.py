N = int(input())
s = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        print(s[N-j-1][i], end = "")
    print() #改行
