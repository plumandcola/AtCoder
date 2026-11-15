from collections import Counter

count = Counter(map(int, input().split()))

if count[5] == 2 and count[7] == 1:
    print("YES")
else:
    print("NO")
