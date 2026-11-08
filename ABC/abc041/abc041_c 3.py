#100点解法
N = int(input())
a = list(map(int, input().split()))

students = [(a[i], i + 1) for i in range(N)]

for a_i, i in sorted(students, reverse=True):
    print(i)
