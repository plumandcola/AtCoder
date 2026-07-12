L, R = map(int, input().split())
s = "atcoder"

for i in range(7):
    if L <= i+1 <= R: print(s[i], end="")

print() #改行