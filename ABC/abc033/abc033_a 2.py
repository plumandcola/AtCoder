from collections import Counter

N = input()

print("SAME" if len(Counter(N)) == 1 else "DIFFERENT")