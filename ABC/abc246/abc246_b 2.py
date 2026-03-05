import math

A, B = map(int, input().split())

theta = math.atan2(B, A)

print(math.cos(theta), math.sin(theta))