N = int(input())
a, b = map(int, input().split())
K = int(input())
P = set(map(int, input().split()))

P.add(a)
P.add(b)

print("YES" if len(P) == K + 2 else "NO")