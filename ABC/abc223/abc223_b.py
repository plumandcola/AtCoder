S = input()

ans1 = S
ans2 = S
n = len(S)
T = S * 2
for i in range(n):
    ans1 = min(ans1, T[i:i+n])
    ans2 = max(ans2, T[i:i+n])

print(ans1)
print(ans2)