#100点解法
N = int(input())
a = list(map(int, input().split()))

students = {}
for i in range(N):
    students[a[i]] = i + 1

for a_i in sorted(a, reverse=True):
    print(students[a_i])
