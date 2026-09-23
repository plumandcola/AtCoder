def calc_time(t: int) -> int:
    return B * t + A / (1 + t) ** 0.5


A, B = map(int, input().split())

#三分探索
l = -1
r = 10 ** 18 + 1
while r - l > 2:
    mid1 = (2*l + r) // 3
    mid2 = (l + 2*r) // 3

    if calc_time(mid1) >= calc_time(mid2):
        l = mid1
    else:
        r = mid2

print(calc_time((l+r) // 2))