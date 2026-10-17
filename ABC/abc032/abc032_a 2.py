import math

lcm = math.lcm(int(input()), int(input()))

print((int(input()) + lcm - 1) // lcm * lcm)