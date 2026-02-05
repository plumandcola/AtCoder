N = sorted(map(int, input()), reverse=True)

ans = 0
for i in range(1 << len(N)):
    nums = [0, 0]
    for j in range(len(N)):
        flag = i >> j & 1
        nums[flag] = nums[flag] * 10 + N[j]
    ans = max(ans, nums[0] * nums[1])

print(ans)