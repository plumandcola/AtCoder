N = int(input())

a = set()
for i in range(N):
    L_and_a = list(map(int, input().split()))
    a.add(tuple(L_and_a[1:]))

print(len(a))