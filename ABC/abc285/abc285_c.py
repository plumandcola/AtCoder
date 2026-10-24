ans = 0
for c in input():
    ans = ans * 26 + ord(c) - ord('A') + 1

print(ans)