N = int(input())

h = N // 3600
m = (N // 60) % 60
s = N % 60

print(f"{h:02}:{m:02}:{s:02}")