from collections import Counter

S = Counter(input())

for i in range(26):
    c = chr(ord('a') + i)
    print(S[c] * c, end = "")
print() #最後の改行