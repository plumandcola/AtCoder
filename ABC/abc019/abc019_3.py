N = int(input())

nums = set()
for a in map(int, input().split()):
    while a % 2 == 0:
        a //= 2
    nums.add(a)

print(len(nums))