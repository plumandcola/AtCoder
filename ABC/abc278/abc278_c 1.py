from collections import defaultdict

N, Q = map(int, input().split())

g = defaultdict(set)
for _ in range(Q):
    T, A, B = map(int, input().split())
    match T:
        case 1:
            g[A].add(B)
        case 2:
            g[A].discard(B)
        case 3:
            print("Yes" if B in g[A] and A in g[B] else "No")
