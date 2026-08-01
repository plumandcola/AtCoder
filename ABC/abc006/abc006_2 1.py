n = int(input())
a = [0] * n

if n >= 3:
    a[2] = 1
    for i in range(n-3):
        a[i+3] = (a[i] + a[i+1] + a[i+2]) % 10007

print(a[n-1])