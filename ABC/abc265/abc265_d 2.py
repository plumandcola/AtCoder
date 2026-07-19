N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

s = [0] * (N+1) #累積和
for i in range(N):
    s[i+1] = s[i] + A[i]

s_set = set(s)

ans = "No"
for x in range(N-2):
    if (s[x] + P) in s_set and (s[x] + P + Q) in s_set and (s[x] + P + Q + R) in s_set:
        print("Yes")
        break
else:
    print("No")
