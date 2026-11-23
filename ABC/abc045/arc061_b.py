from collections import Counter, defaultdict

H, W, N = map(int, input().split())

count_black = defaultdict(int)
for _ in range(N):
    a, b = map(int, input().split())
    for h in (a-2, a-1, a):
        for w in (b-2, b-1, b):
            if 1 <= h <= H-2 and 1 <= w <= W-2:
                count_black[(h, w)] += 1

count = Counter(count_black.values())

print((H-2) * (W-2) - sum(count.values()))
for i in range(1, 10):
    print(count[i])
