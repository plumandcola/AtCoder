from collections import Counter

N = int(input())
A = Counter(map(int, input().split()))

ans = 0
for a in list(A):
    for n in range(1, int(a**0.5) + 1):
        if a % n == 0:
            if n == a // n:
                ans += A[a] * A[n] * A[n]
                #iの場合の数 * jの場合の数 * kの場合の数
            else:
                ans += A[a] * A[n] * A[a//n] * 2
                #iの場合の数 * jの場合の数 * kの場合の数 * 2 (jとkの入れ替え)

print(ans)