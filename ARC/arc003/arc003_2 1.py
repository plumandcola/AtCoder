N = int(input())

s = [input() for _ in range(N)]

t = []
for i in range(N):
    t.append(s[i][::-1])
t.sort()

for i in range(N):
    print(t[i][::-1])
