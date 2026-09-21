N = int(input())
A = {i: a for i, a in enumerate(map(int, input().split()))}

default = -1
Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    match query[0]:
        case 1:
            x = query[1]
            default = x
            A = {}
        case 2:
            i = query[1] - 1
            x = query[2]
            A[i] = A.get(i, default) + x
        case 3:
            i = query[1] - 1
            print(A.get(i, default))
