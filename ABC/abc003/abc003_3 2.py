N, K = map(int, input().split())

print(sum(r * (1/2) ** (i+1) for i, r in enumerate(sorted(map(int, input().split()), reverse=True)[:K])))