#100点解法
from collections import defaultdict

n = int(input())
query = []
for _ in range(n):
    a, b = map(int, input().split())
    query.append((a, 1))
    query.append((b+1, -1))
query.sort()

#イベントソート(?)
num = 0 #人気
s = defaultdict(int)
for color, change in query:
    num += change
    s[color] = num

print(max(s.values()))