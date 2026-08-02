N = int(input())

bit = []
i = 0
while N:
    if N & 1 == 1:
        bit.append(i)
    N >>= 1
    i += 1

n = len(bit)
for b in range(1 << n):
    ans = 0
    for i in range(n):
        if ((b >> i) & 1) == 1:
            ans |= 1 << bit[i]
    print(ans)
