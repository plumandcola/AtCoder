from sortedcontainers import SortedList

A = SortedList()

Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    x = query[1]
    if query[0] == 1:
        A.add(x)
    elif query[0] == 2:
        k = query[2]
        i = A.bisect_right(x)
        if i < k:
            print(-1)
        else:
            print(A[i - k])
    elif query[0] == 3:
        k = query[2]
        i = A.bisect_left(x)
        if i + k - 1 >= len(A):
            print(-1)
        else:
            print(A[i + k - 1])