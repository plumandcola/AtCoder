from collections import Counter

N = int(input())
r = Counter(input())

print((4 * r['A'] + 3 * r['B'] + 2 * r['C'] + r['D']) / N)