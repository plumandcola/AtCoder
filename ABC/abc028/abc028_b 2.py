from collections import Counter

S = Counter(input())

print(*[S[chr(ord('A') + i)] for i in range(6)])