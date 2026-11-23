from collections import Counter

w = Counter(input())

print("Yes" if all(w[c] % 2 == 0 for c in w) else "No")