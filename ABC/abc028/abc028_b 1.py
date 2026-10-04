count = {chr(ord('A') + i): 0 for i in range(6)}

S = input()
for c in S:
    count[c] += 1

print(*count.values())