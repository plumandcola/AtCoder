N = int(input())
a = list(map(int, input().split()))

print(min(sum((a[i] - x) ** 2 for i in range(N)) for x in range(-100, 101)))