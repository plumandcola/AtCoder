import bisect

Deg, Dis = map(int, input().split())

Dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
i = ((Deg * 10 + 1125) // 2250) % 16
Dir = Dirs[i]

if Dis < 15:  Dir = "C"

Diss = [15, 93, 201, 327, 477, 645, 831, 1029, 1245, 1467, 1707, 1959]
W = bisect.bisect_right(Diss, Dis)

print(Dir, W)