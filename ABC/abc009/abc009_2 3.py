first = 0 #最も高い金額
second = -1 #2番目に高い金額

N = int(input())

for _ in range(N):
    A = int(input())
    if A > first:
        second = first
        first = A
    elif first > A > second:
        second = A

print(second)