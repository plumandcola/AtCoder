N = int(input())

h = N // 3600
m = (N // 60) % 60
s = N % 60

print("{:02}:{:02}:{:02}".format(h, m, s))