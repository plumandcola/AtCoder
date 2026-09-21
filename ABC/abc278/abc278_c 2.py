N, Q = map(int, input().split())

g = set()
for _ in range(Q):
    T, A, B = map(int, input().split())
    match T:
        case 1:
            g.add((A, B))
        case 2:
            g.discard((A, B))
        case 3:
            print("Yes" if (A, B) in g and (B, A) in g else "No")
