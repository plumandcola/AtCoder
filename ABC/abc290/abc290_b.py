N, K = map(int, input().split())

count = 0
for c in input():
    if c == 'o' and count < K:
        print('o', end="")
        count += 1
    else:
        print('x', end="")
print() #改行