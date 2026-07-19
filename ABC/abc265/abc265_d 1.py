import bisect

N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

s = [0] * (N+1) #累積和
for i in range(N):
    s[i+1] = s[i] + A[i]

ans = "No"
for x in range(N-2):
    y = bisect.bisect_left(s, s[x] + P)

    #xに対して、2つ目の条件を満たすyが見つかった
    if y != N+1 and s[y] - s[x] == P:
        z = bisect.bisect_left(s, s[y] + Q)

        #x,yに対して、3つ目の条件を満たすzが見つかった
        if z != N+1 and s[z] - s[y] == Q:
            w = bisect.bisect_left(s, s[z] + R)

            #x,y,zに対して、4つ目の条件を満たすwが見つかった
            if w != N+1 and s[w] - s[z] == R:
                ans = "Yes"

print(ans)