T = int(input())
for _ in range(T):
    a, s = map(int, input().split())
    if 2 * a <= s and (s - 2 * a) & a == 0:
        print("Yes")
    else:
        print("No")