S = input()
T = input()

n = len(S)
m = len(T)
TS = T + S
z = [0] * (m+n)
j = 0
for i in range(m+n):
    if j != 0 and i < j + z[j]:
        z[i] = min(z[i-j], j + z[j] - i)
    if j == 0 or j + z[j] <= i + z[i]:
        while i + z[i] < m+n and TS[z[i]] == TS[i + z[i]]:
            z[i] += 1
        j = i

for i in range(m, m+n):
    if z[i] >= m:
        print("Yes")
        break
else:
    print("No")
