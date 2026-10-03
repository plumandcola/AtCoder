N = int(input())
a = list(map(int, input().split()))

S = sum(a)
if S % N != 0:
    print(-1)
else:
    ans = N
    ave = S // N
    s = 0
    n = 0
    for i in range(N):
        s += a[i]
        n += 1
        if s == ave * n: #ここまでの島に橋を架ける
            s = 0
            n = 0
            ans -= 1
    
    print(ans)
