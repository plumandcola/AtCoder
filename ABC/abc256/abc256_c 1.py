h_1, h_2, h_3, w_1, w_2, w_3 = map(int, input().split())

ans = 0
nums = [[0] * 3 for _ in range(3)]
for a in range(1, h_1 - 1):
    nums[0][0] = a
    for b in range(1, h_1 - nums[0][0]):
        nums[0][1] = b
        nums[0][2] = h_1 - nums[0][0] - nums[0][1]
        if nums[0][2] <= 0:
            continue

        for c in range(1, w_1 - nums[0][0]):
            nums[1][0] = c
            nums[2][0] = w_1 - nums[0][0] - nums[1][0]
            if nums[2][0] <= 0:
                continue

            for d in range(1, h_2 - nums[1][0]):
                nums[1][1] = d
                nums[1][2] = h_2 - nums[1][0] - nums[1][1]
                nums[2][1] = w_2 - nums[0][1] - nums[1][1]
                nums[2][2] = w_3 - nums[0][2] - nums[1][2]
                if nums[1][2] <= 0 or nums[2][1] <= 0 or nums[2][2] <= 0:
                    continue
                if sum(nums[2]) != h_3:
                    continue

                ans += 1

print(ans)