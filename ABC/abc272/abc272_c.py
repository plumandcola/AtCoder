N = int(input())

odd = []
even = []
for A in map(int, input().split()):
    if A % 2 == 1:
        odd.append(A)
    else:
        even.append(A)

odd.sort(reverse=True)
even.sort(reverse=True)

ans = -1
if len(odd) >= 2:
    ans = max(ans, odd[0] + odd[1])
if len(even) >= 2:
    ans = max(ans, even[0] + even[1])

print(ans)