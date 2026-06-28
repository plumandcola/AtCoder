N = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(N):
    if a[i] == i + 1:
        count += 1
ans = count * (count - 1) // 2 #a_i = i, a_j = j, i < j

for i in range(N):
    if a[i] > i + 1 and a[a[i] - 1] == i + 1:
        ans += 1 #a_i = j, a_j = i, i < j

print(ans)