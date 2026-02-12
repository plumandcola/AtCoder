N = int(input())
S = list(map(int, input().split()))

areas = set()
a = 1
while True:
    b = a
    s = 4*a*b + 3*a + 3*b
    if s > 100000:
        break

    while True:
        areas.add(s)
        b += 1
        s = 4*a*b + 3*a + 3*b
        if s > 100000:
            break
    a += 1

print(sum(s not in areas for s in S))