N = int(input())

M = 0 #dの最大
s = 0 #dの和
for _ in range(N):
    d = int(input())
    M = max(M, d)
    s += d

print(s)
print(max(0, 2*M - s))