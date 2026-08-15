n = int(input())
a = list(map(int, input().split()))

ans = 0
for a_i in a:
    while a_i % 2 == 0 or a_i % 3 == 2:
        a_i -= 1
        ans += 1

print(ans)