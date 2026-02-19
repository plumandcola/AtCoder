X = int(input())

ans_set = set()
for i in range(1, 10):
    for d in range(-9, 10):
        n = i
        while n <= 111111111111111111:
            ans_set.add(n)
            if 0 <= n % 10 + d <= 9:
                n = 10 * n + n % 10 + d
            else:
                break

ans_list = sorted(ans_set)

for n in ans_list:
    if n >= X:
        print(n)
        break