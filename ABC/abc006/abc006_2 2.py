n = int(input())
a = [0] * n
s = [0] * (n+1)
"""s[i] := a[i-1]までの和"""

if n >= 3:
    a[2] = 1
    s[3] = 1
    for i in range(n-3):
        a[i+3] = (s[i+3] - s[i]) % 10007
        s[i+4] = (s[i+3] + a[i+3]) % 10007

print(a[n-1])