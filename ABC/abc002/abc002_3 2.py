import numpy

x_a, y_a, x_b, y_b, x_c, y_c = map(int, input().split())

AB = numpy.array([x_b - x_a, y_b - y_a])
AC = numpy.array([x_c - x_a, y_c - y_a])

print((sum(AB ** 2) * sum(AC ** 2) - (AB @ AC) ** 2) ** 0.5 / 2)