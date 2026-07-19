N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

ans = "No"
y = 0
s1 = 0
z = 0
s2 = 0
w = 0
s3 = 0
for x in range(N-2):
    while y < N and s1 < P:
        s1 += A[y]
        s2 -= A[y]
        y += 1
    while z < N and s2 < Q:
        s2 += A[z]
        s3 -= A[z]
        z += 1
    while w < N and s3 < R:
        s3 += A[w]
        w += 1
    
    if s1 == P and s2 == Q and s3 == R:
        print("Yes")
        break
    
    s1 -= A[x]
else:
    print("No")
