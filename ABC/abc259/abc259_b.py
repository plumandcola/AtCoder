import math

a, b, d = map(int, input().split())

theta = math.radians(d)

print(a * math.cos(theta) - b * math.sin(theta), a * math.sin(theta) + b * math.cos(theta))