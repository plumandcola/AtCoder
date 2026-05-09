X, A, D, N = map(int, input().split())

if D < 0:
    A = A + D * (N-1)
    D *= -1

if A <= X <= A + D * (N-1):
    if D == 0: #ZeroDivisionErrorを防ぐ
        print(0)
    else:
        print(min((X-A) % D, D - (X-A) % D))
elif X < A:
    print(A - X)
elif A + D * (N-1) < X:
    print(X - (A + D * (N-1)))
