N, M, A, B = map(int, input().split())

for i in range(M):
    if N <= A:
        N += B
    
    c = int(input())
    if c > N:
        print(i+1)
        break
    else:
        N -= c
else:
    print("complete")
