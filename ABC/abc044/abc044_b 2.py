count = [0] * 26

for c in input():
    i = ord(c) - ord('a')
    count[i] += 1

print("Yes" if all(count[i] % 2 == 0 for i in range(26)) else "No")