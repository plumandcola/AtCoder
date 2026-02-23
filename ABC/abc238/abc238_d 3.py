T = int(input())
for _ in range(T):
    a, s = map(int, input().split())
    if a <= s and a & (s - a) == a:
        print("Yes")
    else:
        print("No")