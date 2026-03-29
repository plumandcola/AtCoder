ans = []

for i in range(1, 100):
    ans.append(i)

for i in range(1, 100):
    ans.append(i * 100)

for i in range(1, 100):
    ans.append(i * 10000)

print(len(ans))
print(*ans)