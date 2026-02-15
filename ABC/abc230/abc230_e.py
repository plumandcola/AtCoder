N = int(input())

ans = 0
k = 1
while k * k <= N:
    ans += (N // k - N // (k+1)) * k
    k += 1

#この時点では、k = [√N]+1になっていることに注意
for i in range(1, N // k + 1):
    ans += N // i

print(ans)