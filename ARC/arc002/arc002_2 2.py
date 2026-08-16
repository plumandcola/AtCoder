from datetime import date, timedelta

Y, M, D = map(int, input().split('/'))

cur = date(Y, M, D)

while True:
    y = cur.year
    m = cur.month
    d = cur.day

    if y % (m * d) == 0:
        print(f"{y:04d}/{m:02d}/{d:02d}")
        break

    cur += timedelta(days=1)
