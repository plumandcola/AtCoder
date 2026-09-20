#100点解法
n = int(input())
k = int(input())
mod = 1000000007

#重複組み合わせ nHk = (n+k-1)Ck を求める
ans = 1
for i in range(n, n+k):
    ans = ans * i % mod
for i in range(1, k+1):
    ans = ans * pow(i, mod - 2, mod) % mod

print(ans)