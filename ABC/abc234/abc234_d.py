from sortedcontainers import SortedSet

N, K = map(int, input().split())
P = list(map(int, input().split()))

S = SortedSet(P[:K])
print(S[-K])
for i in range(K, N):
    S.add(P[i])
    print(S[-K])