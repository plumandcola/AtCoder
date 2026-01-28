N, M = map(int, input().split())
A = list(map(int, input().split()))

primes = set()
for a in A:
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            primes.add(i)
            while a % i == 0:
                a //= i
    if a != 1:
        primes.add(a)

ans = [True] * (M+1)
ans[0] = False
for n in primes:
    for i in range(N): #nを素因数に持つAの要素が存在するか確認
        if A[i] % n == 0: #nは素数なので、nで割り切れるかどうかを確かめれば、判定として十分
            for j in range(n, M+1, n):
                ans[j] = False #nを素因数にもつ数を、答えの候補から削除
            break

k = []
for n in range(M+1):
    if ans[n] == True:
        k.append(n)

print(len(k))
print(*k, sep = "\n")