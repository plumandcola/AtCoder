days = [0, 0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335] #その月までの日数
holiday = [False] * 367

for i in range(1, 367, 7):
    holiday[i] = True
for i in range(7, 367, 7):
    holiday[i] = True

N = int(input())

for _ in range(N):
    m, d = map(int, input().split('/'))
    d += days[m]

    while d < 366 and holiday[d] == True:
        d += 1
    holiday[d] = True

ans = 0
l = 1
r = 1
while l <= 366:
    while r <= 366 and holiday[r] == True:
        r += 1
    ans = max(ans, r - l)
    l = r + 1
    r += 1

print(ans)