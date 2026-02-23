T = int(input())
for _ in range(T):
    a, s = map(int, input().split())
    while a:
        if a & 1 == 1:
            if s & 1 == 1 or s < 2:
                print("No")
                break
            else:
                s -= 2
        s >>= 1
        a >>= 1
    else:
        print("Yes")