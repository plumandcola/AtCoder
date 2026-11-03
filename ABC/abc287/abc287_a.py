from collections import Counter

N = int(input())
S = Counter(input() for _ in range(N))

print("Yes" if S["For"] > N//2 else "No")