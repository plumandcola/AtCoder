T = int(input())
for _ in range(T):
    N = int(input())
    print(sum(A % 2 for A in map(int, input().split())))
