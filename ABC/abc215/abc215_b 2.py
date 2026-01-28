N = int(input())

k = 0
while N:
    N >>= 1
    k += 1

print(k-1)