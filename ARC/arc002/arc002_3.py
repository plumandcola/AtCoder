N = int(input())
c = input()

keys = "ABXY"
shortcut = []
for i in range(4):
    for j in range(4):
        shortcut.append(keys[i] + keys[j])

ans = N
n = len(shortcut)
for L in range(n):
    for R in range(L+1, n):
        count = 0
        i = 0
        while i < N:
            count += 1
            if c[i : i+2] == shortcut[L] or c[i : i+2] == shortcut[R]:
                i += 2
            else:
                i += 1
        ans = min(ans, count)

print(ans)