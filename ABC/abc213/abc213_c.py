import bisect

H, W, N = map(int, input().split())

cards = []
rows = set()
columns = set()
for _ in range(N):
    A, B = map(int, input().split())
    cards.append((A-1, B-1))
    rows.add(A-1)
    columns.add(B-1)

rows = sorted(rows)
columns = sorted(columns)
for A, B in cards:
    print(bisect.bisect_left(rows, A) + 1, bisect.bisect_left(columns, B) + 1)