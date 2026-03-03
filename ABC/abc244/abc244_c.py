N = int(input())

nums = set(range(1, 2*N + 2))
while True:
    print(nums.pop())
    m = int(input())
    if m != 0:
        nums.discard(m)
    else:
        break