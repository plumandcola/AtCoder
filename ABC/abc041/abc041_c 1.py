#30点解法
N = int(input())
a = list(map(int, input().split()))

for a_i in sorted(a, reverse=True):
    print(a.index(a_i) + 1)
