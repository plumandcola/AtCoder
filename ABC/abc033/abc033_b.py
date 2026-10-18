N = int(input())

populations = {}
population_total = 0
for _ in range(N):
    S, P = input().split()
    P = int(P)
    populations[S] = P
    population_total += P

ans = "atcoder"
for S in populations:
    if 2 * populations[S] > population_total:
        ans = S

print(ans)