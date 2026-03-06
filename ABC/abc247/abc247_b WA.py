from collections import defaultdict

N = int(input())
names = [input().split() for _ in range(N)]

name_count = defaultdict(int)
for s, t in names:
    name_count[s] += 1
    name_count[t] += 1

for s, t in names:
    if name_count[s] >= 2 and name_count[t] >= 2:
        print("No")
        break
else:
    print("Yes")