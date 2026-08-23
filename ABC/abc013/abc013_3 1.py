#10点解法
N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())

ans = float("inf")
for b in range(pow(3, N)):
    ans_i = 0 #食費の合計
    h = H #満腹度
    for i in range(N):
        if (b // pow(3, i)) % 3 == 0:
            ans_i += A
            h += B
        elif (b // pow(3, i)) % 3 == 1:
            ans_i += C
            h += D
        elif (b // pow(3, i)) % 3 == 2:
            h -= E
            if h <= 0:
                break
    else:
        ans = min(ans, ans_i)

print(ans)