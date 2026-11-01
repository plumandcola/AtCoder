N, A, B = map(int, input().split())
S = input()

ans = float("inf")
for i in range(N):
    count = 0 #前からi文字目と後ろからi文字目が一致していない数
    for j in range(N//2):
        if S[(i+j) % N] != S[(N+i-j-1) % N]:
            count += 1
    ans = min(ans, A * i + count * B)

print(ans)