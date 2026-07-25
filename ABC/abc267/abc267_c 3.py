N, M = map(int, input().split())
A = list(map(int, input().split()))

s0 = [0] * (N+1) #累積和
for i in range(N):
    s0[i+1] = s0[i] + A[i]

s1 = [0] * (N+1) #(i+1) * A[i]の累積和
for i in range(N):
    s1[i+1] = s1[i] + (i+1) * A[i]

print(max((s1[i+M] - s1[i]) - i * (s0[i+M] - s0[i]) for i in range(N-M+1)))