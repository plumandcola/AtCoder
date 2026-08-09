N = int(input())

count = [0] * 4
for c in map(int, input()):
    count[c-1] += 1

print(max(count), min(count))